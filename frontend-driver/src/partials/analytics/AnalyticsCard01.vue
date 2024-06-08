<template>
  <div class="flex flex-col col-span-full xl:col-span-8 bg-white dark:bg-slate-800 shadow-lg rounded-sm border border-slate-200 dark:border-slate-700">
    <header class="px-5 py-4 border-b border-slate-100 dark:border-slate-700 flex items-center">
      <h2 class="font-semibold text-slate-800 dark:text-slate-100">Analytics</h2>
    </header>
    <div class="px-5 py-1">
      <div class="flex flex-wrap">
        <!-- Unique Visitors -->
        <div class="flex items-center py-2">
          <div class="mr-5">
            <div class="flex items-center">
              <div class="text-3xl font-bold text-slate-800 dark:text-slate-100 mr-2">24.7K</div>
              <div class="text-sm font-medium text-emerald-500">+49%</div>
            </div>
            <div class="text-sm text-slate-500 dark:text-slate-400">Carbon integral</div>
          </div>
          <div class="hidden md:block w-px h-8 bg-slate-200 dark:bg-slate-700 mr-5" aria-hidden="true"></div>
        </div>
        <!-- Total Pageviews -->
        <div class="flex items-center py-2">
          <div class="mr-5">
            <div class="flex items-center">
              <div class="text-3xl font-bold text-slate-800 dark:text-slate-100 mr-2">56.9K</div>
              <div class="text-sm font-medium text-emerald-500">+7%</div>
            </div>
            <div class="text-sm text-slate-500 dark:text-slate-400">Energy saving</div>
          </div>
          <div class="hidden md:block w-px h-8 bg-slate-200 dark:bg-slate-700 mr-5" aria-hidden="true"></div>
        </div>
        <!-- Bounce Rate -->
        <div class="flex items-center py-2">
          <div class="mr-5">
            <div class="flex items-center">
              <div class="text-3xl font-bold text-slate-800 dark:text-slate-100 mr-2">54</div>
              <div class="text-sm font-medium text-amber-500">-7</div>
            </div>
            <div class="text-sm text-slate-500 dark:text-slate-400">Order quantity</div>
          </div>
          <div class="hidden md:block w-px h-8 bg-slate-200 dark:bg-slate-700 mr-5" aria-hidden="true"></div>
        </div>
        <!-- Visit Duration-->
        <div class="flex items-center">
          <div>
            <div class="flex items-center">
              <div class="text-3xl font-bold text-slate-800 dark:text-slate-100 mr-2">11m 56s</div>
              <div class="text-sm font-medium text-amber-500">+7%</div>
            </div>
            <div class="text-sm text-slate-500 dark:text-slate-400">Average time saved</div>
          </div>
        </div>
      </div>
    </div>
    <!-- Chart built with Chart.js 3 -->
    <div class="grow">
      <!-- Change the height attribute to adjust the chart height -->
      <LineChart :data="chartData" width="800" height="300" />
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import LineChart from '../../charts/LineChart03.vue'
import { subMonths, format } from 'date-fns'

// Import utilities
import { tailwindConfig, hexToRGB } from '../../utils/Utils'

export default {
  name: 'AnalyticsCard01',
  components: {
    LineChart,
  },
  setup() {
    const generateLastSixMonthsLabels = () => {
      const labels = []
      for (let i = 0; i < 6; i++) {
        const date = subMonths(new Date(), i)
        labels.push(format(date, 'MM-dd-yyyy'))
      }
      return labels.reverse()
    }

    const chartData = ref({
      labels: generateLastSixMonthsLabels(),
      datasets: [
        // Indigo line
        {
          label: 'Current',
          data: [
            5000, 8700, 7500, 12000, 11000, 9500,
          ],
          fill: true,
          backgroundColor: `rgba(${hexToRGB(tailwindConfig().theme.colors.blue[500])}, 0.08)`,
          borderColor: tailwindConfig().theme.colors.indigo[500],
          borderWidth: 2,
          tension: 0,
          pointRadius: 0,
          pointHoverRadius: 3,
          pointBackgroundColor: tailwindConfig().theme.colors.indigo[500],
          pointHoverBackgroundColor: tailwindConfig().theme.colors.indigo[500],
          pointBorderWidth: 0,
          pointHoverBorderWidth: 0,
          clip: 20,
        },
        // Gray line
        {
          label: 'Previous',
          data: [
            8000, 5000, 6500, 5000, 6500, 12000,
          ],
          borderColor: `rgba(${hexToRGB(tailwindConfig().theme.colors.slate[500])}, 0.25)`,
          fill: false,
          borderWidth: 2,
          tension: 0,
          pointRadius: 0,
          pointHoverRadius: 3,
          pointBackgroundColor: `rgba(${hexToRGB(tailwindConfig().theme.colors.slate[500])}, 0.25)`,
          pointHoverBackgroundColor: `rgba(${hexToRGB(tailwindConfig().theme.colors.slate[500])}, 0.25)`,
          pointBorderWidth: 0,
          pointHoverBorderWidth: 0,
          clip: 20,
        },
      ],
    })

    return {
      chartData,
    }
  }
}
</script>
