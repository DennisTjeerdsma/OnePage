<template>
  <div id="dus" class="dus">
    <p>Hi</p>
    <button type="button" class="btn" @click="showModal">Open Modal</button>
    <TestModal v-show="isModalVisible" @close="closeModal"/>
  </div>
</template>

<script>

/* Importing */
import TestModal from '@/components/TestModal';

export default {
  name: 'Dus',
  components: {
    TestModal,
  },
  data() {
    return {
      isModalVisible: false,
    };
  },
  methods: {
    showModal() {
      this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
    },
  },
};
</script>
