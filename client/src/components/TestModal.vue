<template>
  <div class="modal-backdrop fixed pin z-50 overflow-auto bg-smoke-light flex">
    <div class="modal relative p-8 bg-white w-full max-w-md m-auto flex-col flex rounded">
      <header class="modal-header">
        <slot name="header">
            This is a default title!
            <button type="button" class="btn-close" @click="close">x</button>
        </slot>
      </header>

      <section class="modal-body">
        <slot name="body">
          Default body enzo.
        </slot>
      </section>

      <footer class="modal-footer">
        <slot name="footer">
          Een footer
          <button type="button" class="btn-green" @click="close">Close me!</button>
        </slot>
      </footer>
    </div>
  </div>
</template>

<script>

export default {
  name: 'TestModal',
  methods: {
    close() {
      this.$emit('close');
    },
  },
};
</script>

