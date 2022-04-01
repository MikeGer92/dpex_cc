<template>
  <div class="home">
    <Payed/>
    <Welcome/>
    <Partners/>
    <Diagram/>
    <Reviews/>
    <News/>
  </div>
</template>

<script>
  import Payed from "~/components/home/Payed";
  import Welcome from "~/components/home/Welcome";
  import Partners from "~/components/home/Partners";
  import Diagram from "~/components/Diagram";
  import Reviews from "~/components/home/Reviews";
  import News from "~/components/home/News";

  export default {
    components: {Payed, Welcome, Partners, Diagram, Reviews, News},
  }
</script>
