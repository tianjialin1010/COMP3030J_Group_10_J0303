<template>
  <header class="sticky top-0 bg-white dark:bg-[#182235] border-b border-slate-200 dark:border-slate-700 z-30">
    <div class="px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16 -mb-px">

        <!-- Header: Left side -->
        <div class="flex">

          <!-- Hamburger button -->
          <button class="text-slate-500 hover:text-slate-600 lg:hidden" @click.stop="$emit('toggle-sidebar')" aria-controls="sidebar" :aria-expanded="sidebarOpen">
            <span class="sr-only">Open sidebar</span>
            <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <rect x="4" y="5" width="16" height="2" />
              <rect x="4" y="11" width="16" height="2" />
              <rect x="4" y="17" width="16" height="2" />
            </svg>
          </button>

        </div>

        <!-- Header: Right side -->
        <div class="flex items-center space-x-3">
          <div>
<!--            <button-->
<!--              class="w-8 h-8 flex items-center justify-center bg-slate-100 hover:bg-slate-200 dark:bg-slate-700 dark:hover:bg-slate-600/80 rounded-full ml-3"-->
<!--              :class="{ 'bg-slate-200': searchModalOpen }"-->
<!--              @click.stop="searchModalOpen = true"-->
<!--              aria-controls="search-modal"-->
<!--            >-->
<!--              <span class="sr-only">Search</span>-->
<!--              <svg class="w-4 h-4" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">-->
<!--                <path class="fill-current text-slate-500 dark:text-slate-400" d="M7 14c-3.86 0-7-3.14-7-7s3.14-7 7-7 7 3.14 7 7-3.14 7-7 7zM7 2C4.243 2 2 4.243 2 7s2.243 5 5 5 5-2.243 5-5-2.243-5-5-5z" />-->
<!--                <path class="fill-current text-slate-400 dark:text-slate-500" d="M15.707 14.293L13.314 11.9a8.019 8.019 0 01-1.414 1.414l2.393 2.393a.997.997 0 001.414 0 .999.999 0 000-1.414z" />-->
<!--              </svg>-->
<!--            </button>-->
<!--            <SearchModal id="search-modal" searchId="search" :modalOpen="searchModalOpen" @open-modal="searchModalOpen = true" @close-modal="searchModalOpen = false" />-->
          </div>
<!--          <Notifications align="right" />-->
<!--          <Help align="right" />-->
          <ThemeToggle />
          <!-- Divider -->
          <hr class="w-px h-6 bg-slate-200 dark:bg-slate-700 border-none" />
          <UserMenu align="right" />
          <!-- Logout Button -->
          <button @click="handleLogout" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded">
            Logout!
          </button>
        </div>

      </div>
    </div>
  </header>
</template>

<script>
import { ref } from 'vue'
import { mapActions } from 'vuex'
import SearchModal from '../components/ModalSearch.vue'
import Notifications from '../components/DropdownNotifications.vue'
import Help from '../components/DropdownHelp.vue'
import ThemeToggle from '../components/ThemeToggle.vue'
import UserMenu from '../components/DropdownProfile.vue'
import axios from 'axios'

export default {
  name: 'Header',
  props: ['sidebarOpen'],
  components: {
    SearchModal,
    Notifications,
    Help,
    ThemeToggle,
    UserMenu,
  },
  setup() {
    const searchModalOpen = ref(false)
    return {
      searchModalOpen,
    }
  },
  methods: {
    ...mapActions(['logout']),
    handleLogout() {
      axios.post('/api/logout')
        .then(response => {
          if (response.data.success) {
            this.logout(); // 调用 Vuex 动作来清除会话数据
            // 清除浏览器历史记录
            window.location.replace('http://127.0.0.1:5000');
          } else {
            alert('Logout failed!');
          }
        })
        .catch(error => {
          console.error('Error during logout:', error);
          alert('Logout failed!');
        });
    }
  }
}
</script>