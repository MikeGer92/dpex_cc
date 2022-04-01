<template>
  <div class="row bread">
    <nuxt-link to="/" class="bread-link">Главная</nuxt-link>
    <base-icon width="14" height="8" view-box="0 0 14 8" fill="none">
      <icon-stroked-arrow/>
    </base-icon>
    <nuxt-link :to="currentPage.path" class="bread-link">{{ currentPage.title }}</nuxt-link>
  </div>
</template>

<script>
  import BaseIcon from "./BaseIcon";
  import IconStrokedArrow from "./icons/IconStrokedArrow";

  export default {
    components: {BaseIcon, IconStrokedArrow},
    props: {
      currentPage: {
        type: Object,
        required: true
      }
    }
  }
</script>
