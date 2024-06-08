<template>
  <div class="flex flex-col col-span-full sm:col-span-6 xl:col-span-4 bg-white dark:bg-slate-800 shadow-lg rounded-sm border border-slate-200 dark:border-slate-700">
    <div class="px-5 pt-5">
      <header class="flex justify-between items-start mb-2">
        <img src="../../images/icon-01.svg" width="32" height="32" alt="Icon 01" />
        <div class="px-5 pb-5">
          <button @click="openModal" align="right" class="btn-primary relative inline-flex">View the model!</button>
        </div>
      </header>
      <h2 class="text-lg font-semibold text-slate-800 dark:text-slate-100 mb-2">Van vehicle </h2>
      <div class="text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase mb-1">Group 10 model authority(try dragging the model!)</div>
    </div>
<!--    <div class="grow">-->
<!--      <ModelViewer modelUrl="http://localhost:5000/backend/3d/Electric.glb" />-->
<!--    </div>-->
  </div>
  <transition name="modal">
    <div v-if="isModalOpen" class="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg p-4 w-full max-w-4xl">
        <button @click="closeModal" class="btn-secondary mb-4">Close</button>
        <div class="w-full h-96">
          <ModelViewer :fullscreen="true" modelUrl="http://localhost:5000/backend/3d/Electric.glb" />
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { ref } from 'vue'
import ModelViewer from '../../components/ModelViewer.vue'

export default {
  name: 'DashboardCard01',
  components: {
    ModelViewer,
  },
  setup() {
    const isModalOpen = ref(false)

    const openModal = () => {
      isModalOpen.value = true
    }

    const closeModal = () => {
      isModalOpen.value = false
    }

    return {
      isModalOpen,
      openModal,
      closeModal
    }
  }
}
</script>
<style scoped>
.btn-primary {
  background-color: #1d4ed8; /* Blue background */
  color: white; /* White text */
  padding: 10px 20px; /* Padding */
  border: none; /* No border */
  border-radius: 5px; /* Rounded corners */
  cursor: pointer; /* Pointer cursor on hover */
  text-align: center; /* Centered text */
  display: inline-flex; /* Inline flex for alignment */
  justify-content: center; /* Center content */
  align-items: center; /* Center content */
  font-size: 16px; /* Font size */
  transition: background-color 0.3s ease; /* Smooth transition for background color */
}

.btn-primary:hover {
  background-color: #2563eb; /* Darker blue on hover */
}

.btn-primary:active {
  background-color: #1e40af; /* Even darker blue on click */
}

.btn-secondary {
  background-color: #e5e7eb; /* Light gray background */
  color: black; /* Black text */
  padding: 10px 20px; /* Padding */
  border: none; /* No border */
  border-radius: 5px; /* Rounded corners */
  cursor: pointer; /* Pointer cursor on hover */
  text-align: center; /* Centered text */
  display: inline-flex; /* Inline flex for alignment */
  justify-content: center; /* Center content */
  align-items: center; /* Center content */
  font-size: 16px; /* Font size */
  transition: background-color 0.3s ease; /* Smooth transition for background color */
}

.btn-secondary:hover {
  background-color: #d1d5db; /* Darker gray on hover */
}

.btn-secondary:active {
  background-color: #9ca3af; /* Even darker gray on click */
}
</style>