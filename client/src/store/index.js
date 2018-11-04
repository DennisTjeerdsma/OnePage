import Vue from 'vue'
import Vuex from 'vuex'
import bookList from './books.js'

Vue.use(Vuex)

export default new Vuex.Store({
  namespace: true,
  modules: {
    bookList
  }
})
