<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-10">
                <h1>Books</h1>
                <hr><br><br>
                <button type="button" class="bg-green-light hover:bg-green-dark rounded \
                text-white px-4 py-2">Add</button>
                <br><br>
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
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      books: [],
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
  },
  created() {
    this.getBooks();
  },
};
</script>
