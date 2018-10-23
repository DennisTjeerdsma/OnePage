import Vue from 'vue';
import Router from 'vue-router';
import Books from '@/components/Books';
import Dus from '@/components/Dus';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Books',
      component: Books,
    },
    {
      path: '/dus',
      name: 'Dus',
      component: Dus,
    },
  ],
  mode: 'hash',
});
