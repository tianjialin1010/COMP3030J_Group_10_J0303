<template>
  <div class="flex h-[100vh] overflow-hidden">
    <!-- Sidebar -->
    <Sidebar :sidebarOpen="sidebarOpen" @close-sidebar="sidebarOpen = false" />

    <!-- Content area -->
    <div class="relative flex flex-col flex-1 overflow-y-auto overflow-x-hidden">
      <!-- Site header -->
      <Header :sidebarOpen="sidebarOpen" @toggle-sidebar="sidebarOpen = !sidebarOpen" />

      <main class="grow">
        <div class="px-4 sm:px-6 lg:px-8 py-8 w-full max-w-9xl mx-auto">
          <div class="app-container">
            <h1>License Plate Recognition</h1>
            <input type="file" @change="onFileChange" />
            <button @click="recognizePlate" :disabled="!selectedFile">Recognize now!</button>
            <div v-if="imageSrc" class="image-preview">
              <img :src="imageSrc" alt="Selected image preview">
            </div>
            <div v-if="plateNumber" class="results">
              The plate number is: <strong>{{ plateNumber }}</strong>
            </div>
            <div v-if="error" class="error">{{ error }}</div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Sidebar from '../partials/Sidebar.vue';
import Header from '../partials/Header.vue';

export default {
  components: {
    Sidebar,
    Header
  },
  data() {
    return {
      sidebarOpen: false,
      selectedFile: null,
      plateNumber: null,
      imageSrc: null,
      loading: false,
      error: null
    };
  },
  methods: {
    onFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.selectedFile = file;
        const reader = new FileReader();
        reader.onload = (e) => {
          this.imageSrc = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    },
    recognizePlate() {
      this.loading = true;
      const formData = new FormData();
      formData.append('image', this.selectedFile);

      axios.post('/api/recognize', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(response => {
        this.plateNumber = response.data.plate_number;
        this.loading = false;
      })
      .catch(error => {
        this.error = 'Recognition failed';
        this.loading = false;
      });
    }
  }
}
</script>

<style>
.app-container {
  text-align: center;
  padding: 20px;
}
.loading, .error {
  color: red;
}
.image-preview img {
  width: 100%;
  max-width: 500px;
  height: auto;
}
.results {
  margin-top: 20px;
}
</style>
