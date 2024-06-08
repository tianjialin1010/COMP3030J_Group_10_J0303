<template>
  <section class="relative">

    <!-- Blurred shape -->
    <div class="absolute top-0 -mt-32 left-1/2 -translate-x-1/2 ml-10 blur-2xl opacity-70 pointer-events-none -z-10" aria-hidden="true">
      <svg xmlns="http://www.w3.org/2000/svg" width="434" height="427">
        <defs>
          <linearGradient id="bs4-a" x1="19.609%" x2="50%" y1="14.544%" y2="100%">
            <stop offset="0%" stop-color="#A855F7"></stop>
            <stop offset="100%" stop-color="#6366F1" stop-opacity="0"></stop>
          </linearGradient>
        </defs>
        <path fill="url(#bs4-a)" fill-rule="evenodd" d="m0 0 461 369-284 58z" transform="matrix(1 0 0 -1 0 427)"></path>
      </svg>
    </div>

    <div class="px-4 sm:px-6">
      <div class="max-w-5xl mx-auto">
        <div class="pb-12 md:pb-20">

          <!-- Section header -->
          <div class="max-w-3xl mx-auto text-center pb-12 md:pb-20">
            <h2 class="h2 bg-clip-text text-transparent bg-gradient-to-r from-slate-200/60 via-slate-200 to-slate-200/60">Our story (so far)</h2>
          </div>

          <div class="md:flex justify-between space-x-6 md:space-x-8 lg:space-x-14">
            <figure class="min-w-[240px]">
              <img class="sticky top-8 mx-auto mb-12 md:mb-0 rounded-lg -rotate-[4deg]" src="../images/feature-image-04.png" width="420" height="280" alt="Team" />
            </figure>
            <div class="max-w-[548px] mx-auto">
              <div class="text-slate-400 space-y-6">
                <p>
                  The logistics industry is currently facing significant challenges due to outdated manual processes that lead to inefficiencies and increased operational costs. This proposal outlines a transformative solution that leverages image recognition technology and data visualization tools to create an intelligent logistics management system. The core objectives of this system are to enhance operational efficiency, reduce environmental impact, and provide a sustainable solution for logistics companies.
                </p>
                <p>
                  Our innovative system addresses the critical issues of energy consumption and carbon emissions by optimizing logistics routes and transportation plans. Utilizing algorithms such as Dijkstra and Bellman-Ford, the system identifies the most efficient routes, thereby reducing unnecessary mileage and energy usage. This not only lessens the environmental footprint but also aligns with global efforts to combat climate change.
                </p>
                <p>
                  The integration of image recognition technology streamlines the logistics information recording process by automatically capturing license plate numbers, eliminating manual data entry, and reducing the potential for human error. This automation leads to significant time savings and improved accuracy in tracking shipments.
                </p>
                <p>
                  Furthermore, the system includes a user-friendly data visualization website that presents key performance indicators in an accessible format. This interface empowers decision-makers with real-time insights into their logistics operations, facilitating informed decision-making and process optimization.
                </p>
                <p>
                  The proposed route optimization algorithm considers various factors such as traffic conditions, vehicle types, and cargo capacities to recommend the most efficient routes and cargo capacity selections. This leads to improved resource utilization, reduced empty trips, and enhanced overall logistics efficiency.
                </p>
                <p>
                  The success of this system will be measured by its ability to improve logistics efficiency, reduce energy consumption and carbon emissions, and achieve high customer satisfaction through regular feedback and evaluation. By implementing this intelligent logistics management system, logistics companies can expect a significant leap towards sustainable and efficient operations.
                </p>
                <p>
                  This proposal aims to create an intelligent management system for the logistics industry by introducing image recognition technology and data visualization tools. The system will address inefficiencies in the logistics industry.
                </p>
              </div>
            </div>
          </div>


        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Story',
}
</script>