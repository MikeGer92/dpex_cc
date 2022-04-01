<template>
  <div class="page">
    <page-info :link="currentLink"/>

    <div class="rules">
      <div class="wrapper">
        <form class="input">
          <input type="text" placeholder="Поиск">
          <button type="submit" class="input-btn">
            <base-icon width="67" height="32" view-box="0 0 67 32" fill="none">
              <icon-submit-arrow/>
            </base-icon>
          </button>
        </form>

        <div class="rules-items">
          <div class="rules-item">
            <h3 class="rules-title">1. Стороны соглашения</h3>
            <div class="rules-text">
              <p>Договор заключается между интернет сервисом по обмену титульных знаков, далее Исполнитель, — с одной
                стороны, и Заказчик, в лице того, кто воспользовался услугами Исполнителя, — с другой стороны.</p>
            </div>
          </div>
          <div class="rules-item">
            <h3 class="rules-title">2. Список терминов</h3>
            <div class="rules-text">
              <p>
                Обмен титульных знаков — автоматизированный продукт интернет обслуживания, который предоставляется
                Исполнителем на основании данных правил.
              </p>
              <p>
                Заказчик — физическое лицо, соглашающееся с условиями Исполнителя и данного соглашения, к которому
                присоединяется.
              </p>
              <p>
                Сервис 24bestex (Сервис) – система предоставления интернет-услуг по обмену, продаже и покупке
                электронных активов и электронных денежных средств, которая предоставляет свои услуги через сайт
                24bestex.com
              </p>
              <p>
                Титульный знак — условная единица той или иной платежной системы, которая соответствует расчетам
                электронных систем и обозначает объем прав, соответствующих договору системы электронной оплаты и ее
                Заказчика.
              </p>
              <p>
                Заявка — сведения, переданные Заказчиком для использования средств Исполнителя в электронном виде и
                свидетельствующие о том, что он принимает условия пользования сервисом, которые предлагаются
                Исполнителем в данной заявке.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import PageInfo from "../components/PageInfo";
  import BaseIcon from "../components/BaseIcon";
  import IconSubmitArrow from "../components/icons/IconSubmitArrow";

  export default {
    components: {PageInfo, BaseIcon, IconSubmitArrow},
    computed: {
      currentLink() {
        return {title: 'Правила обмена', path: '/rules'}
      }
    }
  }
</script>
