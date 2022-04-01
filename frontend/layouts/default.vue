<template>
  <div>
    <Header/>
    <Nuxt/>
    <Footer/>

    <login-modal/>
    <register-modal/>
    <thanks-modal />
  </div>
</template>

<script>
  import Header from "../components/Header";
  import Footer from "../components/Footer";
  import LoginModal from "../components/modals/LoginModal";
  import RegisterModal from "../components/modals/RegisterModal";
  import ThanksModal from "../components/modals/ThanksModal";


  export default {
    components: {Header, Footer, LoginModal, RegisterModal, ThanksModal}
  }
</script>
