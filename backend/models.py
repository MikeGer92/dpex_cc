import enum
from typing import Optional, List, Dict

from fastapi import File
from pydantic import BaseModel, root_validator, validator, Field


class CurrencyType(str, enum.Enum):
    FIAT = 'fiat'
    CRYPTO = 'crypto'


class Currency(BaseModel):
    name: str
    label: str
    icon: str
    type: CurrencyType


class CurrencyList(BaseModel):
    __root__: List[Currency] = []


class AmountRequest(BaseModel):
    currency_a: Currency
    currency_b: Currency
    amount_a: Optional[str] = Field(None, nullable=True)
    amount_b: Optional[str] = Field(None, nullable=True)
    wallet_address: str

    @root_validator
    def check_amounts(cls, values):
        if values.get('amount_a') is None and values.get('amount_b') is None:
            raise ValueError(
                'Необходимо указать количество хотя бы одной валюты')
        return values


class Provider(str, enum.Enum):
    GROW = 'grow'
    MERCURYO = 'mercuryo'


class Button(BaseModel):
    label: str
    color: str = ''
    link: str = ''
    provider: Provider


class AmountResponseFee(BaseModel):
    # __root__:  Dict[str, str]
    amount_fiat: str
    amount_crypto: str
    buttons: List[Button]


class CurrencyProvider(BaseModel):
    currency: Currency
    providers: List[Provider]


class CurrencyOperation(BaseModel):
    currency: Currency
    buy: Dict[str, CurrencyProvider]


class CurrencyOperations(BaseModel):
    __root__: Dict[str, CurrencyOperation] = {}


GROW_CURRENCIES = [
    Currency(
        name='RUB',
        label='Russian ruble',
        icon='https://api.mercuryo.io/v1.6/img/icons/currencies/rub.png',
        type=CurrencyType.FIAT
    ), 
    Currency(
        name='UAH',
        label='Ukrainian hryvnia',
        icon='https://api.mercuryo.io/v1.6/img/icons/currencies/uah.png',
        type=CurrencyType.FIAT
    ), 
    Currency(
        name='KZT',
        label='KZT',
        icon='/static/kzt_coin.jpg',
        type=CurrencyType.FIAT
    ), 
    Currency(
        name='INR',
        label='INR',
        icon='/static/inr_coin.jpg',
        type=CurrencyType.FIAT
    ), 
    Currency(
        name='TRY',
        label='Turkish lira',
        icon='https://api.mercuryo.io/v1.6/img/icons/currencies/try.png',
        type=CurrencyType.FIAT
    ),
    Currency(
        name='USDT_TRC20',
        label='Tether non-KYC',
        icon='https://api.mercuryo.io/v1.6/img/icons/currencies/usdt.png',
        type=CurrencyType.CRYPTO
    )
]


class AmountResponse(BaseModel):
    amount_fiat: str
    amount_crypto: str
    buttons: List[Button]


class Ad(BaseModel):
    bank: str
    id: str


class Ads(BaseModel):
    __root__: List[Ad] = []


class GrowPayment(BaseModel):
    ad_id: str
    amount: str
    coin: str
    address: str
    currency: str
    payment_info: str


class GrowInvoice(BaseModel):
    fiat: str
    crypto: str
    fio: str
    wallet_address: str
    fiat_amount: str
    invoice_id: int
    token: str


class BankProps(BaseModel):
    amount: float
    card: str
    bank: str
    currency: str


class PaymentStatus(str, enum.Enum):
    WAITING = 'waiting'
    READY = 'ready'


class GrowInvoiceStatus(BaseModel):
    status: PaymentStatus
    data: Optional[BankProps]


class GrowInvoicePayed(BaseModel):
    invoice_id: int


class GrowInvoicePayedStatus(BaseModel):
    status: PaymentStatus
    check_url: Optional[str] = ''


class Rate(BaseModel):
  rub: float
  usd: float


class Rates(BaseModel):
  btc: Rate
  tether: Rate
  tether_grow: Rate
  eth: Rate


class CheckLink(BaseModel):
    link: str


class FeedBack(BaseModel):
    email: str
    telegram: str
