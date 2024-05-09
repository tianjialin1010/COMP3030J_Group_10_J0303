<template>
  <div class="p-6">
    <h1 class="text-xl font-bold mb-4"></h1>

    <ModalBasic :modalOpen="modalOpen" @close-modal="modalOpen = false">
      <!-- Modal Content -->
      <div class="px-5 py-4">
        <div class="text-sm">
          <div class="font-medium text-slate-800 dark:text-slate-100 mb-3">Let Driver know what you need 🙌</div>
          <div class="space-y-3">
            <!-- 仓库员只发布订单信息其他信息由驾驶员认领后补全 -->
            <!-- 仓库员id -->
            <div>
              <label class="block text-sm font-medium mb-1" for="IU_ID">IU_ID <span class="text-rose-500">*</span></label>
              <input id="IU_ID" class="form-input w-full px-2 py-1" type="text" v-model="IU_ID" required/>
            </div>
            <!-- 所需车辆大小 -->
            <div>
              <label class="block text-sm font-medium mb-1" for="vehicleType">Vehicle Type <span
                  class="text-rose-500">*</span></label>
              <select id="vehicleType" class="form-select w-full px-2 py-1" v-model="selected_vehicle_type" required>
                <option value="small">Small</option>
                <option value="mid">Mid</option>
                <option value="large">Large</option>
              </select>
            </div>
            <!-- 目的地 -->
            <div>
              <label class="block text-sm font-medium mb-1" for="destination">Destination <span
                  class="text-rose-500">*</span></label>
              <select id="destination" class="form-select w-full px-2 py-1" v-model="selected_destination" required>
                <option value="shanghai">Shanghai</option>
                <option value="beijing">Beijing</option>
                <option value="shandong">Shandong</option>
              </select>
            </div>
            <!-- 起始点 -->
            <div>
              <label class="block text-sm font-medium mb-1" for="startLocation">Start Location <span
                  class="text-rose-500">*</span></label>
              <select id="startLocation" class="form-select w-full px-2 py-1" v-model="selected_start_location" required>
                <option value="beijing">Beijing</option>
                <option value="shanghai">Shanghai</option>
                <option value="shandong">Shandong</option>
              </select>
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
import axios from 'axios'; // 导入Axios以进行HTTP请求

export default {
  name: 'AddOrderModal',
  components: {
    ModalBasic,
  },
  data() {
    return {
      modalOpen: true,
      IU_ID: '',
      selected_vehicle_type: '',
      selected_destination: '',
      selected_start_location: '',
    };
  },
  methods: {
    sendDataToBackend() {
      const formData = {
        IU_ID: this.IU_ID,
        vehicle_type: this.selected_vehicle_type,
        destination: this.selected_destination,
        start_location: this.selected_start_location,
      };

      axios.post('/api/addOrder', formData)
        .then(response => {
          console.log('Data saved successfully:', response.data);
          this.modalOpen = false;
        })
        .catch(error => {
          console.error('Error saving data:', error);
        });
    }
  }
}
</script>
