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
              <h1 class="text-2xl md:text-3xl text-slate-800 dark:text-slate-100 font-bold">Contect Page. ✨</h1>
            </div>
            <!-- Right: Actions -->
            <div class="grid grid-flow-col sm:auto-cols-max justify-start sm:justify-end gap-2">
              <!-- Search form -->
              <SearchForm />
              <!-- Add member button -->
<!--              <button class="btn bg-indigo-500 hover:bg-indigo-600 text-white">-->
<!--                <svg class="w-4 h-4 fill-current opacity-50 shrink-0" viewBox="0 0 16 16">-->
<!--                  <path d="M15 7H9V1c0-.6-.4-1-1-1S7 .4 7 1v6H1c-.6 0-1 .4-1 1s.4 1 1 1h6v6c0 .6.4 1 1 1s1-.4 1-1V9h6c.6 0 1-.4 1-1s-.4-1-1-1z" />-->
<!--                </svg>-->
<!--                <span class="hidden xs:block ml-2">Add Member</span>-->
<!--              </button>-->
            </div>
          </div>

          <!-- Cards -->
          <div class="grid grid-cols-12 gap-6">
            <UsersTabsCard
              v-for="item in items"
              :key="item.id"
              :item="item"
            />
          </div>

          <!-- Pagination -->
          <div class="mt-8">
            <PaginationNumeric />
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Sidebar from '../../partials/Sidebar.vue'
import Header from '../../partials/Header.vue'
import SearchForm from '../../components/SearchForm.vue'
import UsersTabsCard from '../../partials/community/UsersTabsCard.vue'
import PaginationNumeric from '../../components/PaginationNumeric.vue'

function formatAvatarUrl(url) {
  if (url.startsWith('http')) {
    return url;  // 如果已经是完整的 URL，直接返回
  }
  return `http://127.0.0.1:5000/api/avatars/${url}`;  // 否则，构建完整的 URL
}


export default {
  name: 'UsersTabs',
  components: {
    Sidebar,
    Header,
    SearchForm,
    UsersTabsCard,
    PaginationNumeric,
  },
  setup() {
    const sidebarOpen = ref(false)
    const items = ref([])  // 初始为空数组

    // 从API获取用户信息
    const fetchUsers = async () => {
      try {
        const response = await axios.get('/api/users')
        items.value = response.data.map(user => ({
          id: user.id,
          name: user.username,
          image: formatAvatarUrl(user.avatar_url), // 确保后端返回头像URL
          link: '#0',
          location: user.role, // 角色可以用来表示位置或职责
          content: 'Status: ' + user.status + ', total mileage: ' + user.totalMileage + 'KM',
        }))
      } catch (error) {
        console.error('Error fetching users:', error)
      }
    }

    onMounted(fetchUsers)

    return {
      sidebarOpen,
      items,
    }
  }
}
</script>
