<template>
  <div class="page-info">
    <div class="wrapper">
      <bread-crumbs :current-page="link"/>
      <h1 class="title">{{ link.title }}</h1>
    </div>
  </div>
</template>

<script>
  import BreadCrumbs from "./BreadCrumbs";

  export default {
    components: {BreadCrumbs},
    props: {
      link: {
        type: Object,
        required: true
      }
    }
  }
</script>
