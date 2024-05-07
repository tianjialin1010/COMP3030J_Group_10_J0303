<template>
  <div :class="selectedItems.length < 1 && 'hidden'">
    <div class="flex items-center">
      <div class="hidden xl:block text-sm italic mr-2 whitespace-nowrap"><span>{{ selectedItems.length }}</span> items selected</div>
      <button @click="confirmDeletion" class="btn bg-white dark:bg-slate-800 border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600 text-rose-500">Delete</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'DeleteButton',
  props: ['selectedItems'],
  methods: {
    confirmDeletion() {
      if (confirm(`Are you sure you want to delete these ${this.selectedItems.length} items?`)) {
        this.deleteItems();
        this.$router.push('/ecommerce/customers');
      }
    },
    deleteItems() {
      axios.post('/api/delete-items', { items: this.selectedItems })
        .then(() => {
          alert('Items deleted successfully.');

        })
        .catch(error => {
          alert('Failed to delete items: ' + error.message);
        });
    }
  }
}
</script>
