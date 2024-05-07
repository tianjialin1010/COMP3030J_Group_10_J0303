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
            <h1>车牌识别系统</h1>
            <select v-model="selectedFile" @change="loadImage">
              <option disabled value="">请选择一张图片</option>
              <option v-for="file in files" :key="file">{{ file }}</option>
            </select>
            <button @click="recognizePlate" :disabled="!selectedFile">识别车牌</button>
            <div v-if="imageSrc" class="image-preview">
              <img :src="imageSrc" alt="Selected image preview">
            </div>
            <div v-if="plateNumber" class="results">
              识别结果: <strong>{{ plateNumber }}</strong>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<!--<script>-->
<!--import axios from 'axios';-->

<!--export default {-->
<!--  data() {-->
<!--    return {-->
<!--      files: [],-->
<!--      selectedFile: '',-->
<!--      plateNumber: null,-->
<!--      imageSrc: null,-->
<!--      loading: false,-->
<!--      error: null-->
<!--    };-->
<!--  },-->
<!--  created() {-->
<!--    this.fetchFiles();-->
<!--  },-->
<!--  methods: {-->
<!--    fetchFiles() {-->
<!--      this.loading = true;-->
<!--      axios.get('/images')-->
<!--        .then(response => {-->
<!--          this.files = response.data;-->
<!--          this.loading = false;-->
<!--        })-->
<!--        .catch(error => {-->
<!--          this.error = '无法加载图片列表';-->
<!--          this.loading = false;-->
<!--        });-->
<!--    },-->
<!--    loadImage() {-->
<!--      if (this.selectedFile) {-->
<!--        this.imageSrc = `/path_to_images/${this.selectedFile}`;-->
<!--      }-->
<!--      console.log(this.imageSrc);  // 输出检查路径是否正确-->
<!--    },-->
<!--    recognizePlate() {-->
<!--      this.loading = true;-->
<!--      axios.post('/recognize', { image_name: this.selectedFile })-->
<!--        .then(response => {-->
<!--          this.plateNumber = response.data.plate_number;-->
<!--          this.loading = false;-->
<!--        })-->
<!--        .catch(error => {-->
<!--          this.error = '识别失败';-->
<!--          this.loading = false;-->
<!--        });-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</script>-->
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
      files: [],
      selectedFile: '',
      plateNumber: null,
      imageSrc: null,
      loading: false,
      error: null
    };
  },
  created() {
    this.fetchFiles();
  },
  methods: {
    fetchFiles() {
      this.loading = true;
      axios.get('/images')
        .then(response => {
          this.files = response.data;
          this.loading = false;
        })
        .catch(error => {
          this.error = '无法加载图片列表';
          this.loading = false;
        });
    },
    loadImage() {
      if (this.selectedFile) {
        this.imageSrc = `/path_to_images/${this.selectedFile}`;
      }
    },
    recognizePlate() {
      this.loading = true;
      axios.post('/recognize', { image_name: this.selectedFile })
        .then(response => {
          this.plateNumber = response.data.plate_number;
          this.loading = false;
        })
        .catch(error => {
          this.error = '识别失败';
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