import Vue from 'vue'
import Vuelidate from 'vuelidate';
import App from './App.vue';
import './registerServiceWorker';
import router from './router';
import store from './store';
import dateFilter from '@/filters/date.filter';
import currencyFilter from '@/filters/currency.filter';
import tooltip from './directives/tooltip';
import messagePlugin from '@/utils/message.plugin'
import Loader from '@/components/app/Loader'
import '/node_modules/materialize-css/dist/js/materialize.min';

import firebase from 'firebase/app';
import 'firebase/auth';
import 'firebase/database';

Vue.config.productionTip = false;
Vue.use(Vuelidate);
Vue.use(messagePlugin);
Vue.filter('date', dateFilter);
Vue.filter('currency', currencyFilter);
Vue.directive('tooltip', tooltip)
Vue.component('Loader', Loader);
// const firebaseConfig = {
//   apiKey: "AIzaSyBeT2TZV1xTJZ4D_Ny8nSdAMNiK9unr69s",
//   authDomain: "newvuecrm.firebaseapp.com",
//   projectId: "newvuecrm",
//   storageBucket: "newvuecrm.appspot.com",
//   messagingSenderId: "182455846820",
//   appId: "1:182455846820:web:828ca885b43aceb223e331",
//   measurementId: "G-ZPFB13VF1D"
// };

firebase.initializeApp({
  apiKey: "AIzaSyBeT2TZV1xTJZ4D_Ny8nSdAMNiK9unr69s",
  authDomain: "newvuecrm.firebaseapp.com",
  projectId: "newvuecrm",
  storageBucket: "newvuecrm.appspot.com",
  messagingSenderId: "182455846820",
  appId: "1:182455846820:web:828ca885b43aceb223e331",
  measurementId: "G-ZPFB13VF1D",
  databaseURL: "https://newvuecrm-default-rtdb.europe-west1.firebasedatabase.app/"

});

let app;

firebase.auth().onAuthStateChanged(() => {
  if(!app) {
    app = new Vue({
      router,
      store,
      render: h => h(App)
    }).$mount('#app');
  }
  
});


