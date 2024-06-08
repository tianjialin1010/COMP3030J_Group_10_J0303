<template>
  <section class="relative">
    <!-- Radial gradient -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none -z-10" aria-hidden="true">
      <div class="absolute flex items-center justify-center top-0 -translate-y-1/2 left-1/2 -translate-x-1/2 w-1/3 aspect-square">
        <div class="absolute inset-0 translate-z-0 bg-purple-500 rounded-full blur-[120px] opacity-50"></div>
      </div>
    </div>
    <div class="max-w-6xl mx-auto px-4 sm:px-6">
      <div class="py-12 md:py-20">
        <!-- Content -->
        <div class="max-w-3xl mx-auto text-center pb-12 md:pb-20">
          <h2 class="h2 bg-clip-text text-transparent bg-gradient-to-r from-slate-200/60 via-slate-200 to-slate-200/60 pb-4">We are a happy, small team</h2>
          <p class="text-lg text-slate-400">We are a small but close-knit team, bound by our shared passion for innovation.
            While we occasionally clash, we always resolve our differences positively and support each other. Our workplace is filled with laughter and creativity, making it both productive and enjoyable.
            Each team member brings unique talents and humor, contributing to our collective success.
            Together, we strive to build the most intelligent and sustainable logistics management system, believing that as long as we're united, nothing is impossible.</p>
        </div>
        <!-- Team members -->
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-2 sm:gap-6">
          <template v-for="item in items" :key="item.id">
            <div class="relative flex items-center justify-between py-4 pl-4 pr-3 group before:absolute before:inset-0 before:-z-10 before:border before:border-slate-300 before:bg-slate-700 before:opacity-0 hover:before:opacity-10 transition-opacity focus-within:before:opacity-10 before:rounded-xl before:transition-opacity">
              <div class="flex items-center space-x-4">
                <img class="shrink-0" :src="item.img" width="48" height="48" :alt="item.name" />
                <div class="grow">
                  <div class="font-bold text-slate-100 mb-0.5">{{ item.name }}</div>
                  <div class="text-sm text-purple-500 font-medium">{{ item.role }}</div>
                  <div class="text-sm text-purple-500 font-medium">{{ item.id }}</div>
                </div>
              </div>
              <a class="shrink-0 text-slate-500 md:opacity-0 group-hover:opacity-100 focus-within:opacity-100 focus:outline-none group-hover:before:absolute group-hover:before:inset-0" :href="item.twitter" :aria-label="`${item.name}'s Twitter`">
                <svg class="fill-current" xmlns="http://www.w3.org/2000/svg" width="24" height="24">
                  <path d="M11.297 13.807 7.424 18H5.276l5.019-5.436L5 6h4.43l3.06 3.836L16.025 6h2.147l-4.688 5.084L19 18h-4.32l-3.383-4.193Zm3.975 2.975h1.19L8.783 7.155H7.507l7.766 9.627Z" />
                </svg>
              </a>
            </div>
          </template>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Member01 from '../images/team-01.png'
import Member02 from '../images/team-02.png'
import Member03 from '../images/team-03.png'
import Member04 from '../images/team-04.png'
import Member05 from '../images/team-05.png'
import Member06 from '../images/team-06.png'

export default {
  name: 'Team',
  setup() {
    const items = [
      {
        img: Member01,
        name: 'Jialin Tian',
        role: 'Artificial Intelligence Engineer',
        twitter: '#0',
        id: '21207354'
      },
      {
        img: Member02,
        name: 'Zeying Yu',
        role: 'Front-end Engineer',
        twitter: '#0',
        id: '21207293'
      },
      {
        img: Member03,
        name: 'Sizhan Hou',
        role: 'Back-end Engineer and Algorithms',
        twitter: '#0',
        id: '21207348'
      },
      {
        img: Member04,
        name: 'Yichen Zhang',
        role: 'Animator and Test Engineer',
        twitter: '#0',
        id: '21207360'
      },
      {
        img: Member05,
        name: 'Zhenfei Sun',
        role: 'Data Analyst',
        twitter: '#0',
        id: '21207364'
      },
      {
        img: Member06,
        name: 'Juncheng Li',
        role: 'Database Manager',
        twitter: '#0',
        id: '21207443'
      },
    ];

    return {
      items
    }
  }
}
</script>
