<template>
  <div class="page">
    <page-info :link="currentLink"/>

    <div class="wrapper">
      <div class="align-top news-items">
        <news-item v-for="news in newsItems" :key="news.title" :news="news"/>
        <news-item v-for="news in newsItems" :key="news.title" :news="news"/>
        <news-item v-for="news in newsItems" :key="news.title" :news="news"/>
      </div>

      <pagination/>

      <subscribe/>
    </div>
  </div>
</template>

<script>
  import PageInfo from "../components/PageInfo";
  import NewsItem from "../components/NewsItem";
  import Pagination from "../components/Pagination";
  import Subscribe from "../components/Subscribe";
  import { NEWS } from "../settings/const";

  export default {
    components: {PageInfo, NewsItem, Pagination, Subscribe},
    computed: {
      currentLink() {
        return {title: 'Новости', path: '/news'}
      },
      newsItems() {
        return NEWS.items
      }
    }
  }
</script>
