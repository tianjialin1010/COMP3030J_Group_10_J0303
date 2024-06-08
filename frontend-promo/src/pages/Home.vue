<template>
  <div className="flex flex-col min-h-screen overflow-hidden supports-[overflow:clip]:overflow-clip">

    <!-- Site header -->
    <Header />

    <!-- Page content -->
    <main class="grow">

      <Hero />
      <Clients />
      <Features />
      <Features03 />
      <Story />
      <Team />
      <Testimonials />
      <Cta />

    </main>
    
    <!-- Site footer -->
    <Footer />    

  </div>
</template>

<script>
import Clients from '../partials/Clients.vue'
import Features from '../partials/Features.vue'
import Features02 from '../partials/Features02.vue'
import Features03 from '../partials/Features03.vue'
import TestimonialsCarousel from '../partials/TestimonialsCarousel.vue'
import Features04 from '../partials/Features04.vue'
import Testimonials from '../partials/Testimonials.vue'
import Header from '../partials/Header.vue'
import Hero from '../partials/HeroAbout.vue'
import Story from '../partials/Story.vue'
import Team from '../partials/Team.vue'
import Recruitment from '../partials/Recruitment.vue'
import Cta from '../partials/Cta02.vue'
import Footer from '../partials/Footer.vue'

export default {
  name: 'Home',
  components: {
    Team, Story, Recruitment,
    Header,
    Hero,
    Clients,
    Features,
    Features02,
    Features03,
    TestimonialsCarousel,
    Features04,
    Testimonials,
    Cta,
    Footer,
  },
}
</script>