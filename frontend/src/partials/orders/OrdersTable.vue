<template>
  <div class="bg-white dark:bg-slate-800 shadow-lg rounded-sm border border-slate-200 dark:border-slate-700 relative">
    <header class="px-5 py-4">
      <h2 class="font-semibold text-slate-800 dark:text-slate-100">All Orders <span class="text-slate-400 dark:text-slate-500 font-medium">442</span></h2>
    </header>
    <div>

      <!-- Table -->
      <div class="overflow-x-auto">
        <table class="table-auto w-full dark:text-slate-300 divide-y divide-slate-200 dark:divide-slate-700">
          <!-- Table header -->
          <thead class="text-xs uppercase text-slate-500 dark:text-slate-400 bg-slate-50 dark:bg-slate-900/20 border-t border-slate-200 dark:border-slate-700">
            <tr>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap w-px">
                <div class="flex items-center">
                  <label class="inline-flex">
                    <span class="sr-only">Select all</span>
                    <input class="form-checkbox" type="checkbox" v-model="selectAll" @click="checkAll" />
                  </label>
                </div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">OrderID</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">IU_ID</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">AD_ID</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Status</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold">Destination</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold">Mileage</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Created_at</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Completed_at</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Vehicle_Type</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Carbon_Emission</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">CarID</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Startlocation</div>
              </th>

            </tr>
          </thead>
          <!-- Table body -->
          <Order
            v-for="order in orders"
            :key="order.id"
            :order="order"
            v-model:selected="selected"
            :value="order.id"
          />
        </table>

      </div>
    </div>
  </div>
</template>

<script>
import {onMounted, ref, watch} from 'vue'
import Order from './OrdersTableItem.vue'
import axios from 'axios';

import Image01 from '../../images/icon-01.svg'
import Image02 from '../../images/icon-02.svg'
import Image03 from '../../images/icon-03.svg'

export default {
  name: 'OrdersTable',
  components: {
    Order,
  },  
  props: ['selectedItems'],
  setup(props, { emit }) {

    const selectAll = ref(false)
    const selected = ref([])
    const orders = ref([])

    const fetchOrders = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/orders')
        orders.value = response.data
      } catch (error) {
        console.error('There was an error fetching the customers:', error)
      }
    }

    const checkAll = () => {
      selected.value = []
      if (!selectAll.value) {
        selected.value = orders.value.map(order => order.id)
      }
    }
    
    watch(selected, () => {
      selectAll.value = orders.value.length === selected.value.length ? true : false
      emit('change-selection', selected.value)
    })    
    
    onMounted(() => {
      fetchOrders()
    })

    return {
      selectAll,
      selected,
      checkAll,
      orders,
    }
  }
}
</script>