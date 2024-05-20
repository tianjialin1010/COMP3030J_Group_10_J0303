<!--WarehouseEndOrderModel.vue-->
<template>
  <div class="p-6">
    <h1 class="text-xl font-bold mb-4"></h1>

    <ModalBasic :modalOpen="modalOpen" @close-modal="modalOpen = false">
      <!-- Google Map Component -->
      <Road @map-loaded="handleMapLoaded" />
      <!-- Modal Content -->
      <div class="px-5 py-4">
        <div class="text-sm">
          <div class="font-medium text-slate-800 dark:text-slate-100 mb-3">Accept Order</div>
          <div class="space-y-3">
            <!-- 订单ID -->
            <div>
              <p class="block text-sm font-medium mb-1">Order ID: {{ order.order_id }}</p>
            </div>

            <!-- 车辆ID -->
            <div>
              <label class="block text-sm font-medium mb-1" for="Vehicle_ID">Vehicle ID <span class="text-rose-500">*</span></label>
              <select id="Vehicle_ID" class="form-select w-full px-2 py-1" v-model="Vehicle_ID" required>
                <option v-for="vehicle in vehicles" :key="vehicle.license_plate" :value="vehicle.license_plate">
                  {{ vehicle.license_plate }}
                </option>
              </select>
            </div>

            <!-- 替换 <video> 标签为 Plate 组件 -->
            <Plate />
          </div>
        </div>
        <!-- Modal Footer -->
        <div class="px-5 py-4 border-t border-slate-200 dark:border-slate-700">
          <div class="flex flex-wrap justify-end space-x-2">
            <button class="btn-sm border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600 text-slate-600 dark:text-slate-300" @click="modalOpen = false; $emit('close-modal')">Cancel</button>
            <button class="btn-sm bg-indigo-500 hover:bg-indigo-600 text-white" @click="sendDataToBackend">Accept</button>
          </div>
        </div>
      </div>
    </ModalBasic>
  </div>
</template>

<script>
import ModalBasic from '../../components/ModalBasic.vue'; // 调整路径以适合您的项目结构
import axios from 'axios'; // 导入Axios以进行HTTP请求
import Road from '../../pages/Road.vue'; // 调整路径以适合您的项目结构
import Plate from '../../pages/Plate.vue'; // 调整路径以适合您的项目结构

export default {
  name: 'DriverAddOrderModal',
  components: {
    Road,
    ModalBasic,
    Plate, // 引入 Plate 组件
  },
  props: {
    order: Object
  },
  data() {
    return {
      modalOpen: true,
      Vehicle_ID: '',
      vehicles: [],
    };
  },
  mounted() {
    this.fetchVehicles();
  },
  methods: {
    async fetchVehicles() {
      try {
        const response = await axios.get('/api/vehicles');
        this.vehicles = response.data;
      } catch (error) {
        console.error('Error fetching vehicles:', error);
      }
    },
    async sendDataToBackend() {
      try {
        const response = await axios.post('/update_order', {
          order_id: this.order.order_id,
          vehicle_id: this.Vehicle_ID,
        });
        console.log(response.data); // 如果需要的话，你可以处理后端返回的响应
        this.modalOpen = false; // 关闭模态框
      } catch (error) {
        console.error('Error sending data to backend:', error);
      }
    },
    handleMapLoaded() {
      console.log('Map loaded');
      // 如果需要在地图加载后执行某些操作，可以在这里处理
    }
  }
}
</script>
