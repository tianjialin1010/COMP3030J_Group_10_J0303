<!-- EndOrder.vue -->
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
          <div class="sm:flex sm:justify-between sm:items-center mb-5">
            <!-- Left: Title -->
            <div class="mb-4 sm:mb-0">
              <h1 class="text-2xl md:text-3xl text-slate-800 dark:text-slate-100 font-bold">End these orders ✨</h1>
            </div>
          </div>
          <!-- Page content -->
          <div class="flex flex-col space-y-10 sm:flex-row sm:space-x-6 sm:space-y-0 md:flex-col md:space-x-0 md:space-y-10 xl:flex-row xl:space-x-6 xl:space-y-0 mt-9">
            <!-- Sidebar -->
            <JobSidebar @update-filter="updateFilter" />
            <!-- Content -->
            <div class="w-full">
              <!-- Search form -->
              <div class="mb-5">
                <form class="relative">
                  <label for="job-search" class="sr-only">Search</label>
                  <input id="job-search" class="form-input w-full pl-9 bg-white dark:bg-slate-800" type="search" placeholder="Search job title or keyword…" />
                  <button class="absolute inset-0 right-auto group" type="submit" aria-label="Search">
                    <svg class="w-4 h-4 shrink-0 fill-current text-slate-400 dark:text-slate-500 group-hover:text-slate-500 dark:group-hover:text-slate-400 ml-3 mr-2" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
                      <path d="M7 14c-3.86 0-7-3.14-7-7s3.14-7 7-7 7.14 7 7 7-3.14 7-7 7zM7 2C4.243 2 2 4.243 2 7s2.243 5 5 5 5-2.243 5-5-2.243-5-5-5z" />
                      <path d="M15.707 14.293L13.314 11.9a8.019 8.019 0 01-1.414 1.414l2.393 2.393a.997.997 0 001.414 0 .999.999 0 000-1.414z" />
                    </svg>
                  </button>
                </form>
              </div>
              <!-- Jobs header -->
              <div class="flex justify-between items-center mb-4">
                <div class="text-sm text-slate-500 dark:text-slate-400 italic">Showing {{ filteredItems.length }} Jobs</div>
                <!-- Sort -->
                <div class="text-sm">
                  <span>Sort by </span>
                  <DropdownSort align="right" @sort-change="handleSortChange" />
                </div>
              </div>
              <!-- Job list -->
              <div class="space-y-2">
                <JobListItem
                  v-for="item in filteredItems"
                  :key="item.order_id"
                  :item="item"
                  @click="openModal(item)"
                />
              </div>
              <!-- Pagination -->
              <div class="mt-6">
                <PaginationNumeric :page="page" :total="total" :per-page="perPage" @change-page="fetchJobs" />
              </div>
            </div>
          </div>
        </div>
      </main>
      <WarehouseEndOrderModal v-if="showModal" :order="selectedOrder" @close-modal="showModal = false" />
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import Sidebar from '../../partials/Sidebar.vue'
import Header from '../../partials/Header.vue'
import JobSidebar from '../../partials/job/JobSidebar.vue'
import DropdownSort from '../../components/DropdownSort.vue'
import JobListItem from '../../partials/job/JobListItem.vue'
import PaginationNumeric from '../../components/PaginationNumeric.vue'
import WarehouseEndOrderModal from '../../partials/actions/WarehouseEndOrderModal.vue'
import axios from 'axios'

export default {
  name: 'JobListing',
  components: {
    WarehouseEndOrderModal,
    Sidebar,
    Header,
    JobSidebar,
    DropdownSort,
    JobListItem,
    PaginationNumeric,
  },
  setup() {
    const sidebarOpen = ref(false)
    const items = ref([])
    const filteredItems = ref([])
    const showModal = ref(false)
    const total = ref(0)
    const page = ref(1)
    const perPage = ref(10)
    const selectedOrder = ref(null)
    const sortType = ref('Newest')

    const filterCriteria = ref({
      destination: [],
      status: null,
      distance: null,
    })

    const fetchJobs = async (newPage = 1) => {
      page.value = newPage
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/orders', {
          params: { page: page.value, per_page: perPage.value }
        })
        items.value = response.data.orders
        total.value = response.data.total
        applyFilters()
      } catch (error) {
        console.error('Error fetching jobs:', error)
      }
    }

    const updateFilter = ({ type, value, checked }) => {
      if (type === 'destination') {
        if (checked) {
          filterCriteria.value.destination.push(value)
        } else {
          const index = filterCriteria.value.destination.indexOf(value)
          if (index > -1) {
            filterCriteria.value.destination.splice(index, 1)
          }
        }
      } else if (type === 'status') {
        filterCriteria.value.status = checked ? value : null
      } else if (type === 'distance') {
        filterCriteria.value.distance = checked ? value : null
      }
      applyFilters()
    }

    const applyFilters = () => {
      filteredItems.value = items.value.filter(item => {
        const meetsDestination = !filterCriteria.value.destination.length || filterCriteria.value.destination.includes(item.destination)
        const meetsStatus = !filterCriteria.value.status || item.status === filterCriteria.value.status
        const meetsDistance = !filterCriteria.value.distance || (
          (filterCriteria.value.distance === '0-100' && item.mileage <= 100) ||
          (filterCriteria.value.distance === '100-200' && item.mileage > 100 && item.mileage <= 200) ||
          (filterCriteria.value.distance === '>200' && item.mileage > 200)
        )
        return meetsDestination && meetsStatus && meetsDistance
      })
      applySort()
    }

    const applySort = () => {
      if (sortType.value === 'Newest') {
        filteredItems.value.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
      } else if (sortType.value === 'Oldest') {
        filteredItems.value.sort((a, b) => new Date(a.created_at) - new Date(b.created_at))
      }
    }

    const handleSortChange = (sort) => {
      sortType.value = sort
      applyFilters()
    }

    const openModal = (order) => {
      selectedOrder.value = order
      console.log('Selected Order:', selectedOrder.value)  // 添加日志
      showModal.value = true
    }

    onMounted(() => {
      fetchJobs(page.value)
    })

    return {
      sidebarOpen,
      items,
      filteredItems,
      showModal,
      total,
      page,
      perPage,
      selectedOrder,
      fetchJobs,
      updateFilter,
      openModal,
      handleSortChange,
    }
  }
}
</script>
