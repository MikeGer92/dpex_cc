import io
from typing import Optional, List

import aiosmtplib
from fastapi import FastAPI, status, Response, Depends, File, UploadFile, Form
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse
from weasyprint import HTML, CSS
import aiohttp
import models
import time
import json
import hashlib
import os
import db
import urllib.parse
from email.message import EmailMessage


app = FastAPI()


ONE_DAY = 86400


@app.on_event("startup")
async def startup():
    app.state.fiat = {}
    app.state.crypto = {}
    app.state.operations = models.CurrencyOperations()
    app.state.currencies_tm = 0
    app.state.config = read_config()

    app.state.db_pool = await db.init(app.state.config['db'])


@app.on_event("shutdown")
async def shutdown():
    if app.state.db_pool:
        await db.close(app.state.db_pool)


@app.get("/api/currencies/sell", response_model=models.CurrencyList)
async def sell():
    await check_cache()
    response_currencies = models.CurrencyList()
    for currency_operations in app.state.operations.__root__.values():
        response_currencies.__root__.append(currency_operations.currency)

    return sorted(response_currencies.__root__, key=lambda i: i.label)


@app.get('/api/currencies/buy', response_model=models.CurrencyList)
async def buy(a: str):
    await check_cache()
    response_currencies = models.CurrencyList()
    for currency_operation in app.state.operations.__root__[a].buy.values():
        response_currencies.__root__.append(
            currency_operation.currency
        )

    return sorted(response_currencies.__root__, key=lambda i: i.label)


@app.get('/api/rates', response_model=models.Rates)
async def get_rates_test():
    await check_cache()
    config = app.state.config
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.mercuryo.io/v1.6/public/rates?widget_id={config["widget_id"]}') as response:
            json_response = await response.json()
            tether_grow_rub = float(json_response['data']['buy']['USDT']['RUB'])/100*5+float(json_response['data']['buy']['USDT']['RUB'])
            tether_grow_usd = float(json_response['data']['buy']['USDT']['USD'])/100*5+float(json_response['data']['buy']['USDT']['USD'])
            rates = models.Rates(
                btc=models.Rate(rub=json_response['data']['buy']['BTC']['RUB'], usd=json_response['data']['buy']['BTC']['USD']),
                tether=models.Rate(rub=json_response['data']['buy']['USDT']['RUB'], usd=json_response['data']['buy']['USDT']['USD']),
                tether_grow=models.Rate(rub=tether_grow_rub, usd=tether_grow_usd),
                eth=models.Rate(rub=json_response['data']['buy']['ETH']['RUB'], usd=json_response['data']['buy']['ETH']['USD']),
            )
            return rates


