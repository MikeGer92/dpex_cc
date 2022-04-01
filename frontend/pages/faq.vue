<template>
  <div class="page">
    <page-info :link="currentLink"/>

    <div class="wrapper">

      <div class="faq-items">
        <faq-item v-for="faq in faqItems" :key="faq.ask" :ask="faq.ask" :answer="faq.answer"/>
      </div>

      <request-form :need-question="true" title="Остались вопросы, мы поможем" image="/images/form/faq.svg"/>
    </div>
  </div>
</template>

<script>
  import PageInfo from "../components/PageInfo";
  import RequestForm from "../components/RequestForm";
  import FaqItem from "../components/faq/FaqItem";

  export default {
    components: {PageInfo, RequestForm, FaqItem},
    computed: {
      currentLink() {
        return {title: 'FAQ', path: '/faq'}
      },
      faqItems() {
        return [
          {ask: 'В каком режиме работает сервис?', answer: 'Рабочий график — круглосуточно'},
          {
            ask: 'Почему при переводе средств в сети Ethereum выводится ошибка транзакции &amp«quot»Out of gas&amp«quot»?\n',
            answer: 'Рабочий график — круглосуточно'
          },
          {
            ask: 'Что такое Memo/Destination Tag/Message, когда и зачем они нужны?\n',
            answer: 'Рабочий график — круглосуточно'
          },
          {
            ask: 'Меня просят очистить Куки (Cookies) и Кеш (Chache). Как это сделать?\n',
            answer: 'Рабочий график — круглосуточно'
          },
        ]
      }
    }
  }
</script>
