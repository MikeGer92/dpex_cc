<template>
  <div class="news">
    <div class="wrapper">
      <h2 class="title">Новости</h2>
      <div class="align-top news-items">
        <news-item v-for="news in newsItems" :key="news.title" :news="news"/>
      </div>
    </div>
  </div>
</template>

<script>
  import NewsItem from "../NewsItem";
  import {NEWS} from "~/settings/const";

  export default {
    components: {NewsItem},
    computed: {
      newsItems() {
        return NEWS.items
      }
    }
  }
</script>
