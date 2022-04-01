<template>
  <div class="contacts-map">
    <yandex-map v-if="showMap" :coords="coords" :controls="controls" :zoom="18">
      <ymap-marker :coords="coords" :balloon="{}" marker-id="123"/>
    </yandex-map>
    <div class="wrapper">
      <div class="contacts-info">
        <div class="contacts-city">Москва</div>
        <div class="contacts-subtitle">Адрес</div>
        <address class="contacts-address">Россия, Москва, Мясницкая ул., 16</address>
      </div>
    </div>
  </div>
</template>

<script>
  import {yandexMap, ymapMarker} from 'vue-yandex-maps'

  export default {
    components: {yandexMap, ymapMarker},
    data() {
      return {
        showMap: false,
        controls: [],
        coords: [55.7522, 37.6156],
      }
    },
    mounted() {
      this.showMap = true
    }
  }
</script>
