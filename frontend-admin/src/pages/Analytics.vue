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
              <h1 class="text-2xl md:text-3xl text-slate-800 dark:text-slate-100 font-bold">Analytics 📉</h1>
            </div>
        
            <!-- Right: Actions -->
            <div class="grid grid-flow-col sm:auto-cols-max justify-start sm:justify-end gap-2">
                
              <!-- Datepicker built with flatpickr -->
              <div class="text-xl text-slate-600 dark:text-slate-300 " align="right" >{{ currentDateTime }}</div>
                
            </div>
          
          </div>

          <!-- Cards -->
          <div class="grid grid-cols-12 gap-6">

            <!-- Line chart (Analytics) -->
            <AnalyticsCard01 />
            <!--  Line chart (Active Users Right Now) -->
            <AnalyticsCard02 />
            <!-- Stacked bar chart (Acquisition Channels) -->
            <AnalyticsCard03 />
            <!-- Horizontal bar chart (Audience Overview) -->
<!--            <AnalyticsCard04 />-->
<!--            &lt;!&ndash; Report card (Top Channels) &ndash;&gt;
            <AnalyticsCard05 />
            &lt;!&ndash; Report card (Top Pages) &ndash;&gt;
            <AnalyticsCard06 />-->
            <!-- Report card (Top Countries) -->
            <AnalyticsCard07 />
<!--            &lt;!&ndash; Doughnut chart (Sessions By Device) &ndash;&gt;
            <AnalyticsCard08 />
            &lt;!&ndash; Doughnut chart (Visit By Age Category) &ndash;&gt;
            <AnalyticsCard09 />-->
            <!-- Polar chart (Sessions By Gender) -->
            <AnalyticsCard10 />
<!--            &lt;!&ndash; Table (Top Products) &ndash;&gt;
            <AnalyticsCard11 />-->

          </div>

        </div>
      </main>

    </div> 

  </div>
</template>

<script>
import {onMounted, ref} from 'vue'
import Sidebar from '../partials/Sidebar.vue'
import Header from '../partials/Header.vue'
import Datepicker from '../components/Datepicker.vue'
import AnalyticsCard01 from '../partials/analytics/AnalyticsCard01.vue'
import AnalyticsCard02 from '../partials/analytics/AnalyticsCard02.vue'
import AnalyticsCard03 from '../partials/analytics/AnalyticsCard03.vue'
import AnalyticsCard04 from '../partials/analytics/AnalyticsCard04.vue'
import AnalyticsCard05 from '../partials/analytics/AnalyticsCard05.vue'
import AnalyticsCard06 from '../partials/analytics/AnalyticsCard06.vue'
import AnalyticsCard07 from '../partials/analytics/AnalyticsCard07.vue'
import AnalyticsCard08 from '../partials/analytics/AnalyticsCard08.vue'
import AnalyticsCard09 from '../partials/analytics/AnalyticsCard09.vue'
import AnalyticsCard10 from '../partials/analytics/AnalyticsCard10.vue'
import AnalyticsCard11 from '../partials/analytics/AnalyticsCard11.vue'

export default {
  name: 'Analytics',
  components: {
    Sidebar,
    Header,
    Datepicker,
    AnalyticsCard01,
    AnalyticsCard02,
    AnalyticsCard03,
    AnalyticsCard04,
    AnalyticsCard05,
    AnalyticsCard06,
    AnalyticsCard07,
    AnalyticsCard08,
    AnalyticsCard09,
    AnalyticsCard10,
    AnalyticsCard11,
  },
  setup() {

    const sidebarOpen = ref(false)

    const currentDateTime = ref(new Date().toLocaleString())

    onMounted(() => {
      setInterval(() => {
        currentDateTime.value = new Date().toLocaleString()
      }, 1000)
    })
    return {
      sidebarOpen,
      currentDateTime,
    }  
  }
}
</script>