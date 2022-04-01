<template>
  <div class="page">
    <page-info :link="currentLink"/>

    <div class="wrapper">
      <request-form title="Остались вопросы, мы поможем" image="/images/form/contacts.svg"/>

      <contacts-info/>
    </div>

    <contacts-map/>
  </div>
</template>

<script>
  import PageInfo from "../components/PageInfo";
  import RequestForm from "../components/RequestForm";
  import ContactsInfo from "../components/contacts/ContactsInfo";
  import ContactsMap from "../components/contacts/ContactsMap";

  export default {
    components: {PageInfo, RequestForm, ContactsInfo, ContactsMap},
    computed: {
      currentLink() {
        return {title: 'Контакты', path: '/contacts'}
      }
    }
  }
</script>
