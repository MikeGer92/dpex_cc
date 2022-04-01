<template>
  <div class="partners">
    <div class="wrapper">
      <div class="partners-wrapper">
        <h3 class="subtitle partners-wrapper-item">
          РАБОТА С FINTRADE ГАРАНТИРУЕТ ВАМ:
        </h3>
        <div class="partners-wrapper-item">
          <div class="partners-guarantees">
            <guaranty-item
              v-for="partner in partnersInfo"
              :key="partner.title"
              :partners-info="partner"
            />
          </div>
        </div>
        <h3 class="subtitle partners-wrapper-item">
          ПАРТНЕРСКАЯ ПРОГРАММА ДЛЯ МОНИТОРИНГОВ
        </h3>
        <div class="partners-wrapper-item">
          <div class="partners-diagram">
            <p class="description partners-description">
              Мы очень рады партнерству с мониторингами обменников и готовы
              делиться прибылью за привлеченных пользователей. Наши партнеры
              зарабатывают до 0,8% с каждого обмена, в том числе с заявок
              незарегистрированных пользователей
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import GuarantyItem from "../GuarantyItem";
import safety from "../../assets/images/safety.png";
import speed from "../../assets/images/speed.png";
import service from "../../assets/images/service.png";
import confidentiality from "../../assets/images/confidentiality.png";

export default {
  components: { GuarantyItem },
  computed: {
    partnersInfo() {
      return [
        {
          image: safety,
          title: "БЕЗОПАСНОСТЬ",
          description:
            "Мы официально зарегистрированы и имеем легальное право обменивать криптовалюты.",
        },
        {
          image: speed,
          title: "СКОРОСТЬ",
          description:
            "За счёт современных платежных сервисов обмен на площадке DPex займёт у Вас не более 5 минут. ",
        },
        {
          image: service,
          title: "СЕРВИС",
          description:
            "Наши специалисты всегда на связи и готовы помочь Вам с любым вопросом 24/7",
        },
        {
          image: confidentiality,
          title: "КОНФИДЕНЦИАЛЬНОСТЬ",
          description:
            "Мы очень бережно относимся к данным наших клиентов и партнёров. С нами можете не переживать за сохранность Ваших данных",
        },
      ];
    },
  },
};
</script>
