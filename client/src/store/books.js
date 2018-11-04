import axios from 'axios'

export default {
  state: {
    bookList: []
  },
  mutations: {
    setBookList(state, bookList) {
      state.bookList = bookList
    }
  },
  actions: {
    async loadBooks({ state, commit }, data) {
      let response = await axios.get('http://localhost:5000/books', data)
      commit('setBookList', response.data)
    }
  },
  getters: {
    bookList: state => state.bookList
  }
}
