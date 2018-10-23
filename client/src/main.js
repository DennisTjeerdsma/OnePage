// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

/* absolute imports */
import '@/assets/css/tailwind.css';

/* relative imports */
import Vue from 'vue';
import App from './App';
import router from './router';

Vue.config.productionTip = false;

/* Initiate components */

/* eslint-disable no-new */
new Vue({
  el: '#app',
  data: {
  },
  router,
  components: { App },
  template: '<App/>',
});
