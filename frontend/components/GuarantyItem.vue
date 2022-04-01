<template>
  <div class="guaranty">
    <div class="guaranty-icon">
      <img alt="guaranty-icon" :src="partnersInfo.image" />
    </div>
    <p class="guaranty-title">{{ partnersInfo.title }}</p>
    <div class="guaranty-description">{{ partnersInfo.description }}</div>
  </div>
</template>

<script>
export default {
  props: {
    partnersInfo: {
      type: Object,
      default: {},
    },
  },
};
</script>