@app.post("/api/amount", response_model=models.AmountResponse,  responses={400: {"model": str}, 500: {"model": str}})
async def get_amount(
    data: models.AmountRequest,
    response: Response,
):
    await check_cache()
    config = app.state.config
    providers = app.state.operations.__root__[data.currency_a.name].buy[data.currency_b.name.upper()].providers
    if models.Provider.GROW in providers:
        link = f'{config["grow_domain"]}/api/v6/payment/request'
        json_data = {
            "amount": data.amount_a,
            "coin": data.currency_b.name.lower(),
            "currency": data.currency_a.name,
            "locale": "ru"
        }
        headers = auth_headers(config)
        async with aiohttp.ClientSession() as session:
            async with session.post(link, data=json_data, headers=headers) as response:
                response_json = await response.json()               

                if response.status == 403:
                    return JSONResponse(
                        status_code=403,
                        content='Не авторизован'
                    )
                elif response.status == 200 and response_json['status'] == 0:
                    return JSONResponse(
                        status_code=400,
                        content="The amount or the coin field is required."
                    )
                else:
                    if response_json['status'] == 1:
                        return models.AmountResponse(
                            amount_fiat=data.amount_a,
                            amount_crypto=response_json["merchant_amount"],
                            buttons=[
                                models.Button(
                                    label='Перевод без KYC',
                                    color='',
                                    link='',
                                    provider=models.Provider.GROW
                                )
                            ]
                        )
    else:    
        amount = data.amount_a or data.amount_b
        currency_a, currency_b = (data.currency_a, data.currency_b) if data.amount_a else (
            data.currency_b, data.currency_a)
        convert_type = 'buy'
        if currency_a.type == models.CurrencyType.CRYPTO:
            convert_type = 'sell'
        async with aiohttp.ClientSession() as session:
            link = f'{config["mercuryo_domain"]}/v1.6/public/convert?from={currency_a.name}&to={currency_b.name}&type={convert_type}&amount={amount}&widget_id={config["widget_id"]}'

            async with session.get(link) as response:
                response_json = await response.json()
                message = response_json.get('message')
                if message == 'Amount off limits.':
                    return JSONResponse(
                        status_code=400,
                        content=f'Сумма должна быть в диапазоне: {currency_a.label} от {response_json["data"][currency_a.name]["min"]} до {response_json["data"][currency_a.name]["max"]}, ' \
                            f'{currency_b.label} от {response_json["data"][currency_b.name]["min"]} до {response_json["data"][currency_b.name]["max"]}'
                    )
                elif message == f'Currency {currency_b.name} is not supported.':
                    return JSONResponse(
                        status_code=400,
                        content=f'Валюта {currency_b.name} не поддерживается.'
                    )

                if not data.wallet_address:
                    return JSONResponse(
                        status_code=400,
                        content=f'Введите адрес кошелька'
                    )
                signature = get_signature(data.wallet_address, config["secret"])
                return models.AmountResponse(
                    amount_fiat=response_json["data"]["fiat_amount"],
                    amount_crypto=response_json["data"]["amount"],
                    buttons=[
                        models.Button(
                            label='Перевод с KYC',
                            color='',
                            link=get_link(
                                    config,
                                    currency_a,
                                    currency_b,
                                    response_json["data"]["amount"],
                                    response_json["data"]["fiat_amount"],
                                    convert_type,
                                    data.wallet_address,
                                    signature
                                ),
                            provider=models.Provider.MERCURYO
                        )
                    ]
                )


@app.post("/api/grow/ads/list", response_model=models.Ads)
async def get_ads(data: models.AmountRequest):
    config = app.state.config
    async with aiohttp.ClientSession() as session:
        link = f'{config["grow_domain"]}/api/v6/payment/request'
        json_data = {
            "amount": data.amount_a,
            "coin": data.currency_b.name.lower(),
            "currency": data.currency_a.name,
            "locale": "ru"
        }
        headers = auth_headers(config)
        ads = models.Ads()
        async with session.post(link, json=json_data, headers=headers) as response:
            response_json = await response.json()
            if response.status == 403:
                return JSONResponse(
                    status_code=403,
                    content='Не авторизован'
                )
            else:
                if response_json['status'] == 1:
                    for item in response_json['data']:
                        if item['currency'].upper() == data.currency_a.name.upper():
                            ads.__root__.append(
                                models.Ad(bank=item["bank_name"], id=item["ad_id"])
                            )
                else:
                    return JSONResponse(
                        status_code=400,
                        content=response_json.get('error', 'Сервис временно недоступен. Попробуйте позже.')
                    )                    
        return ads


@app.post("/api/grow/invoices", response_model=models.GrowInvoice)
async def invoices(data: models.GrowPayment):
    config = app.state.config
    async with aiohttp.ClientSession() as session:
        link = f'{config["grow_domain"]}/api/v6/payment/create'
        json_data = {
          "ad_id": data.ad_id,
          "amount": data.amount,
          "coin": data.coin.lower(),
          "address": data.address,
          "currency": data.currency,
          "payment_info": data.payment_info,
          "locale": "ru"
        }
        headers = auth_headers(config)
        async with session.post(link, json=json_data, headers=headers) as response:
            response_json = await response.json()
            if response_json['status'] == 1:
                token = hashlib.md5(str(response_json['data']['invoice_id']).encode()+config['secret'].encode()).hexdigest()
                invoice = models.GrowInvoice(
                    fiat_amount='',
                    fiat=data.currency,
                    crypto=data.coin,
                    fio=data.payment_info,
                    wallet_address=data.address,
                    invoice_id=int(response_json['data']['invoice_id']),
                    token=str(token)
                )
                return invoice
            else:
                return JSONResponse(
                    status_code=400,
                    content=response_json['error']
                )


