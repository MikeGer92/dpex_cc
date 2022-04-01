<template>
  <div class="home">
    <Main/>
    <Welcome/>
    <Partners/>
  </div>
</template>

<script>
  import Main from "../components/home/Main";
  import Welcome from "../components/home/Welcome";
  import Partners from "../components/home/Partners.vue";

  export default {
    components: {Main, Welcome, Partners }
  }
</script>
