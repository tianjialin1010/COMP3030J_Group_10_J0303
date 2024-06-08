<template>
  <section>
    <div class="relative max-w-6xl mx-auto px-4 sm:px-6">

      <!-- Particles animation -->
      <div class="absolute inset-0 max-w-6xl mx-auto px-4 sm:px-6">
        <Particles class="absolute inset-0 -z-10" :quantity="5" />
      </div>

      <div class="py-12 md:py-16">
        <div class="overflow-hidden">
          <!-- Carousel built with Swiper.js [https://swiperjs.com/] -->
          <!-- * Custom styles in src/css/additional-styles/theme.scss -->
          <div class="clients-carousel swiper-container relative before:absolute before:inset-0 before:w-32 before:z-10 before:pointer-events-none before:bg-gradient-to-r before:from-slate-900 after:absolute after:inset-0 after:left-auto after:w-32 after:z-10 after:pointer-events-none after:bg-gradient-to-l after:from-slate-900">
            <div class="swiper-wrapper !ease-linear select-none items-center">
              <!-- Carousel items -->
              <div class="swiper-slide !w-auto">
                <div class="client-text">Produced by J0303 Technique Software Company</div>
              </div>
              <div class="swiper-slide !w-auto">
                <div class="client-text">We insight your needs!</div>
              </div>
              <div class="swiper-slide !w-auto">
                <div class="client-text">We satisfy your needs!</div>
              </div>
              <div class="swiper-slide !w-auto">
                <div class="client-text">Building Tomorrow Today</div>
              </div>
              <div class="swiper-slide !w-auto">
                <div class="client-text">Innovation for Growth</div>
              </div>
              <div class="swiper-slide !w-auto">
                <div class="client-text">Your Success, Our Commitment</div>
              </div>
              <div class="swiper-slide !w-auto">
                <div class="client-text">Driving the Future</div>
              </div>
              <div class="swiper-slide !w-auto">
                <div class="client-text">Quality You Can Trust</div>
              </div>
              <div class="swiper-slide !w-auto">
                <div class="client-text">Innovation Meets Excellence</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { onMounted } from 'vue'
import Particles from './Particles.vue'

// Import Swiper
import Swiper, { Autoplay } from 'swiper'
import 'swiper/css'

Swiper.use([Autoplay])

export default {
  name: 'Clients',
  components: {
    Particles
  },
  setup() {
    onMounted(() => {
      const carousel = new Swiper('.clients-carousel', {
        slidesPerView: 'auto',
        spaceBetween: 64,
        centeredSlides: true,
        loop: true,
        speed: 5000,
        noSwiping: true,
        noSwipingClass: 'swiper-slide',
        autoplay: {
          delay: 0,
          disableOnInteraction: true,
        },
      })
    })
  }
}
</script>

<style scoped>
.client-text {
  font-size: 1.25rem;
  color: #fff;
  text-align: center;
  padding: 10px;
}
</style>
