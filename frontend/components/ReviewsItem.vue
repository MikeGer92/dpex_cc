<template>
  <div class="review">
    <div class="row review-author">
      <div class="review-author-image">
        <img src="/images/photo.jpg" alt="">
      </div>
      <div class="review-author-name">Владимир</div>
    </div>
    <div class="review-title">Благодарю, обмен прошел оперативно! Однозначно рекомендую!</div>
    <div class="review-text">
      Мы очень рады партнерству с мониторингами обменников и готовы делиться прибылью за привлеченных пользователей.
      Наши партнеры зарабатывают 0,8% с каждого обмена, в том числе с заявок незарегистрированных пользователей
    </div>
    <div class="row review-change">
      <img src="~assets/images/bitcoin.png" alt="">
      <base-icon width="18" height="18" view-box="0 0 48 48">
        <icon-arrows/>
      </base-icon>
      <img src="~assets/images/ltc.png" alt="">
    </div>

    <div class="row review-info">
      <rating-stars :rating="3"/>
      <div class="review-text review-date">2021-08-01 13:30</div>
    </div>
  </div>
</template>

<script>
  import BaseIcon from "./BaseIcon";
  import IconArrows from "./icons/IconArrows";
  import RatingStars from "./RatingStars";

  export default {
    components: {BaseIcon, IconArrows, RatingStars}
  }
</script>
