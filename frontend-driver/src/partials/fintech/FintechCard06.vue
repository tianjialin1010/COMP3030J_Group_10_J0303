<template>
  <div class="col-span-full xl:col-span-6 bg-white dark:bg-slate-800 shadow-lg rounded-sm border border-slate-200 dark:border-slate-700">
    <header class="px-5 py-4 border-b border-slate-100 dark:border-slate-700">
      <h2 class="font-semibold text-slate-800 dark:text-slate-100">Recent Order 👎</h2>
    </header>
    <div class="p-3">

      <!-- Table -->
      <div class="overflow-x-auto">
        <table class="table-auto w-full dark:text-slate-300">
          <!-- Table header -->
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
                <div class="font-semibold text-right">Wasting</div>
              </th>
            </tr>
          </thead>
          <!-- Table body -->
          <tbody class="text-sm divide-y divide-slate-100 dark:divide-slate-700" v-if="recentOrders.length">
            <tr v-for="order in recentOrders" :key="order.order_id">
              <td class="p-2 whitespace-nowrap">
                <div class="flex items-center">
                  <div class="shrink-0 rounded-full mr-2 sm:mr-3 bg-sky-500">
                    <svg class="w-9 h-9 fill-current text-sky-50" viewBox="0 0 36 36">
                      <path d="M18 26a8 8 0 1 1 8-8 8.009 8.009 0 0 1-8 8Zm0-14a6 6 0 1 0 0 12 6 6 0 0 0 0-12Z" />
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
                <div class="font-medium text-red-500 text-right">+{{ order.carbon_wasting.toFixed(2) }} ㎏ CO₂</div>
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
  name: 'FintechCard06',
  setup() {
    const recentOrders = ref([])

    const fetchRecentOrders = async () => {
      try {
        const response = await axios.get('/api/recent-orders-worst')
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
