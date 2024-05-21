<template>
  <div>
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
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedFile: null,
      plateNumber: null,
      imageSrc: null,
      error: null,
      loading: false
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
    async recognizePlate() {
      this.loading = true;
      const formData = new FormData();
      formData.append('image', this.selectedFile);

      try {
        const response = await axios.post('http://localhost:5000/api/recognize', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        this.plateNumber = response.data.plate_number;
      } catch (error) {
        this.error = `Recognition failed: ${error.response?.data?.error || error.message}`;
      } finally {
        this.loading = false;
      }
    }
  }
}
</script>

<style>
.image-preview img {
  width: 100%;
  max-width: 500px;
  height: auto;
}
.results {
  margin-top: 20px;
}
.error {
  color: red;
}
</style>
