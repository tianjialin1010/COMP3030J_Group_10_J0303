<template>
  <div class="flex flex-col col-span-full xl:col-span-4 bg-gradient-to-b from-slate-700 to-slate-800 dark:bg-none dark:bg-slate-800 shadow-lg rounded-sm border border-slate-700">
    <header class="px-5 py-4 border-b border-slate-600 dark:border-slate-700 flex items-center">
      <h2 class="font-semibold text-slate-200">Your Vehicles</h2>
    </header>
    <div class="h-full flex flex-col px-5 py-6">
      <!-- CC container -->
      <div class="relative w-full max-w-sm mx-auto bg-white-800 dark:bg-slate-900 p-3 rounded-2xl">
        <!-- Car Image -->
        <img :src="carImage" class="inline-flex rounded-full" alt="Car" />
        <!-- Options button -->
        <EditMenu align="right" class="absolute top-0 right-0 inline-flex">
          <li>
            <button class="font-medium text-sm text-slate-600 dark:text-slate-300 hover:text-slate-800 dark:hover:text-slate-200 flex py-1 px-3" @click="selectCar('Truck')">Truck</button>
          </li>
          <li>
            <button class="font-medium text-sm text-slate-600 dark:text-slate-300 hover:text-slate-800 dark:hover:text-slate-200 flex py-1 px-3" @click="selectCar('Van')">Van</button>
          </li>
          <li>
            <button class="font-medium text-sm text-slate-600 dark:text-slate-300 hover:text-slate-800 dark:hover:text-slate-200 flex py-1 px-3" @click="selectCar('Electric')">Electric</button>
          </li>
        </EditMenu>
      </div>
      <!-- Details -->
      <div class="grow flex flex-col justify-center mt-3">
        <div class="text-xs text-slate-500 font-semibold uppercase mb-3">Details</div>
        <div class="space-y-2">
          <div>
            <div class="flex justify-between text-sm mb-2">
              <!-- 燃油效率：越高越好单位mpg -->
              <div class="text-slate-300">Engine Condition</div>
              <div class="text-slate-400 italic">{{ engineCondition }}</div>
            </div>
            <div class="relative w-full h-2 bg-slate-600">
              <div class="absolute inset-0 bg-emerald-500" aria-hidden="true" :style="{ width: engineConditionWidth + '%' }"></div>
            </div>
          </div>
          <div>
            <div class="flex justify-between text-sm mb-2">
              <!-- 空气滤清器单位% -->
              <div class="text-slate-300">Usage Condition</div>
              <div class="text-slate-400 italic">{{ airFilterCondition }}% / 100%</div>
            </div>
            <div class="relative w-full h-2 bg-slate-600">
              <div class="absolute inset-0 bg-yellow-400" aria-hidden="true" :style="{ width: airFilterCondition + '%' }"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import EditMenu from '../../components/DropdownEditMenuCard.vue'
import axios from 'axios'

export default {
  name: 'FintechCard02',
  components: {
    EditMenu,
  },
  data() {
    return {
      selectedCar: 'Truck',
      carImages: {
        Truck: '/api/car_images/Truck.jpg',
        Van: '/api/car_images/Van.jpg',
        Electric: '/api/car_images/Electric.jpg',
      },
      engineConditions: {
        Truck: '30mpg / 40mpg',
        Van: '25mpg / 35mpg',
        Electric: '100mpg / 100mpg',
      },
      airFilterConditions: {
        Truck: 75,
        Van: 65,
        Electric: 90,
      },
    };
  },
  computed: {
    carImage() {
      return this.carImages[this.selectedCar];
    },
    engineCondition() {
      return this.engineConditions[this.selectedCar];
    },
    engineConditionWidth() {
      return this.selectedCar === 'Truck' ? 75 : this.selectedCar === 'Van' ? 65 : 100;
    },
    airFilterCondition() {
      return this.airFilterConditions[this.selectedCar];
    },
  },
  methods: {
    selectCar(car) {
      this.selectedCar = car;
    },
  },
}
</script>
