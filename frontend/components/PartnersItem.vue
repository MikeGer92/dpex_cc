<template>
  <div class="partner">
    <div class="partner-circle" />
    <div class="partner-title">{{ partnersInfo.title }}</div>
    <div class="partner-description">{{ partnersInfo.description }}</div>
  </div>
</template>

<script>
  export default {
    props: {
      partnersInfo: {
        type: Object,
        default: {}
      }
    }
  }
</script>
