<template>
  <div class="flex justify-center">
    <nav class="flex" role="navigation" aria-label="Navigation">
      <div class="mr-2">
        <span
          class="inline-flex items-center justify-center rounded leading-5 px-2.5 py-2 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-300 dark:text-slate-600"
          :class="{ 'cursor-pointer': page > 1 }"
          @click="changePage(page - 1)"
        >
          <span class="sr-only">Previous</span><wbr />
          <svg class="h-4 w-4 fill-current" viewBox="0 0 16 16">
            <path d="M9.4 13.4l1.4-1.4-4-4 4-4-1.4-1.4L4 8z" />
          </svg>
        </span>
      </div>
      <ul class="inline-flex text-sm font-medium -space-x-px shadow-sm">
        <li v-for="n in totalPages" :key="n">
          <span
            v-if="n === page"
            class="inline-flex items-center justify-center leading-5 px-3.5 py-2 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-indigo-500"
          >
            {{ n }}
          </span>
          <a
            v-else
            class="inline-flex items-center justify-center leading-5 px-3.5 py-2 bg-white dark:bg-slate-800 hover:bg-indigo-500 dark:hover:bg-indigo-500 border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:text-white cursor-pointer"
            @click.prevent="changePage(n)"
          >
            {{ n }}
          </a>
        </li>
      </ul>
      <div class="ml-2">
        <span
          class="inline-flex items-center justify-center rounded leading-5 px-2.5 py-2 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-300 dark:text-slate-600"
          :class="{ 'cursor-pointer': page < totalPages }"
          @click="changePage(page + 1)"
        >
          <span class="sr-only">Next</span><wbr />
          <svg class="h-4 w-4 fill-current" viewBox="0 0 16 16">
            <path d="M6.6 13.4L5.2 12l4-4-4-4 1.4-1.4L12 8z" />
          </svg>
        </span>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'PaginationNumeric',
  props: {
    page: {
      type: Number,
      default: 1
    },
    total: {
      type: Number,
      default: 0
    },
    perPage: {
      type: Number,
      default: 10
    }
  },
  computed: {
    totalPages() {
      return Math.ceil(this.total / this.perPage)
    }
  },
  methods: {
    changePage(newPage) {
      if (newPage > 0 && newPage <= this.totalPages) {
        this.$emit('change-page', newPage)
      }
    }
  }
}
</script>
