<template>
  <div class="page">
    <page-info :link="currentLink"/>

    <diagram/>

    <div class="wrapper">
      <request-form title="Заполните заявку, и мы с вами свяжемся" image="/images/form/questions.svg"/>
    </div>
  </div>
</template>

<script>
  import PageInfo from "../components/PageInfo";
  import Diagram from "../components/Diagram";
  import RequestForm from "../components/RequestForm";

  export default {
    components: {PageInfo, Diagram, RequestForm},
    computed: {
      currentLink() {
        return {title: 'Партнерская программа', path: '/partners'}
      }
    }
  }
</script>
