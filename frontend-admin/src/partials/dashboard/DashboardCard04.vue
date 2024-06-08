<template>
  <div class="flex flex-col col-span-full sm:col-span-6 bg-white dark:bg-slate-800 shadow-lg rounded-sm border border-slate-200 dark:border-slate-700">
    <header class="px-5 py-4 border-b border-slate-100 dark:border-slate-700">
      <h2 class="font-semibold text-slate-800 dark:text-slate-100">Calendar</h2>
    </header>
    <div class="p-5">
      <vue-cal
        :events="events"
        default-view="month"
        :time="false"
        class="bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border-slate-200 dark:border-slate-700"
      />
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import VueCal from 'vue-cal'
import 'vue-cal/dist/vuecal.css'

export default {
  name: 'DashboardCard04',
  components: {
    VueCal
  },
  setup() {
    const events = ref([
      {
        start: new Date(),
        end: new Date(),
        title: 'Today\'s Event'
      },
      // 添加更多事件
    ])

    return {
      events
    }
  }
}
</script>

<style scoped>
/* 自定义日历样式 */
.vuecal__cell {
  background-color: #f9fafb;
}

.vuecal__event {
  background-color: #3b82f6;
  color: white;
}
</style>
