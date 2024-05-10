<template>
  <div class="p-6">
    <h1 class="text-xl font-bold mb-4"></h1>

    <ModalBasic :modalOpen="modalOpen" @close-modal="modalOpen = false">
      <!-- Modal Content -->
      <div class="px-5 py-4">
        <div class="text-sm">

          <div class="font-medium text-slate-800 dark:text-slate-100 mb-3">Let Driver know what you need 🙌</div>
          <!-- Google Map Component -->
          <Road @map-loaded="handleMapLoaded" />
          <div class="space-y-3">
            <!--  ID    -->
            <div>
              <label class="block text-sm font-medium mb-1" for="ID">Order_ID <span class="text-rose-500">*</span></label>
              <input id="ID" class="form-input w-full px-2 py-1" type="text" v-model="ID" required/>
            </div>

            <!-- ad id -->
            <div>
              <label class="block text-sm font-medium mb-1" for="AD_ID">AD_ID <span class="text-rose-500">*</span></label>
              <input id="AD_ID" class="form-input w-full px-2 py-1" type="text" v-model="AD_ID" required/>
            </div>
            <!-- 驾驶员id -->
            <div>
              <label class="block text-sm font-medium mb-1" for="Driver_ID">Driver_ID <span
                  class="text-rose-500">*</span></label>
              <input id="Driver_ID" class="form-select w-full px-2 py-1" v-model="Driver_ID" required>
            </div>
            <!-- 车辆id -->
            <div>
              <label class="block text-sm font-medium mb-1" for="destination">Vehicle_ID <span
                  class="text-rose-500">*</span></label>
              <input id="Vehicle_ID" class="form-select w-full px-2 py-1" v-model="Vehicle_ID" required>
            </div>

          </div>
        </div>
        <!-- Modal Footer -->
        <div class="px-5 py-4 border-t border-slate-200 dark:border-slate-700">
          <div class="flex flex-wrap justify-end space-x-2">
            <button class="btn-sm border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600 text-slate-600 dark:text-slate-300"
                    @click="modalOpen = false; $emit('close-modal')">Cancel</button>
            <button class="btn-sm bg-indigo-500 hover:bg-indigo-600 text-white" @click="sendDataToBackend">Send</button>
          </div>
        </div>
      </div>
    </ModalBasic>
  </div>
</template>

<script>
import ModalBasic from '../../components/ModalBasic.vue'; // 调整路径以适合您的项目结构
import axios from 'axios';// 导入Axios以进行HTTP请求
import Road from '../../pages/Road.vue'; // 调整路径以适合您的项目结构

function handleMapLoaded() {

}

export default {
  name: 'DriverAddOrderModal',
  components: {
    Road,
    ModalBasic,
  },
  data() {
    return {
      modalOpen: true,
      ID:"",
      AD_ID: '',
      Driver_ID: '',
      Vehicle_ID: '',

    };
  },
  methods: {
    sendDataToBackend: async function () {
      try {
        const response = await axios.post('/update_order', {
          ID: this.ID,
          AD_ID: this.AD_ID,
          Driver_ID: this.Driver_ID,
          Vehicle_ID: this.Vehicle_ID
        });
        console.log(response.data); // 如果需要的话，你可以处理后端返回的响应
        this.modalOpen = false; // 关闭模态框
      } catch (error) {
        console.error('Error sending data to backend:', error);
      }
      handleMapLoaded()
      {
        console.log('Map loaded');
        // 如果需要在地图加载后执行某些操作，可以在这里处理
      }
    }
  }
}
</script>
