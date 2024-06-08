<template>
  <div>
    <input type="file" @change="onFileChange" />
    <button @click="recognizePlate" :disabled="!selectedFile && !selectedImage">Recognize now!</button>
    <div v-if="imageSrc" class="image-preview">
      <img :src="imageSrc" alt="Selected image preview">
    </div>
    <div v-if="plateNumber" class="results">
      The plate number is: <strong>{{ plateNumber }}</strong>
    </div>
    <div v-if="error" class="error">{{ error }}</div>
    <div v-if="loading" class="loading">Loading...</div>
    <select v-model="selectedImage" @change="onImageSelect">
      <option value="">Select an image</option>
      <option v-for="image in images" :key="image" :value="image">{{ image }}</option>
    </select>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedFile: null,
      selectedImage: null,
      plateNumber: null,
      imageSrc: null,
      images: [],
      error: null,
      loading: false
    };
  },
  created() {
    this.fetchImages();
  },
  methods: {
    async fetchImages() {
      try {
        const response = await axios.get('http://localhost:5000/api/images');
        this.images = response.data;
      } catch (error) {
        this.error = `Failed to fetch images: ${error.response?.data?.error || error.message}`;
      }
    },
    onFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.selectedFile = file;
        this.selectedImage = null;  // 清空选择的图片路径
        const reader = new FileReader();
        reader.onload = (e) => {
          this.imageSrc = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    },
    onImageSelect() {
      this.selectedFile = null;  // 清空上传的文件
      this.imageSrc = `http://localhost:5000/api/images/${this.selectedImage}`;
    },
    async recognizePlate() {
      this.loading = true;
      const formData = new FormData();

      if (this.selectedFile) {
        formData.append('image', this.selectedFile);
      } else if (this.selectedImage) {
        formData.append('image_name', this.selectedImage);
      }

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
.loading {
  color: blue;
}
</style>
