<template>
  <div class="container">
    <div
      id="modal"
      class="fixed pin z-50 overflow-auto bg-smoke-light flex"
      name="modal"
      role="modal"
      @click.self="close"
    >
      <div class="relative p-8 bg-white w-full max-w-md m-auto flex-col flex rounded">
        <form class="mb-4">
          <slot name="title"/>
          <slot name="body"/>
          <slot name="footer"/>
          <slot name="buttons"/>
        </form>
      </div>
    </div>
  </div>
</template>


<script>
// Javascript functions for modal
export default {
  name: 'Modal',
  methods: {
    close() {
      this.$emit('close')
    }
  }
}
</script>
