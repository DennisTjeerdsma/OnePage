<template class="w-full">
    <div class="container w-screen flex flex-wrap mx-auto" id="Books">
        <div class="row w-full">
            <div class="col-sm-10 w-full">
                <h1>Books</h1>
                <hr><br><br>
                <table class="text-left w-full">
                  <div class="bg-green-lightest border border-green-light text-green-dark \
                  px-4 py-3 rounded relative" role="alert" id="alert" v-if="Alert.showMessage">
                    <div class="font-bold w-full">
                      <alert :message="Alert.message"></alert>
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
                                rounded text-white shadow-md py-2 px-4" @click="showModal"
                                >Update</button>
                                <button type="button" class="bg-red hover:bg-red-darker text-white \
                                rounded py-2 px-4">Delete</button>
                            </td>
                        </tr>
                        <tr class="w-full">
                            <td class="p-4 w-1/4"><button type="button"
                             class="bg-green-light hover:bg-green-dark rounded \
                            text-white px-4 py-2" ref="add" @click="showModal">Add</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <book-modal v-show="isModalVisible" @close='closeModal' @getbooks='getBooks'/>
    </div>
</template>

<script type=text/javascript>

// Importing
import axios from 'axios';
import BookModal from '@/components/BookModal';

// Generate Javascript functions
export default {
  components: {
    BookModal,
  },
  data() {
    return {
      books: [],
      isModalVisible: false,
      Alert: {
        message: '',
        showMessage: false,
        dismissable: false,
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
    showModal() {
      this.isModalVisible = true;
    },
    closeModal() {
      this.getBooks();
      this.isModalVisible = false;
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
