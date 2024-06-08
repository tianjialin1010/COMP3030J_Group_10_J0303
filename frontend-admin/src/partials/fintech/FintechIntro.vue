<template>
  <div class="flex flex-col col-span-full bg-white dark:bg-slate-800 shadow-lg rounded-sm border border-slate-200 dark:border-slate-700">
    <div class="px-5 py-6">
      <div class="md:flex md:justify-between md:items-center">
        <!-- Left side -->
        <div class="flex items-center mb-4 md:mb-0">
          <!-- Avatar -->
          <div class="mr-4">
            <img v-if="driverInfo.avatar_url" :src="driverInfo.avatar_url" class="inline-flex rounded-full" width="64" height="64" alt="User" />
          </div>
          <!-- User info -->
          <div>
            <div class="mb-2">Hey <strong class="font-medium text-slate-800 dark:text-slate-100">{{ driverInfo.username }}</strong> 👋, this is your carbon footprint:</div>
            <div class="text-3xl font-bold text-emerald-500">{{ driverInfo.total_carbon_emission }} ㎏ CO₂</div>
          </div>
        </div>
        <!-- Right side -->
<!--        <ul class="shrink-0 flex flex-wrap justify-end md:justify-start -space-x-3 -ml-px">-->
<!--          &lt;!&ndash; Example Icons &ndash;&gt;-->
<!--          <li v-for="icon in icons" :key="icon">-->
<!--            <a class="block" href="#0">-->
<!--              <img :src="icon" class="w-9 h-9 rounded-full" width="36" height="36" :alt="icon" />-->
<!--            </a>-->
<!--          </li>-->
<!--          <li>-->
<!--            <button class="flex justify-center items-center w-9 h-9 rounded-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600 text-indigo-500 shadow-sm transition duration-150">-->
<!--              <span class="sr-only">Add new user</span>-->
<!--              <svg class="w-4 h-4 fill-current" viewBox="0 0 16 16">-->
<!--                <path d="M15 7H9V1c0-.6-.4-1-1-1S7 .4 7 1v6H1c-.6 0-1 .4-1 1s.4 1 1 1h6v6c0 .6.4 1 1 1s1-.4 1-1V9h6c.6 0 1-.4 1-1s-.4-1-1-1z" />-->
<!--              </svg>-->
<!--            </button>-->
<!--          </li>-->
<!--        </ul>-->
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'FintechIntro',
  data() {
    return {
      driverInfo: {},
      icons: [
        '../../images/company-icon-01.svg',
        '../../images/company-icon-02.svg',
        '../../images/company-icon-03.svg',
        '../../images/company-icon-04.svg'
      ]
    };
  },
  created() {
    this.fetchDriverInfo();
  },
  methods: {
    async fetchDriverInfo() {
      try {
        const response = await axios.get('/api/driver-info');
        this.driverInfo = response.data;
        if (this.driverInfo.avatar_url) {
          this.driverInfo.avatar_url = `${window.location.origin}/api/avatars/${this.driverInfo.avatar_url}`;
        }
      } catch (error) {
        console.error('Error fetching driver info:', error);
      }
    }
  }
};
</script>
