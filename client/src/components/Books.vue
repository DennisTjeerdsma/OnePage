<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-10">
                <h1>Books</h1>
                <hr><br><br>
                <table class="text-left w-full">
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
                <form class="mb-4" @reset="onReset">
                    <h1 class="text-decoration: underline">Add Books</h1><hr><br>
                    <div>
                        <label for="title">Title</label><br>
                        <input type="text" name="title" id="title" class="border rounded"
                         placeholder="Add book title here" required>
                    </div><br>
                    <div>
                        <label for="author">Author</label><br>
                        <input type="text" name="author" id="author" class="border rounded"
                        placeholder="Add author here" required>
                    </div><br>
                        <label for="read">Read</label>
                        <input type="checkbox" class="mr-2 leading-tight"><br><hr><br>
                    <div>
                    </div>
                    <button class="bg-green hover:bg-green-darker rounded text-white \
                     shadow-md py-2 px-4 w-1/3">Add</button>
                    <button class="bg-red hover:bg-red-darker rounded text-white shadow-md py-2 \
                    px-4 w-1/3" type="reset">Reset</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script type=text/javascript>
import axios from 'axios';

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
  },
  created() {
    this.getBooks();
  },
};
</script>
