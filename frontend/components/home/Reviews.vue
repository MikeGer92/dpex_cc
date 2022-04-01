<template>
  <div class="reviews">
    <div class="wrapper">
      <h2 class="title">Отзывы</h2>
      <div class="reviews-items">
        <swiper :options="sliderOptions">
          <swiper-slide v-for="slide in 10" :key="slide">
            <reviews-item/>
          </swiper-slide>
        </swiper>
        <div class="reviews-pagination"/>
      </div>
    </div>
  </div>
</template>

<script>
  import {Swiper, SwiperSlide, directive} from 'vue-awesome-swiper'
  import 'swiper/css/swiper.css'
  import ReviewsItem from "../ReviewsItem";
  import { HOME } from "~/settings/const";

  export default {
    components: {Swiper, SwiperSlide, ReviewsItem},
    directives: {
      swiper: directive
    },
    data() {
      return {
        sliderOptions: HOME.reviewsSlider
      }
    }
  }
</script>
