<!-- WarehouseEndOrderModal.vue -->
<template>
  <div class="p-6">
    <h1 class="text-xl font-bold mb-4">End Orders by License Plate</h1>

    <ModalBasic :modalOpen="modalOpen" @close-modal="closeModal">
      <div class="px-5 py-4">
        <div class="text-sm">
          <div class="font-medium text-slate-800 dark:text-slate-100 mb-3">End Orders</div>
          <div class="space-y-3">
            <!-- 车辆ID -->
            <div>
              <label class="block text-sm font-medium mb-1" for="Vehicle_ID">Vehicle ID <span class="text-rose-500">*</span></label>
              <input type="text" id="Vehicle_ID" class="form-input w-full px-2 py-1" v-model="Vehicle_ID" required list="vehicle-list"/>
              <datalist id="vehicle-list">
                <option v-for="vehicle in vehicles" :key="vehicle.license_plate" :value="vehicle.license_plate">
                  {{ vehicle.license_plate }}
                </option>
              </datalist>
            </div>

            <!-- 车型选择 -->
            <div>
              <label class="block text-sm font-medium mb-1" for="vehicleType">Vehicle Type <span class="text-rose-500">*</span></label>
              <select id="vehicleType" class="form-select w-full px-2 py-1" v-model="selectedModel" required>
                <option value="">--Please choose an option--</option>
                <option value="Truck.glb">Truck</option>
                <option value="Van.glb">Van</option>
                <option value="Electric.glb">Electric</option>
              </select>
            </div>

            <!-- 车牌识别组件 -->
            <div v-if="selectedModel">
              <Plate :src="selectedModelSrc" />
            </div>
          </div>
        </div>
        <!-- Modal Footer -->
        <div class="px-5 py-4 border-t border-slate-200 dark:border-slate-700">
          <div class="flex flex-wrap justify-end space-x-2">
            <button class="btn-sm border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600 text-slate-600 dark:text-slate-300" @click="closeModal">Cancel</button>
            <button class="btn-sm bg-indigo-500 hover:bg-indigo-600 text-white" @click="sendDataToBackend">End Orders</button>
          </div>
        </div>
      </div>
    </ModalBasic>
  </div>
</template>

<script>
import ModalBasic from '../../components/ModalBasic.vue';
import axios from 'axios';
import Plate from '../../pages/Plate.vue';

export default {
  name: 'WarehouseEndOrderModal',
  components: {
    ModalBasic,
    Plate,
  },
  props: {},
  data() {
    return {
      modalOpen: true,
      Vehicle_ID: '',
      vehicles: [],
      selectedModel: null
    };
  },
  computed: {
    selectedModelSrc() {
      if (this.selectedModel) {
        return `/api/models/${this.selectedModel}`;
      }
      return null;
    }
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
      // 添加调试信息
      console.log('Vehicle_ID:', this.Vehicle_ID);

      if (!this.Vehicle_ID) {
        console.error('Missing Vehicle_ID');
        alert('Please fill all required fields');
        return;
      }

      try {
        const response = await axios.post('/api/end_order', {
          license_plate: this.Vehicle_ID,
        });
        console.log(response.data);
        this.modalOpen = false;
        this.$emit('close-modal');
        alert(`Orders ended successfully: ${response.data.message}`);
      } catch (error) {
        console.error('Error sending data to backend:', error);
        alert(`Failed to end orders: ${error.response?.data?.error || error.message}`);
      }
    },
    closeModal() {
      this.modalOpen = false;
      this.$emit('close-modal');
    },
  }
}
</script>

<style scoped>
.glb-models {
  width: 100%;
  height: 500px; /* 根据需要调整尺寸 */
}
</style>