@app.post("/api/grow/invoices/status", response_model=models.GrowInvoiceStatus)
async def check_status(data: models.GrowInvoice):
    config = app.state.config
    token = hashlib.md5(str(data.invoice_id).encode()+config['secret'].encode()).hexdigest()
    
    if token == data.token:
        async with aiohttp.ClientSession() as session:
            link = f'{config["grow_domain"]}/api/v6/payment/check/approved'
            json_data = {
                "invoice_id": data.invoice_id,
                "locale": "ru"
            }
            headers = auth_headers(config)
            async with session.post(link, json=json_data, headers=headers) as response:
                json_response = await response.json()
                try:
                    if json_response['status'] == 1:
                        bank_props = models.BankProps(
                            amount=float(json_response['data']['amount']),
                            card=json_response['data']['card_number'],
                            bank=json_response['data']['bank_name'],
                            currency=json_response['data']['currency']
                        )
                        invoice_status = models.GrowInvoiceStatus(
                            status=models.PaymentStatus.READY,
                            data=bank_props
                        )
                        return invoice_status
                    elif json_response['status'] == 0:
                        if 'PI000' in json_response['error_code']:
                            invoice_status = models.GrowInvoiceStatus(
                                status=models.PaymentStatus.WAITING,
                                data=None
                            )
                            return invoice_status
                        else:
                            return JSONResponse(
                                status_code=400,
                                content='Ваш запрос на перевод был отклонен'
                            )
                except:
                    return JSONResponse(
                        status_code=400,
                        content=json_response
                    )
    else:
        return JSONResponse(
            status_code=401,
            content='Invalid token'
        )


@app.post('/api/grow/invoices/done')
async def done(invoice_id: int = Form(...), file: Optional[UploadFile] = File(None)):
    config = app.state.config
    async with aiohttp.ClientSession() as session:
        link = f'{config["grow_domain"]}/api/v6/payment/confirm'
        headers = auth_headers(config)
        if file is None:
            json_data = {
                "invoice_id": invoice_id,
                "locale": "ru"
            }
            response = await session.post(link, json=json_data, headers=headers)
            response_json = await response.json()
            if response_json['status'] == 1:
                return JSONResponse(
                    status_code=200,
                    content='Оплата прошла успешно'
                )
            else:
                return JSONResponse(
                    status_code=400,
                    content='Платеж еще не утвержден',
                    
                )
        else:
            data = aiohttp.FormData()
            data.add_field('invoice_id', str(invoice_id))
            data.add_field('locale', 'ru')
            data.add_field('document', file.file._file, content_type=file.content_type, filename=file.filename)
            response = await session.post(link, data=data, headers=headers)

            response_json = await response.json()
            if response_json['status'] == 1:
                return JSONResponse(
                    status_code=200,
                    content='Оплата прошла успешно'
                )
            else:
                return JSONResponse(
                    status_code=400,
                    content='Платеж еще не утвержден',
                )


