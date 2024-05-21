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
          <button @click="handleRowClick"
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
    <!-- Realtime Modal -->
    <ShowRealTimeModal v-if="showRealtimeModal" @close-modal="showRealtimeModal = false" :order="order" />

</template>

<script>
import { ref, computed } from 'vue';
import ShowRealTimeModal from "../actions/ShowRealTimeModal.vue";

export default {
  name: 'OrdersTableItem',
  components: {
    ShowRealTimeModal,
  },
  props: ['order', 'value', 'selected'],
  setup(props, context) {
    const checked = computed(() => props.selected.includes(props.value));

    function check() {
      let updatedSelected = [...props.selected];
      if (checked.value) {
        updatedSelected.splice(updatedSelected.indexOf(props.value), 1);
      } else {
        updatedSelected.push(props.value);
      }
      context.emit('update:selected', updatedSelected);
    }

    const descriptionOpen = ref(false);
    const showRealtimeModal = ref(false);

    function handleRowClick() {
      showRealtimeModal.value = true;
    }

    const statusColor = (status) => {
      switch (status) {
        case 'COMPLETED':
          return 'bg-emerald-100 dark:bg-emerald-400/30 text-emerald-600 dark:text-emerald-400';
        case 'IN_PROGRESS':
          return 'bg-blue-100 dark:bg-blue-400/30 text-blue-600 dark:text-blue-400';
        case 'ACCEPTED':
          return 'bg-yellow-100 dark:bg-yellow-400/30 text-yellow-600 dark:text-yellow-400';
        case 'CREATED':
          return 'bg-slate-100 dark:bg-slate-700 text-slate-500 dark:text-slate-400';
        default:
          return 'bg-slate-100 dark:bg-slate-700 text-slate-500 dark:text-slate-400';
      }
    };

    function formatDate(dateString) {
      return dateString ? dateString.replace('T', ' ') : '';
    }

    function formatEstimateTime(seconds) {
      const hrs = Math.floor(seconds / 3600);
      const mins = Math.floor((seconds % 3600) / 60);
      const secs = seconds % 60;
      return `${hrs}h ${mins}m ${secs}s`;
    }

    return {
      check,
      checked,
      statusColor,
      descriptionOpen,
      formatDate,
      formatEstimateTime,
      showRealtimeModal,
      handleRowClick,
    };
  },
};
</script>
