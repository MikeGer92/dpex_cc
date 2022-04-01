import Vue from 'vue'
import YmapPlugin from 'vue-yandex-maps'

const settings = {
  apiKey: '41dee9e3-0b1f-4d83-86df-7a94be4c3f99',
  lang: 'ru_RU',
  coordorder: 'latlong',
  version: '2.1'
};

Vue.use(YmapPlugin, settings);
