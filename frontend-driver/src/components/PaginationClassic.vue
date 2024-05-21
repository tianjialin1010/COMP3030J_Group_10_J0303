<template>
  <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between">
    <nav class="mb-4 sm:mb-0 sm:order-1" role="navigation" aria-label="Navigation">
      <ul class="flex justify-center">
        <li class="ml-3 first:ml-0" @click="changePage(page - 1)" :class="{ 'cursor-pointer': page > 1, 'text-gray-300': page <= 1 }">
          <span :class="{'btn': true, 'bg-white': true, 'dark:bg-slate-800': true, 'border-slate-200': true, 'dark:border-slate-700': true, 'text-slate-300': page <= 1, 'dark:text-slate-600': page <= 1}">&lt;- Previous</span>
        </li>
        <li class="ml-3 first:ml-0" @click="changePage(page + 1)" :class="{ 'cursor-pointer': page * perPage < total, 'text-gray-300': page * perPage >= total }">
          <span :class="{'btn': true, 'bg-white': true, 'dark:bg-slate-800': true, 'border-slate-200': true, 'dark:border-slate-700': true, 'text-slate-300': page * perPage >= total, 'dark:text-slate-600': page * perPage >= total, 'text-indigo-500': page * perPage < total}">Next -&gt;</span>
        </li>
      </ul>
    </nav>
    <div class="text-sm text-slate-500 dark:text-slate-400 text-center sm:text-left">
      Showing <span class="font-medium text-slate-600 dark:text-slate-300">{{ Math.min((page - 1) * perPage + 1, total) }}</span> to <span class="font-medium text-slate-600 dark:text-slate-300">{{ Math.min(page * perPage, total) }}</span> of <span class="font-medium text-slate-600 dark:text-slate-300">{{ total }}</span> results
    </div>
  </div>
</template>

<script>
export default {
  name: 'PaginationClassic',
  props: {
    page: {
      type: Number,
      default: 1
    },
    perPage: {
      type: Number,
      default: 10
    },
    total: {
      type: Number,
      default: 0
    }
  },
  methods: {
    changePage(newPage) {
      if (newPage > 0 && newPage <= Math.ceil(this.total / this.perPage)) {
        this.$emit('change-page', newPage)
      }
    }
  }
}
</script>
