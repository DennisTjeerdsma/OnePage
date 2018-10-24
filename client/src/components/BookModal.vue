<template>
<div class="container">
  <div id="BookModal" @click.self='close'
  class="fixed pin z-50 overflow-auto bg-smoke-light flex">
    <div class="relative p-8 bg-white w-full max-w-md m-auto flex-col flex rounded">
      <form class="mb-4">
        <header class="modal-header">
         <h1 class="text-decoration: underline">Add Books</h1><hr><br>
        </header>
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
        <div>
          <label for="read">Read</label>
          <input type="checkbox" class="mr-2 leading-tight" v-model="BookModal.read"
          id="read" name="read" value="true">
          <br><hr><br>
          <button class="bg-green hover:bg-green-darker rounded text-white \
          shadow-md py-2 px-4 w-1/3" @click.prevent="onSubmit">Add</button>
          <button class="bg-red hover:bg-red-darker rounded text-white shadow-md py-2 \
          px-4 w-1/3" type="reset" @click.prevent="onReset">Reset</button>
        </div>
      </form>
    </div>
  </div>
</div>
</template>


<script>

// Javascript functions for modal
export default {
  name: 'BookModal',
  data() {
    return {
      BookModal: {
        title: '',
        author: '',
        read: [],
      },
    };
  },
  methods: {
    close() {
      this.$emit('close');
      },
    onSubmit() {
      let read = false;
      if (this.BookModal.read[0]) read = true;
      const payload = {
        title: this.BookModal.title,
        author: this.BookModal.author,
        read,
      };
      this.$emit('added', payload);
      this.initForm();
      this.close();
    },
    initForm() {
      this.BookModal.title = '';
      this.BookModal.author = '';
      this.BookModal.read = [];
    },
    onReset() {
      this.initForm();
      this.close();
    },
  },
};
</script>
