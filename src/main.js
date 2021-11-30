import Vue from 'vue'
import App from './App.vue';
import './registerServiceWorker';
import router from './router';
import store from './store';
import '/node_modules/materialize-css/dist/js/materialize.minmaterialize';

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')