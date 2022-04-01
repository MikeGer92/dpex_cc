<template>
  <div class="news-item">
    <div class="news-image">
      <img :src="news.image" :alt="news.title">
    </div>
    <a href="#" class="news-title">{{ news.title }}</a>
    <div class="news-description">{{ news.description }}</div>
  </div>
</template>

<script>
  export default {
    props: {
      news: {
        type: Object,
        required: true
      }
    }
  }
</script>
