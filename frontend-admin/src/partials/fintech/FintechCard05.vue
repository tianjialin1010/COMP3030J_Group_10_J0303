<template>
  <div class="col-span-full xl:col-span-6 bg-white dark:bg-slate-800 shadow-lg rounded-sm border border-slate-200 dark:border-slate-700">
    <header class="px-5 py-4 border-b border-slate-100 dark:border-slate-700">
      <h2 class="font-semibold text-slate-800 dark:text-slate-100">Recent Orders 👍</h2>
    </header>
    <div class="p-3">
      <div class="overflow-x-auto">
        <table class="table-auto w-full dark:text-slate-300">
          <thead class="text-xs uppercase text-slate-400 dark:text-slate-500 bg-slate-50 dark:bg-slate-700 dark:bg-opacity-50 rounded-sm">
            <tr>
              <th class="p-2 whitespace-nowrap">
                <div class="font-semibold text-left">City</div>
              </th>
              <th class="p-2 whitespace-nowrap">
                <div class="font-semibold text-left">Vehicle</div>
              </th>
              <th class="p-2 whitespace-nowrap">
                <div class="font-semibold text-left">Date</div>
              </th>
              <th class="p-2 whitespace-nowrap">
                <div class="font-semibold text-right">Saving</div>
              </th>
            </tr>
          </thead>
          <tbody class="text-sm divide-y divide-slate-100 dark:divide-slate-700" v-if="recentOrders.length">
            <tr v-for="order in recentOrders" :key="order.completed_at">
              <td class="p-2 whitespace-nowrap">
                <div class="flex items-center">
                  <div class="shrink-0 rounded-full mr-2 sm:mr-3 bg-indigo-500">
                    <svg class="w-9 h-9 fill-current text-indigo-50" viewBox="0 0 36 36">
                      <path d="M24.446 19.335a2.5 2.5 0 00-3.522 3.194c-.845.63-1.87.97-2.924.971a4.979 4.979 0 01-1.113-.135 4.436 4.436 0 01-1.343 1.682 6.91 6.91 0 006.9-1.165 2.5 2.5 0 002-4.547h.002zM20.431 11.938a2.5 2.5 0 10-.4 2.014 5.027 5.027 0 012.723 3.078c.148-.018.297-.028.446-.03a4.5 4.5 0 011.7.334 7.023 7.023 0 00-4.469-5.396zM14.969 20.25a2.49 2.49 0 00-1.932-1.234A4.624 4.624 0 0113 18.5a4.97 4.97 0 011.348-3.391 4.456 4.456 0 01-.788-2.016A6.989 6.989 0 0011 18.5c.003.391.04.781.11 1.166a2.5 2.5 0 103.859.584z" />
                    </svg>
                  </div>
                  <div class="font-medium text-slate-800 dark:text-slate-100">{{ order.origin }} - {{ order.destination }}</div>
                </div>
              </td>
              <td class="p-2 whitespace-nowrap">
                <div>{{ order.vehicle_type }}</div>
              </td>
              <td class="p-2 whitespace-nowrap">
                <div>{{ order.completed_at }}</div>
              </td>
              <td class="p-2 whitespace-nowrap">
                <div class="font-medium text-emerald-500 text-right">-{{ order.carbon_saving.toFixed(2) }} ㎏ CO₂</div>
              </td>
            </tr>
          </tbody>
          <tbody v-else>
            <tr>
              <td colspan="4" class="p-2 text-center text-slate-500">No recent orders found.</td>
            </tr>
          </tbody>
        </table>
      </div>
<!--      <div class="text-center border-t border-slate-100 dark:border-slate-700 px-2">-->
<!--        <a class="block text-sm font-medium text-indigo-500 hover:text-indigo-600 dark:hover:text-indigo-400 pt-4 pb-1" href="#0">View All -&gt;</a>-->
<!--      </div>-->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { ref, onMounted } from 'vue'

export default {
  name: 'FintechCard05',
  setup() {
    const recentOrders = ref([])

    const fetchRecentOrders = async () => {
      try {
        const response = await axios.get('/api/recent-orders')
        recentOrders.value = response.data
      } catch (error) {
        console.error('Error fetching recent orders:', error)
      }
    }

    onMounted(() => {
      fetchRecentOrders()
    })

    return {
      recentOrders,
    }
  }
}
</script>