@app.post('/api/grow/invoices/payed/status', response_model=models.GrowInvoicePayedStatus)
async def payed_status(
    data: models.GrowInvoice,
    db_conn: db.Connection = Depends(db.get)
):
    config = app.state.config
    link = f'{config["grow_domain"]}/api/v6/payment/check/status'
    json_data = {
        "invoice_id": data.invoice_id,
        "locale": "ru"
    }
    headers = auth_headers(config)
    token = hashlib.md5(str(data.invoice_id).encode() + config['secret'].encode()).hexdigest()
    if token == data.token:
        async with aiohttp.ClientSession() as session:
            async with session.post(link, json=json_data, headers=headers) as response:
                response_json = await response.json()
                try:
                    if response_json['status'] == 1:
                        # типы статусов оплаты:
                        # -1 - Payment canceled
                        # 0 - Payment is being processed
                        # 1 - Payment paid (платеж подтвержден со стороны трейдера)
                        # 2 - Payment confirmed (со стороны пользователя)

                        if response_json['data']['status']['id'] == -1:
                            return JSONResponse(
                                status_code=400,
                                content='Платеж отклонен'
                            )

                        if response_json['data']['status']['id'] != 1 or not response_json['data']['status'].get('address_amount_current'):
                            return models.GrowInvoicePayedStatus(
                                status=models.PaymentStatus.WAITING
                            )
                        
                        response_json['crypto'] = data.crypto
                        response_json['fiat'] = data.fiat
                        response_json['fiat_amount'] = data.fiat_amount
                        response_json['address'] = data.wallet_address
                        response_json['fio'] = data.fio
                        row = await db_conn.fetchrow("INSERT INTO callback_data (data_jsonb, provider, ctime) VALUES ($1, 'grow', now() at time zone 'utc') RETURNING id", response_json)
                        check_token = hashlib.md5(str(row["id"]).encode() + config['secret'].encode()).hexdigest()
                        return models.GrowInvoicePayedStatus(
                            status=models.PaymentStatus.READY,
                            check_url=f'/check/pdf/{row["id"]}/{check_token}'
                        )
                    elif response_json['status'] == 0:
                        return models.GrowInvoicePayedStatus(
                            status=models.PaymentStatus.WAITING
                        )
                    else:
                        return JSONResponse(
                            status_code=400,
                            content='Error'
                        )
                except:
                    return JSONResponse(
                        status_code=400,
                        content=response_json
                    )
    else:
        return JSONResponse(
            status_code=401,
            content="Invalid token"
        )


MERCURYO_STATUS = {
    'new': 'исполняется',
    'pending': 'исполняется',
    'completed': 'выполнена',
    'cancelled': 'отменина',
    'paid': 'выполнена',
    'order_failed': 'отменина',
    'descriptor_failed': 'отменина'
}


