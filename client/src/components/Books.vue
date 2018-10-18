<template class="w-full">
    <div class="container w-screen flex flex-wrap mx-auto">
        <div class="row w-full">
            <div class="col-sm-10 w-full">
                <h1>Books</h1>
                <hr><br><br>
                <table class="text-left w-full">
                  <div class="bg-green-lightest border border-green-light text-green-dark \
                  px-4 py-3 rounded relative" role="alert" id="alert" v-if="showMessage">
                    <div class="font-bold w-full">
                      <alert :message="message">{{ message }}</alert>
                    </div>
                  </div><br>
                    <thead class="bg-black flex text-white w-full">
                        <tr class="flex w-full mb-4">
                            <th scope="col" class="p-4 w-1/4">Title</th>
                            <th scope="col" class="p-4 w-1/4">Author</th>
                            <th scope="col" class="p-4 w-1/4">Read?</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody class="w-full">
                        <tr v-for="(book, index) in books" :key="index" class="flex w-full mb-4">
                            <td class="p-4 w-1/4">{{ book.title}} </td>
                            <td class="p-4 w-1/4">{{ book.author }}</td>
                            <td class="p-4 w-1/4">
                                <span v-if="book.read">Yes</span>
                                <span v-else>No</span>
                            </td>
                            <td>
                                <button type="button" class="bg-blue hover:bg-blue-darker \
                                rounded text-white shadow-md py-2 px-4">Update</button>
                                <button type="button" class="bg-red hover:bg-red-darker text-white \
                                rounded py-2 px-4">Delete</button>
                            </td>
                        </tr>
                        <tr class="w-full">
                            <td class="p-4 w-1/4"><button type="button"
                             @click="toggleModal"
                             class="bg-green-light hover:bg-green-dark rounded \
                            text-white px-4 py-2">Add</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div v-if="BookModal.visible" id="BookModal" @click.self="toggleModal"
        class="fixed pin z-50 overflow-auto bg-smoke-light flex">
            <div class="relative p-8 bg-white w-full max-w-md m-auto flex-col flex rounded">
                <form class="mb-4" @reset.prevent="onReset" @submit.prevent="onSubmit">
                    <h1 class="text-decoration: underline">Add Books</h1><hr><br>
                    <div>
                        <label for="title">Title</label><br>
                        <input type="text" name="title" id="title" class="border rounded"
                         placeholder="Add book title here" required v-model="BookModal.title">
                    </div><br>
                    <div>
                        <label for="author">Author</label><br>
                        <input type="text" name="author" id="author" class="border rounded"
                        placeholder="Add author here" required v-model="BookModal.author">
                    </div><br>
                        <label for="read">Read</label>
                        <input type="checkbox" class="mr-2 leading-tight" v-model="BookModal.read"
                        ><br><hr><br>
                    <div>
                    </div>
                    <button class="bg-green hover:bg-green-darker rounded text-white \
                     shadow-md py-2 px-4 w-1/3" type='submit'>Add</button>
                    <button class="bg-red hover:bg-red-darker rounded text-white shadow-md py-2 \
                    px-4 w-1/3" type="reset">Reset</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script type=text/javascript>

// Importing
import axios from 'axios';

// Generate Javascript functions
export default {
  data() {
    return {
      books: [],
      BookModal: {
        title: '',
        author: '',
        read: [],
        visible: false,
      },
      message: '',
      showMessage: false,
    };
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    toggleModal() {
      this.BookModal.visible = !this.BookModal.visible;
    },
    initForm() {
      this.BookModal.title = '';
      this.BookModal.author = '';
      this.BookModal.read = [];
    },
    onReset() {
      this.initForm();
    },
    onSubmit() {
      let read = false;
      if (this.BookModal.read[0]) read = true;
      const payload = {
        title: this.BookModal.title,
        author: this.BookModal.author,
        read,
      };
      this.addBook(payload);
      this.initForm();
      this.toggleModal();
    },
    addBook(payload) {
      const path = 'http://localhost:5000/books';
      axios.post(path, payload)
        .then(() => {
          this.message = 'Book added!';
          this.showMessage = true;
          this.getBooks();
        })
        .catch((error) => {
          console.log(error);
          this.getBooks();
        });
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
