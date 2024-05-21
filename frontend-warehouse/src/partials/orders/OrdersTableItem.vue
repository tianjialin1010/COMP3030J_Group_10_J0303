<!-- OrdersTableItem.vue -->
<template>
    <!-- Row -->
    <tr>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap w-px">
        <div class="flex items-center">
          <label class="inline-flex">
            <span class="sr-only">Select</span>
            <input :id="order.id" class="form-checkbox" type="checkbox" :value="value" @change="check" :checked="checked" />
          </label>
        </div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap text-center">
        <div class="font-medium text-slate-800 dark:text-slate-100">{{ order.id }}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-left font-medium text-emerald-500">{{ order.assigned_driver_id }}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap text-left">
        <div class="inline-flex font-medium rounded-full text-center px-2.5 py-0.5" :class="statusColor(order.status)">{{ order.status }}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-left">{{ order.origin }}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-left">{{ order.destination }}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-left">{{ order.license_plate }}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-left">{{ formatDate(order.created_at) }}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-left">{{ formatDate(order.completed_at) }}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-left">{{ order.mileage }}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-left">{{ formatEstimateTime(order.estimate_time) }}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-left">{{ order.carbon_emission }}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap w-px">
        <div class="flex items-center">
          <button
            class="text-slate-400 hover:text-slate-500 dark:text-slate-500 dark:hover:text-slate-400 transform"
            :class="descriptionOpen && 'rotate-180'"
            :aria-expanded="descriptionOpen"
            @click.prevent="descriptionOpen = !descriptionOpen"
            :aria-controls="`description-${order.id}`"
          >
            <span class="sr-only">Menu</span>
            <svg class="w-8 h-8 fill-current" viewBox="0 0 32 32">
              <path d="M16 20l-5.4-5.4 1.4-1.4 4 4 4-4 1.4 1.4z" />
            </svg>
          </button>
        </div>
      </td>
    </tr>
    <!--
    Example of content revealing when clicking the button on the right side:
    Note that you must set a "colSpan" attribute on the <td> element,
    and it should match the number of columns in your table
    -->
    <tr :id="`description-${order.id}`" role="region" :class="!descriptionOpen && 'hidden'">
      <td colspan="14" class="px-2 first:pl-5 last:pr-5 py-3">
        <div class="flex items-center bg-slate-50 dark:bg-slate-900/30 dark:text-slate-400 p-3 -mt-3">
          <svg class="w-4 h-4 shrink-0 fill-current text-slate-400 dark:text-slate-500 mr-2">
            <path d="M1 16h3c.3 0 .5-.1.7-.3l11-11c.4-.4.4-1 0-1.4l-3-3c-.4-.4-1-.4-1.4 0l-11 11c-.2.2-.3.4-.3.7v3c0 .6.4 1 1 1zm1-3.6l10-10L13.6 4l-10 10H2v-1.6z" />
          </svg>
          <div class="italic">{{ order.description }}</div>
        </div>
      </td>
    </tr>
</template>

<script>
import { ref, computed } from 'vue'

export default {
  name: 'OrdersTableItem',
  props: ['order', 'value', 'selected'],
  setup(props, context) {
    const checked = computed(() => props.selected.includes(props.value))

    function check() {
      let updatedSelected = [...props.selected]
      if (checked.value) {
        updatedSelected.splice(updatedSelected.indexOf(props.value), 1)
      } else {
        updatedSelected.push(props.value)
      }
      context.emit('update:selected', updatedSelected)
    }

    const descriptionOpen = ref(false)

    const statusColor = (status) => {
      switch (status) {
        case 'COMPLETED':
          return 'bg-emerald-100 dark:bg-emerald-400/30 text-emerald-600 dark:text-emerald-400'
        case 'IN_PROGRESS':
          return 'bg-blue-100 dark:bg-blue-400/30 text-blue-600 dark:text-blue-400'
        case 'ACCEPTED':
          return 'bg-yellow-100 dark:bg-yellow-400/30 text-yellow-600 dark:text-yellow-400'
        case 'CREATED':
          return 'bg-slate-100 dark:bg-slate-700 text-slate-500 dark:text-slate-400'
        default:
          return 'bg-slate-100 dark:bg-slate-700 text-slate-500 dark:text-slate-400'
      }
    }

    function formatDate(dateString) {
      return dateString ? dateString.replace('T', ' ') : ''
    }

    function formatEstimateTime(seconds) {
      const hrs = Math.floor(seconds / 3600)
      const mins = Math.floor((seconds % 3600) / 60)
      const secs = seconds % 60
      return `${hrs}h ${mins}m ${secs}s`
    }

    return {
      check,
      checked,
      statusColor,
      descriptionOpen,
      formatDate,
      formatEstimateTime,
    }
  },
}
</script>
