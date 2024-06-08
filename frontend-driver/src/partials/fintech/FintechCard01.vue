//改成司机碳排放（蓝线）理想碳排放（黄线）他人平均碳排放（灰线）
<template>
  <div class="flex flex-col col-span-full xl:col-span-8 bg-white dark:bg-slate-800 shadow-lg rounded-sm border border-slate-200 dark:border-slate-700">
    <header class="px-5 py-4 border-b border-slate-100 dark:border-slate-700 flex items-center">
        <h2 class="font-semibold text-slate-800 dark:text-slate-100">Carbon Emission</h2>
    </header>
    <!-- Chart built with Chart.js 3 -->
    <!-- Change the height attribute to adjust the chart height -->
    <LineChart :data="chartData" width="800" height="300" />
  </div>
</template>

<script>
import { ref } from 'vue'
import LineChart from '../../charts/LineChart05.vue'

// Import utilities
import { tailwindConfig, hexToRGB } from '../../utils/Utils'

export default {
  name: 'FintechCard01',
  components: {
    LineChart,
  },
  setup() {
    const chartData = ref({
      labels: [
        '06-01-2024', '05-28-2024', '05-21-2024', '05-14-2024', '05-07-2024',
        '05-01-2024', '04-28-2024', '04-21-2024', '04-14-2024', '04-07-2024',
        '04-01-2024', '03-28-2024', '03-21-2024', '03-14-2024', '03-07-2024',
        '03-01-2024', '02-28-2024', '02-21-2024', '02-14-2024', '02-07-2024',
        '02-01-2024', '01-28-2024', '01-21-2024', '01-14-2024', '01-07-2024',
        '01-01-2024'
      ],
      datasets: [
        // Indigo line
        {
          label: 'Your emissions',
          data : [
             124.34, 456.78, 342.21, 219.85, 168.94, 292.56, 478.90,
             125.34, 310.67, 199.45, 285.34, 167.89, 389.12, 320.34,
             201.45, 150.78, 421.98, 189.45, 299.67, 411.23, 229.89,
             350.12, 277.56, 413.67, 180.34, 482.4
          ],
          borderColor: tailwindConfig().theme.colors.indigo[500],
          fill: true,
          backgroundColor: `rgba(${hexToRGB(tailwindConfig().theme.colors.blue[500])}, 0.08)`,
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
        // Yellow line
        {
          label: 'Expected emissions',
          data: [
            379.57, 125.62, 427.34, 265.18, 200.87, 347.23, 301.45,
            413.97, 162.34, 473.85, 412.06, 273.84, 439.25, 190.67,
            276.98, 360.15, 257.44, 321.77, 385.65, 311.23, 370.98,
            229.45, 415.32, 315.74, 268.45, 480.89
          ],
          borderColor: tailwindConfig().theme.colors.green[400],
          borderDash: [4, 4],
          fill: false,
          borderWidth: 2,
          tension: 0,
          pointRadius: 0,
          pointHoverRadius: 3,
          pointBackgroundColor: tailwindConfig().theme.colors.green[400],
          clip: 20,
        },
        // gray line
        {
          label: "Average emissions",
          data: [
              323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36,
              323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36,
              323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36,
              323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36, 323.36,
              323.36
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
