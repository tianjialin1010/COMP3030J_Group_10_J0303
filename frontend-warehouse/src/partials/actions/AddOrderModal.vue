<template>
  <div class="p-6">
    <h1 class="text-xl font-bold mb-4"></h1>

    <ModalBasic :modalOpen="modalOpen" @close-modal="modalOpen = false">
      <!-- Modal Content -->
      <div class="px-5 py-4">
        <div class="text-sm">
          <div class="font-medium text-slate-800 dark:text-slate-100 mb-3">Let Driver know what you need 🙌</div>
          <div class="space-y-3">
            <!-- 起始地 -->
            <div>
              <label class="block text-sm font-medium mb-1" for="startLocation">Start Location <span class="text-rose-500">*</span></label>
              <select id="startLocation" class="form-select w-full px-2 py-1" v-model="selected_start_location" @change="updateDistanceAndTime" required>
                <option value="Dublin">Dublin, Ireland</option>
                <option value="Cork">Cork, Ireland</option>
                <option value="Galway">Galway, Ireland</option>
                <option value="Limerick">Limerick, Ireland</option>
              </select>
            </div>
            <!-- 目的地 -->
            <div>
              <label class="block text-sm font-medium mb-1" for="destination">Destination <span class="text-rose-500">*</span></label>
              <select id="destination" class="form-select w-full px-2 py-1" v-model="selected_destination" @change="updateDistanceAndTime" required>
                <option value="Dublin">Dublin, Ireland</option>
                <option value="Cork">Cork, Ireland</option>
                <option value="Galway">Galway, Ireland</option>
                <option value="Limerick">Limerick, Ireland</option>
              </select>
            </div>
            <!-- 距离值 -->
            <div>
              <label class="block text-sm font-medium mb-1" for="distanceValue">Distance (km)</label>
              <input id="distanceValue" class="form-input w-full px-2 py-1" type="text" v-model="distanceValue" readonly />
            </div>
            <!-- 时间值 -->
            <div>
              <label class="block text-sm font-medium mb-1" for="durationValue">Estimated Time</label>
              <input id="durationValue" class="form-input w-full px-2 py-1" type="text" :value="formattedDuration" readonly />
            </div>
          </div>
        </div>
        <!-- Modal Footer -->
        <div class="px-5 py-4 border-t border-slate-200 dark:border-slate-700">
          <div class="flex flex-wrap justify-end space-x-2">
            <button class="btn-sm border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600 text-slate-600 dark:text-slate-300" @click="modalOpen = false; $emit('close-modal')">Cancel</button>
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
  props: {
    fetchOrders: {
      type: Function,
      required: true
    }
  },
  data() {
    return {
      modalOpen: true,
      selected_destination: '',
      selected_start_location: '',
      distanceValue: '',  // 存储距离值
      durationValue: '',  // 存储时间值
    };
  },
  computed: {
    formattedDuration() {
      if (!this.durationValue || this.durationValue === 'N/A') {
        return 'N/A';
      }
      const totalSeconds = parseInt(this.durationValue, 10);
      const hours = Math.floor(totalSeconds / 3600);
      const minutes = Math.floor((totalSeconds % 3600) / 60);
      const seconds = totalSeconds % 60;
      return `${hours} hours, ${minutes} minutes, ${seconds} seconds`;
    }
  },
  methods: {
    updateDistanceAndTime() {
      const key = `${this.selected_start_location}-${this.selected_destination}`;
      const routes = {
        'Dublin-Galway': { distance: 207, duration: 8465 },
        'Galway-Dublin': { distance: 207, duration: 8465 },
        'Dublin-Cork': { distance: 260, duration: 10331 },
        'Cork-Dublin': { distance: 260, duration: 10331 },
        'Dublin-Limerick': { distance: 203, duration: 8353 },
        'Limerick-Dublin': { distance: 203, duration: 8353 },
        'Cork-Galway': { distance: 205, duration: 9121 },
        'Galway-Cork': { distance: 205, duration: 9121 },
        'Cork-Limerick': { distance: 99, duration: 5461 },
        'Limerick-Cork': { distance: 99, duration: 5461 },
        'Galway-Limerick': { distance: 108, duration: 9121 },
        'Limerick-Galway': { distance: 108, duration: 9121 }
      };
      if (routes[key]) {
        this.distanceValue = routes[key].distance;
        this.durationValue = routes[key].duration;
      } else {
        this.distanceValue = 'N/A';
        this.durationValue = 'N/A';
      }
    },
    sendDataToBackend() {
      if (this.selected_start_location === this.selected_destination) {
        alert("Start location and destination cannot be the same.");
        return;
      }

      const formData = {
        origin: this.selected_start_location,
        destination: this.selected_destination,
        mileage: this.distanceValue,
        estimate_time: this.durationValue,
      };
      console.log('Sending data:', formData);  // 添加这行来检查发送的数据

      axios.post('/api/addOrder', formData)
        .then(response => {
          console.log('Data saved successfully:', response.data);
          this.modalOpen = false;
          this.$emit('close-modal');
          this.fetchOrders();  // 刷新订单列表
        })
        .catch(error => {
          console.error('Error saving data:', error);
        });
    }
  }
}
</script>
