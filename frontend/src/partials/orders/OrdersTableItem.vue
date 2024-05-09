<template>
  <tbody class="text-sm">
    <!-- Row -->
    <tr>
<!--   选项   -->
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap w-px">
        <div class="flex items-center">
          <label class="inline-flex">
            <span class="sr-only">Select</span>
            <input :id="order.id" class="form-checkbox" type="checkbox" :value="value" @change="check" :checked="checked" />
          </label>
        </div>
      </td>

      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div>{{order.id}}</div>
      </td>
      <td class="px-2 first:pl-5 Flast:pr-5 py-3 whitespace-nowrap">
        <div class="text-left font-medium text-emerald-500">{{order.initiator_user_id}}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-center">{{order.assigned_driver_id}}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="inline-flex font-medium rounded-full text-center px-2.5 py-0.5" :class="statusColor(order.status)">{{order.status}}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-left">{{order.destination}}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-left">{{order.mileage}}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-left">{{order.created_at}}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-left">{{order.completed_at}}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-left">{{order.vehicle_type}}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="text-left">{{order.carbon_emission}}</div>
      </td>
       <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="font-medium text-slate-800 dark:text-slate-100">{{order.vehicle_id}}</div>
      </td>
      <td class="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap">
        <div class="font-medium text-slate-800 dark:text-slate-100">{{order.start_location}}</div>
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
      <td colspan="10" class="px-2 first:pl-5 last:pr-5 py-3">
        <div class="flex items-center bg-slate-50 dark:bg-slate-900/30 dark:text-slate-400 p-3 -mt-3">
          <svg class="w-4 h-4 shrink-0 fill-current text-slate-400 dark:text-slate-500 mr-2">
            <path d="M1 16h3c.3 0 .5-.1.7-.3l11-11c.4-.4.4-1 0-1.4l-3-3c-.4-.4-1-.4-1.4 0l-11 11c-.2.2-.3.4-.3.7v3c0 .6.4 1 1 1zm1-3.6l10-10L13.6 4l-10 10H2v-1.6z" />
          </svg>
          <div class="italic">{{order.description}}</div>
        </div>
      </td>
    </tr>
  </tbody>
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
      if (this.checked) {
        updatedSelected.splice(updatedSelected.indexOf(props.value), 1)
      } else {
        updatedSelected.push(props.value)
      }
      context.emit('update:selected', updatedSelected)
    }

    const descriptionOpen = ref(false)

    const statusColor = (status) => {
      switch (status) {
        case 'completed':
          return 'bg-emerald-100 dark:bg-emerald-400/30 text-emerald-600 dark:text-emerald-400'
        case 'cancelled':
          return 'bg-amber-100 dark:bg-amber-400/30 text-amber-600 dark:text-amber-400'
        default:
          return 'bg-slate-100 dark:bg-slate-700 text-slate-500 dark:text-slate-400'
      }
    }
    


    return {
      check,
      checked,
      statusColor,

      descriptionOpen,
    }
  },
}
</script>