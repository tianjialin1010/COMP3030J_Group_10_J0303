<template>
  <div class="flex h-[100dvh] overflow-hidden">
    <!-- Sidebar -->
    <Sidebar :sidebarOpen="sidebarOpen" @close-sidebar="sidebarOpen = false" />

    <!-- Content area -->
    <div class="relative flex flex-col flex-1 overflow-y-auto overflow-x-hidden">
      <!-- Site header -->
      <Header :sidebarOpen="sidebarOpen" @toggle-sidebar="sidebarOpen = !sidebarOpen" />

      <main class="grow">
        <div class="px-4 sm:px-6 lg:px-8 py-8 w-full max-w-9xl mx-auto">
          <!-- Page header -->
          <div class="sm:flex sm:justify-between sm:items-center mb-8">
            <!-- Left: Title -->
            <div class="mb-4 sm:mb-0">
              <h1 class="text-2xl md:text-3xl text-slate-800 dark:text-slate-100 font-bold">Orders ✨</h1>
            </div>

            <!-- Right: Actions  -->
            <div class="grid grid-flow-col sm:auto-cols-max justify-start sm:justify-end gap-2">
              <!-- Delete button -->
              <DeleteButton :selectedItems="selectedItems" apiUrl="/api/delete-orders" />
<!--              &lt;!&ndash; Dropdown &ndash;&gt;-->
<!--              <DateSelect />-->
<!--              &lt;!&ndash; Filter button &ndash;&gt;-->
<!--              <FilterButton align="right" />-->
              <!-- Add order button -->
              <button class="btn bg-indigo-500 hover:bg-indigo-600 text-white" @click="showModal=true">
                <svg class="w-4 h-4 fill-current opacity-50 shrink-0" viewBox="0 0 16 16">
                  <path d="M15 7H9V1c0-.6-.4-1-1-1S7 .4 7 1v6H1c-.6 0-1 .4-1 1s.4 1 1 1h6v6c0 .6.4 1 1 1s1-.4 1-1V9h6c.6 0 1-.4 1-1s-.4-1-1-1z" />
                </svg>
                <span class="hidden xs:block ml-2">Add Order</span>
              </button>
            </div>
          </div>

          <!-- Table -->
          <OrdersTable :orders="orders" :total="total" @change-selection="updateSelectedItems" />

          <!-- Pagination -->
          <div class="mt-8">
            <PaginationClassic :page="page" :perPage="per_page" :total="total" @change-page="fetchOrders" />
          </div>

          <!-- Add Order Modal -->
          <AddOrderModal v-if="showModal" @close-modal="showModal = false" :fetchOrders="fetchOrders" />
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import Sidebar from '../../partials/Sidebar.vue'
import Header from '../../partials/Header.vue'
import DeleteButton from '../../partials/actions/DeleteButton.vue'
import DateSelect from '../../components/DateSelect.vue'
import FilterButton from '../../components/DropdownFilter.vue'
import OrdersTable from '../../partials/orders/OrdersTable.vue'
import PaginationClassic from '../../components/PaginationClassic.vue'
import AddOrderModal from '../../partials/actions/AddOrderModal.vue'
import axios from 'axios'

export default {
  name: 'Orders',
  components: {
    Sidebar,
    Header,
    DeleteButton,
    DateSelect,
    FilterButton,
    OrdersTable,
    PaginationClassic,
    AddOrderModal,
  },
  setup() {
    const sidebarOpen = ref(false)
    const selectedItems = ref([])
    const showModal = ref(false)
    const orders = ref([])
    const total = ref(0)
    const page = ref(1)
    const per_page = ref(10)

    const fetchOrders = async (newPage = 1) => {
      page.value = newPage
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/orders', {
          params: { page: page.value, per_page: per_page.value }
        })
        orders.value = response.data.orders
        total.value = response.data.total
      } catch (error) {
        console.error('There was an error fetching the orders:', error)
      }
    }

    const updateSelectedItems = (selected) => {
      selectedItems.value = selected
    }

    onMounted(() => {
      fetchOrders()
    })

    return {
      sidebarOpen,
      selectedItems,
      orders,
      total,
      page,
      per_page,
      fetchOrders,
      updateSelectedItems,
      showModal,
    }
  }
}
</script>
