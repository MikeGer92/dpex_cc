<template>
  <div class="page">
    <page-info :link="currentLink"/>

    <div class="reviews">
      <div class="wrapper">
        <div class="align-top reviews-items">
          <reviews-item v-for="review in 5" :key="review"/>
        </div>

        <request-form :need-question="true" textarea-placeholder="Оставьте свой отзыв" title="Оставьте свой отзыв"
                      image="/images/form/reviews.svg"/>
      </div>
    </div>
  </div>
</template>

<script>
  import PageInfo from "../components/PageInfo";
  import ReviewsItem from "../components/ReviewsItem";
  import RequestForm from "../components/RequestForm";

  export default {
    components: {PageInfo, ReviewsItem, RequestForm},
    computed: {
      currentLink() {
        return {title: 'Отзывы', path: '/reviews'}
      }
    }
  }
</script>
