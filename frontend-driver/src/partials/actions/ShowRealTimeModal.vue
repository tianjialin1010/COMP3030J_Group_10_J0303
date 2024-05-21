<template>
  <div class="p-6">
    <h1 class="text-xl font-bold mb-4"></h1>

    <ModalBasic :modalOpen="modalOpen" @close-modal="modalOpen = false">
      <!-- Google Map Component -->
      <ShowRealTimeRoad
        @map-loaded="handleMapLoaded"
        :origin="order.origin"
        :destination="order.destination"
      />
      <!-- Modal Content -->
      <div class="px-5 py-4">
        <div class="text-sm">
          <div class="font-medium text-slate-800 dark:text-slate-100 mb-3">View Order</div>
          <div class="space-y-3">
            <button class="btn-sm border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600 text-slate-600 dark:text-slate-300" @click="modalOpen = false; $emit('close-modal')">Cancel</button>


          </div>
        </div>
      </div>
    </ModalBasic>
  </div>
</template>

<script>
import ModalBasic from '../../components/ModalBasic.vue';
import ShowRealTimeRoad from '../../pages/ShowRealTimeRoad.vue';

export default {
  name: 'ShowRealTimeModal',
  components: {
    ShowRealTimeRoad,
    ModalBasic,
  },
  props: {
    order: Object
  },
  data() {
    return {
      modalOpen: true,
    };
  },
  methods: {
    handleMapLoaded() {
      console.log('Map loaded');
    }
  }
}
</script>
