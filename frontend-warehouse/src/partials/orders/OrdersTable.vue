<template>
  <div class="bg-white dark:bg-slate-800 shadow-lg rounded-sm border border-slate-200 dark:border-slate-700 relative">
    <header class="px-5 py-4">
      <h2 class="font-semibold text-slate-800 dark:text-slate-100">All Orders <span class="text-slate-400 dark:text-slate-500 font-medium">{{ total }}</span></h2>
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
<!--              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap w-px">-->
<!--                <span class="sr-only">Favourite</span>-->
<!--              </th>-->
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap text-left">
                <div class="font-semibold text-left">OrderID</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Assigned Driver ID</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap text-right">
                <div class="font-semibold text-left">Status</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap text-left">
                <div class="font-semibold">Origin</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold">Destination</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold">License Plate</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Created At</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Completed At</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Mileage (KM)</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Estimate Time</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Carbon Emission</div>
              </th>
            </tr>
          </thead>
          <tbody class="text-sm divide-y divide-slate-200 dark:divide-slate-700">
            <Order
              v-for="order in orders"
              :key="order.id"
              :order="order"
              v-model:selected="selected"
              :value="order.id"
            />
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch } from 'vue'
import Order from './OrdersTableItem.vue'

export default {
  name: 'OrdersTable',
  components: {
    Order,
  },
  props: ['selectedItems', 'orders', 'total'],
  setup(props, { emit }) {
    const selectAll = ref(false)
    const selected = ref([])

    const checkAll = () => {
      selected.value = []
      if (!selectAll.value) {
        selected.value = props.orders.map(order => order.id)
      }
    }

    watch(selected, () => {
      selectAll.value = props.orders.length === selected.value.length
      emit('change-selection', selected.value)
    })

    return {
      selectAll,
      selected,
      checkAll,
    }
  }
}
</script>
