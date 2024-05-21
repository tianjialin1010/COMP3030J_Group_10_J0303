<!-- CustomersTable.vue -->
<template>
  <div class="bg-white dark:bg-slate-800 shadow-lg rounded-sm border border-slate-200 dark:border-slate-700 relative">
    <header class="px-5 py-4">
      <h2 class="font-semibold text-slate-800 dark:text-slate-100">All Customers <span class="text-slate-400 dark:text-slate-500 font-medium">{{ total }}</span></h2>
    </header>
    <div>
      <!-- Table-->
      <div class="overflow-x-auto">
        <table class="table-auto w-full dark:text-slate-300">
          <!-- Table header -->
          <thead class="text-xs font-semibold uppercase text-slate-500 dark:text-slate-400 bg-slate-50 dark:bg-slate-900/20 border-t border-b border-slate-200 dark:border-slate-700">
          <tr>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap w-px">
                <div class="flex items-center">
                  <label class="inline-flex">
                    <span class="sr-only">Select all</span>
                    <input class="form-checkbox" type="checkbox" v-model="selectAll" @click="checkAll" />
                  </label>
                </div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap w-px">
                <span class="sr-only">Favourite</span>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Name</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Email</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap text-left">
                <div class="font-semibold">Role</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Registered</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold text-left">Total footprint</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <div class="font-semibold">Refunds</div>
              </th>
              <th class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
                <span class="sr-only">Menu</span>
              </th>
            </tr>
          </thead>
          <tbody class="text-sm divide-y divide-slate-200 dark:divide-slate-700">
            <Customer
              v-for="customer in customers"
              :key="customer.id"
              :customer="customer"
              v-model:selected="selected"
              :value="customer.id"
            />
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch } from 'vue'
import Customer from './CustomersTableItem.vue'

export default {
  name: 'CustomersTable',
  components: {
    Customer,
  },
  props: {
    selectedItems: Array,
    customers: Array,
    total: Number
  },
  setup(props, { emit }) {
    const selectAll = ref(false)
    const selected = ref([])

    const checkAll = () => {
      selected.value = []
      if (!selectAll.value) {
        selected.value = props.customers.map(customer => customer.id)
      }
    }

    watch(selected, () => {
      selectAll.value = props.customers.length === selected.value.length ? true : false
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
