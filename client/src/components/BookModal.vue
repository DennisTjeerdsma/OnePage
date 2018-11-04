<template>
<div class="container">
  <div id="modal" @click.self='close'
  class="fixed pin z-50 overflow-auto bg-smoke-light flex" name="modal" role="modal">
    <div class="relative p-8 bg-white w-full max-w-md m-auto flex-col flex rounded">
      <form class="mb-4">
        <slot name="title">
        </slot>
        <slot name="body">
        </slot>
        <slot name="footer">
        </slot>
        <slot name="buttons">
        </slot>
      </form>
    </div>
  </div>
</div>
</template>


<script>

// Javascript functions for modal
export default {
  name: 'modal',
  methods: {
    close() {
      this.$emit('close');
      },
  },
};
</script>
