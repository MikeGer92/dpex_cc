<template>
  <div class="full api">
    <div class="cabinet-content">
      <div class="cabinet-body">
        <div class="cabinet-view">
          <h3 class="cabinet-title">Доступ к REST-API</h3>
          <p class="api-text">(Интерфейс прикладного программирования) представляет собой набор готовых классов,
            процедур, функций,
            структур и констант, предоставляемых службой для использования во внешних программных продуктах.
            Используется программистами при написании всевозможных приложений.</p>
          <div class="row api-buttons">
            <button class="btn api-btn">Создать API доступ</button>
            <a href="#" class="api-bordered-btn">Documentation</a>
          </div>

          <div class="align-top api-qr">
            <div class="qr"></div>
            <div class="api-info">
              <div class="cabinet-title">Сохранить доступ к API</div>
              <div class="row api-row">
                <div class="api-key">KEY:</div>
                <div class="row api-value">
                  <span>EX_9D1C1C3B07D341E3164D3ABB04ABEB69D026C125</span>
                  <button>
                    <base-icon width="18" height="18" view-box="0 0 18 18" fill="422E93">
                      <icon-copy/>
                    </base-icon>
                  </button>
                </div>
              </div>
              <div class="row api-row">
                <div class="api-key">SECRET:</div>
                <div class="row api-value">
                  <span>47d98d8a99bd9bbe6c6f63359f31149e33cb1aeb</span>
                  <button>
                    <base-icon width="18" height="18" view-box="0 0 18 18" fill="422E93">
                      <icon-copy/>
                    </base-icon>
                  </button>
                </div>
              </div>
              <div class="row api-row">
                <div class="api-key">Доступ:</div>
                <div class="row api-value">
                  <label class="row check">
                    <input type="checkbox">
                    <span class="row check-box"/>
                    <span class="check-text">Включить API</span>
                  </label>
                  <label class="row check">
                    <input type="checkbox">
                    <span class="row check-box"/>
                    <span class="check-text">Разрешить вывод</span>
                  </label>
                </div>
              </div>
            </div>
          </div>

          <div class="api-table">
            <table>
              <thead>
              <tr>
                <th>API-key</th>
                <th>Создано</th>
                <th>Удалить</th>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td>
                  <base-icon width="18" height="18" view-box="0 0 18 18" fill="#422E93">
                    <icon-key />
                  </base-icon>
                  <span>EX_9D1C1C3B07D341E3164D3ABB04ABEB69D026C125</span>
                </td>
                <td>12.04.21 14:04</td>
                <td class="api-delete">
                  <base-icon width="18" height="18" view-box="0 0 18 18" fill="#422E93">
                    <icon-delete/>
                  </base-icon>
                </td>
              </tr>
              </tbody>
            </table>
          </div>

          <div class="api-access">
            <h3 class="cabinet-title">Для доступа к этому API требуется авторизация, и вы должны использовать
              POST-запросы.</h3>
            <p>
              <span>URL</span> - Вы так же должны использовать этот адрес
              https://domain.com/service/api/v1/{method_name} page.user.where method_name - Это имя метода
              page.user.auth_with
            </p>
            <p>
              <span>Apikey</span> - Открытый ключ, необходимо принять настройки профиля пользователя ( Открытый ключ,
              необходимо принять настройки профиля пользователя:EF04794F718A3FC8C6DFA0B)
            </p>
            <p>
              <span>Hash</span> - Параметры GET и POST (в форме одного json) алгоритм SHA512 получил от них контрольную
              сумму, и
              следующим шагом является повторное выполнение хеша SHA512 (контрольная сумма + секрет), подписанного
              методом секретного ключа, секретный ключ также должен быть взят в настройки профиля пользователя.
            </p>
            <p>
              Кроме того, все запросы должны содержать требуемый параметр времени с числовым значением времени unix (>
              0). Это значение не должно повторяться или уменьшаться. (для безопасности вашей хэш-подписи)
            </p>
          </div>

          <div class="api-block">
            <h3 class="api-block-title">An example of creating hash in javascript</h3>
            <div class="api-code">
              <p>const <span>crypto</span> = require(<span>'crypto'</span>);</p>
              <br>
              <p>const <span>GET_PARAMS</span> = {time:123456789}</p>
              <p>const <span>POST_PARAMS</span> = {param1:'val1'}</p>
              <p>const <span>YOUR_SECRET</span> = '97aab8410868ba7c1824f490999607c0ce46a3de';</p>
              <br>
              <p>const <span>params</span> = {...<span>GET_PARAMS</span>,...<span>POST_PARAMS</span>};</p>
              <p>const checksumParams = crypto.createHash('sha256').update(JSON.stringify(params)).digest('hex');</p>
              <p>const <span>HASH</span> = crypto.createHash('sha256').update(checksumParams + <span>YOUR_SECRET</span>).digest('hex');
              </p>
              <br>
              <p>console.log('result <span>HASH</span>:', <span>HASH</span>);</p>
              <p>// ---------- result ------- ^^</p>
            </div>
          </div>

          <div class="api-block">
            <h3 class="api-block-title">Example headers:</h3>
            <div class="api-code">
              <p>apikey: 8c50e2809306b61b9b5f6253f89ed203a60e624f</p>
              <p>hash: ac876c6314ffcca01b0e65571cc136cedfb2c3d8e2194aaaf364ca7123568fc7</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import BaseIcon from "~/components/BaseIcon";
  import IconCopy from "~/components/icons/IconCopy";
  import IconDelete from "~/components/icons/IconDelete";
  import IconKey from "~/components/icons/IconKey";

  export default {
    components: {BaseIcon, IconCopy, IconDelete, IconKey}
  }
</script>
