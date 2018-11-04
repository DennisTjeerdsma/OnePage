<template class="w-full">
  <div id="Books" class="container w-screen flex flex-wrap mx-auto">
    <div class="row w-full">
      <div class="col-sm-10 w-full">
        <h1>Books</h1>
        <hr>
        <br>
        <br>
        <table class="text-left w-full">
          <div
            v-if="Alert.showMessage"
            id="alert"
            class="bg-green-lightest border border-green-light text-green-dark \ px-4 py-3 rounded relative"
            role="alert"
          >
            <div class="font-bold w-full">
              <alert :message="Alert.message"/>
            </div>
          </div>
          <br>
          <thead class="bg-black flex text-white w-full">
            <tr class="flex w-full mb-4">
              <th scope="col" class="p-4 w-1/4">Title</th>
              <th scope="col" class="p-4 w-1/4">Author</th>
              <th scope="col" class="p-4 w-1/4">Read?</th>
              <th/>
            </tr>
          </thead>
          <tbody class="w-full">
            <tr v-for="(book, index) in books.books" :key="index" class="flex w-full mb-4">
              <td class="p-4 w-1/4">{{ book.title }}</td>
              <td class="p-4 w-1/4">{{ book.author }}</td>
              <td class="p-4 w-1/4">
                <span v-if="book.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <button
                  type="button"
                  class="bg-blue hover:bg-blue-darker \ rounded text-white shadow-md py-2 px-4"
                  @click="editBookForm(book)"
                >Update</button>
                <button
                  type="button"
                  class="bg-red hover:bg-red-darker text-white \ rounded py-2 px-4"
                >Delete</button>
              </td>
            </tr>
            <tr class="w-full">
              <td class="p-4 w-1/4">
                <button
                  ref="add"
                  type="button"
                  class="bg-green-light hover:bg-green-dark rounded \ text-white px-4 py-2"
                  @click="showModal"
                >Add</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <modal v-show="isModalVisible" @close="closeModal" @added="addBook">
      <div slot="title" name="modal-title">
        <h3>Add Books</h3>
      </div>
      <div slot="body" name="modal-body">
        <h3>Title</h3>
        <input
          id="title"
          v-model="BookModal.title"
          type="text"
          name="title"
          class="border rounded"
          placeholder="Add book title here"
          required
        >
        <h3>Author</h3>
        <input
          id="author"
          v-model="BookModal.author"
          type="text"
          name="author"
          class="border rounded"
          placeholder="Add author here"
          required
        >
        <h3>Read?</h3>
        <input
          id="read"
          v-model="BookModal.read"
          type="checkbox"
          class="mr-2 leading-tight"
          name="read"
          value="true"
        >
      </div>
      <br>
      <hr>
      <br>
      <div slot="buttons" name="modal-footer">
        <button
          class="bg-green hover:bg-green-darker rounded text-white \ shadow-md py-2 px-4 w-1/3"
          @click.prevent="onSubmit"
        >Add</button>
        <button
          class="bg-red hover:bg-red-darker rounded text-white shadow-md py-2 \ px-4 w-1/3"
          type="reset"
          @click.prevent="onReset"
        >Reset</button>
      </div>
    </modal>
  </div>
</template>

<script type=text/javascript>
// Importing
import axios from 'axios'
import Modal from '@/components/modal'
import { mapGetters, mapActions } from 'vuex'

// Generate Javascript functions
export default {
  components: {
    Modal
  },
  data() {
    return {
      isModalVisible: false,
      Alert: {
        message: '',
        showMessage: false,
        dismissable: false
      },
      BookModal: {
        title: '',
        author: '',
        read: []
      }
    }
  },
  computed: {
    ...mapGetters({
      books: 'bookList'
    })
  },
  created() {
    this.$store.dispatch('loadBooks')
  },
  methods: {
    ...mapActions({
      loadBooks: 'books/loadBooks'
    }),
    showModal() {
      this.isModalVisible = true
    },
    closeModal() {
      this.initForm()
      this.isModalVisible = false
    },
    addBook(payload) {
      const path = 'http://localhost:5000/books'
      axios
        .post(path, payload)
        .then(() => {
          this.books.push(payload)
          console.log('added', payload)
        })
        .catch(error => {
          console.log(error)
        })
    },
    initForm() {
      this.BookModal.title = ''
      this.BookModal.author = ''
      this.BookModal.read = []
    },
    onReset() {
      this.initForm()
    },
    onSubmit() {
      let read = false
      if (this.BookModal.read[0]) read = true
      const payload = {
        title: this.BookModal.title,
        author: this.BookModal.author,
        read
      }
      this.addBook(payload)
      this.initForm()
      this.closeModal()
    },
    editBookForm(book) {
      this.BookModal.title = book.title
      this.BookModal.author = book.author
      this.BookModal.read = book.read
      this.showModal()
    }
  }
}
</script>