@app.get('/check/pdf/{id}/{token}')
async def check_pdf(
    id: int,
    token: str,
    db_conn: db.Connection = Depends(db.get)
):
    config = app.state.config
    calculated_token = hashlib.md5(str(id).encode() + config['secret'].encode()).hexdigest()
    if token != calculated_token:
        return JSONResponse(
            status_code=400,
            content="Invalid token"
        )
    data = await db_conn.fetchrow(f"SELECT * FROM callback_data WHERE id={id}")
    if not data:
        return JSONResponse(
            status_code=400,
            content="Invalid id"
        )
    data = dict(data)
    if data['provider'] == models.Provider.GROW:
        amount = data['data_jsonb']['data']['status']['address_amount_current']
        fiat_amount = data['data_jsonb']['fiat_amount']
        status = data['data_jsonb']['data']['status']['message']
    else:
        amount = data['data_jsonb']['data']['amount']
        fiat_amount = data['data_jsonb']['data']['fiat_amount']
        status = MERCURYO_STATUS[data['data_jsonb']['data']['status']]
    html = HTML(string=f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/grow.css">
    <title>Document</title>
</head>
<body>
    <div class="container">
        <div class="checkGrow">
            <div class="logo"></div>
            <div class="date">{utc2local(data['ctime']).strftime("%Y-%m-%d %H:%M:%S")}</div>
            <div class="wrapp wrapp-result">
                <div class="total">Итого</div>
                <div class="cash">{fiat_amount} {data['data_jsonb']['fiat']}</div>
            </div>
            <div class="hr">&nbsp;</div>
            <div class="wrapp wrapp-status">
                <div class="maintext status">Статус</div>
                <div class="maintext status-result">{status}</div>
            </div>
            <div class="wrapp wrapp-sender">
                <div class="maintext sender">Отправитель</div>
                <div class="maintext status-name">{data['data_jsonb']['fio']}</div>
            </div>
            <div class="wrapp wrapp-wallet">
                <div class="maintext reciviers-wallet">Кошелек получателя</div>
                <div class="maintext currency">{data['data_jsonb']['crypto']}</div>
            </div>
            <div class="wallet-name">{data['data_jsonb']['address']}</div>
            <div class="wrapp wrapp-recieve-cash">
                <div class="maintext recieve-descr">Зачисленная сумма</div>
                <div class="maintext recieve-cash">{amount} {data['data_jsonb']['crypto']}</div>
            </div>
            <div class="wrapp wrapp-operation">
                <div class="maintext operation-descr">Назначение платежа</div>
                <div class="maintext operation">Покупка криптовалюты</div>
            </div>
            <div class="print"></div>
            <div class="hr">&nbsp;</div>
            <div class="reception">Квитанция {'G' if data['provider'] == models.Provider.GROW else 'M'}{data['ctime'].strftime("%d-%m-%Y")}-{id}</div>
            <div class="support">При возникновении вопросов по транзакции <br> обращайтесь 
                в службу поддержки: https://t.me/@Dpexinf</div>
        </div>
    </div>
    
</body>
</html>
    ''')

    css = CSS(filename='static/grow.css')
    pdf_io = html.write_pdf(stylesheets=[css], presentational_hints=True)
    return StreamingResponse(io.BytesIO(pdf_io))


@app.post("/api/provider/callback")
async def provider_callback(
    data: dict,
    db_conn: db.Connection = Depends(db.get)
):
    pk = data['data']['id']
    row = await db_conn.fetchrow("SELECT id FROM callback_data WHERE data_jsonb#>>'{data,id}' = $1 AND provider = $2 ORDER BY id DESC LIMIT 1", str(pk), models.Provider.MERCURYO)
    data['crypto'] = data['data']['currency']
    data['fiat'] = data['data']['fiat_currency']
    data['address'] = data['data']['tx']['address']
    data['fio'] = ''
    if row:
        await db_conn.execute("UPDATE callback_data SET data_jsonb = $1 AND id = $2", data, row['id'])
    else:
        await db_conn.execute("INSERT INTO callback_data (data_jsonb, provider, ctime) VALUES ($1, $2, now() at time zone 'utc') RETURNING id", data, models.Provider.MERCURYO)
    return {}


@app.get("/api/check", response_model=models.CheckLink)
async def check(
    address: str,
    db_conn: db.Connection = Depends(db.get)
):
    config = app.state.config
    row = await db_conn.fetchrow("SELECT id FROM callback_data WHERE data_jsonb#>>'{address}' = $1 ORDER BY id DESC LIMIT 1", address)
    if not row:
        return JSONResponse(
            status_code=404,
            content="Платеж не найден"
        )
    check_token = hashlib.md5(str(row["id"]).encode() + config['secret'].encode()).hexdigest()
    return models.CheckLink(link=f'/check/pdf/{row["id"]}/{check_token}')


@app.post('/api/feedback')
async def feedback(data: models.FeedBack):
    config = app.state.config
    email = data.email
    telegram = data.telegram
    message = EmailMessage()
    message.set_content(f'Пришла новая заявка с формы обратной связи на сайте dpex.cc.\nEmail клиента : {email}\nTelegram клиента: {telegram}')
    message['Subject'] = 'Новая заявка с контактной формы dpex.cc'
    message['From'] = config['smtp']['sender']
    message['To'] = config['smtp']['recipient']

    try:
        conn = aiosmtplib.SMTP(hostname=config['smtp']['transport']['hostname'], port=config['smtp']['transport']['port'], use_tls=True)
        await conn.connect()
        await conn.login(username=config['smtp']['sender'], password=config['smtp']['passwd'])
        await conn.send_message(message)
        await conn.quit()
        return JSONResponse(
            status_code=200,
            content=''
        )
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content=e
        )


def get_link(
    config,
    currency_a, 
    currency_b, 
    amount_crypto, 
    amount_fiat,  
    convert_type, 
    wallet_address, 
    signature
):
    currency_crypto, currency_fiat = (currency_a, currency_b) if currency_a.type == "crypto" else (currency_b, currency_a)
    qs = urllib.parse.urlencode({
        'widget_id': config['widget_id'],
        'amount': str(amount_crypto),
        'currency': currency_crypto.name,
        'fiat_amount': str(amount_fiat),
        'fiat_currency': currency_fiat.name,
        'ref_code': config['ref_code'],
        'type': convert_type,
        'address': wallet_address,
        'signature': signature,
        'lang': 'ru',
        'return_url': f'{config["mercuryo_redirect_url"]}/payed?address={wallet_address}'
    })
    return f"{config['mercuryo_exhange']}/?{qs}"


def get_signature(address, secret):
    data = address + secret
    signature = hashlib.sha512(data.encode())
    return signature.hexdigest()


def read_config():
    config_path = 'local.json'
    if 'CONFIG' in os.environ:
        config_path = os.environ['CONFIG']

    with open(config_path, 'r') as fd:
        return json.load(fd)


async def check_cache():
    current_time = time.time()
    if not app.state.fiat or not app.state.crypto:
        await get_currencies()
    elif (current_time - app.state.currencies_tm) > ONE_DAY:
        await get_currencies()


async def get_currencies():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.mercuryo.io/v1.6/lib/currencies') as response:
            response_json = await response.json()

            operations = models.CurrencyOperations()
            fiat = {}
            crypto = {}

            at_grow = [i.name for i in models.GROW_CURRENCIES]
            at_mercuryo = []

            for key, value in response_json["data"]["config"]["display_options"].items():
                currency_type = models.CurrencyType.CRYPTO if key in response_json["data"]["crypto"] else models.CurrencyType.FIAT
                currency = models.Currency(
                    name=key,
                    label="Tether KYC" if key == 'USDT' else value["fullname"],
                    icon=response_json["data"]["config"]["icons"][key]['png'],
                    type=currency_type
                )
                if currency_type == models.CurrencyType.FIAT:
                    fiat[currency.name] = currency
                elif currency_type == models.CurrencyType.CRYPTO:
                    crypto[currency.name] = currency
                at_mercuryo.append(currency.name)
        
            for currency in models.GROW_CURRENCIES:
                if currency.type == models.CurrencyType.FIAT:
                    fiat[currency.name] = currency
                elif currency.type == models.CurrencyType.CRYPTO:
                    crypto[currency.name] = currency
            
            providers_list = [
                (models.Provider.GROW, lambda i, j: i in at_grow and j in at_grow), 
                (models.Provider.MERCURYO, lambda i, j: i in at_mercuryo and j in at_mercuryo)
            ]
            for fiat_currency in fiat.values():
                operations.__root__[fiat_currency.name] = models.CurrencyOperation(
                    currency=fiat_currency,
                    buy={
                        crypto_currency.name: models.CurrencyProvider(
                            currency=crypto_currency,
                            providers=[
                                k
                                for k, v in providers_list if v(fiat_currency.name, crypto_currency.name)
                            ]
                        )
                        for crypto_currency in crypto.values()
                    }
                )
                            
            app.state.fiat = fiat
            app.state.crypto = crypto
            app.state.currencies_tm = time.time()                
            app.state.operations = operations


def auth_headers(config) -> dict:
    return {
        "Authorization": f"Bearer {config['grow_merchant']}",
    }


def utc2local(utc):
    import datetime
    epoch = time.mktime(utc.timetuple())
    offset = datetime.datetime.fromtimestamp(epoch) - datetime.datetime.utcfromtimestamp(epoch)
    return utc + offset


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="debug")
