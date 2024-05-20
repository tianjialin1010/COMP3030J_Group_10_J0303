<template>
  <div class="flex h-[50vh] overflow-hidden">
    <!-- Main Content area -->
    <main class="grow">
      <div id="mapElement" ref="mapElement" style="height: 100%; width: 100%;"></div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, toRefs } from 'vue'
import { defineProps } from 'vue'

const { origin, destination } = defineProps({
  origin: {
    type: Object,
    required: true
  },
  destination: {
    type: Object,
    required: true
  }
})

const mapElement = ref(null);

onMounted(() => {
  if (!window.google || !window.google.maps) {
    loadGoogleMapsScript().then(() => {
      initializeMap();
    }).catch(error => {
      console.error("Google Maps failed to load", error);
    });
  } else {
    initializeMap();
  }
});

function loadGoogleMapsScript() {
  return new Promise((resolve, reject) => {
    const script = document.createElement('script');
    script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyA09g-Nb2xujhJc0jEsR8iPPqmUbvRqLuw&v=weekly&language=en";
    script.async = true;
    script.defer = true;
    script.onload = resolve;
    script.onerror = reject;
    document.head.appendChild(script);
  });
}

function initializeMap() {
  const map = new window.google.maps.Map(mapElement.value, {
    center: { lat: (origin.lat + destination.lat) / 2, lng: (origin.lng + destination.lng) / 2 },
    zoom: 7,
  });

  const directionsService = new google.maps.DirectionsService();
  const directionsRenderer = new google.maps.DirectionsRenderer({ map: map });

  calculateRoute(directionsService, directionsRenderer, map);
}

function calculateRoute(directionsService, directionsRenderer, map) {
  const request = {
    origin: origin,
    destination: destination,
    travelMode: google.maps.TravelMode.DRIVING,
  };

  directionsService.route(request, (response, status) => {
    if (status === 'OK') {
      directionsRenderer.setDirections(response);
      animateMarker(map, response.routes[0], origin, destination);
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });
}

function animateMarker(map, route, origin, destination) {
  const path = route.overview_path;
  const stoppingPointIndex = Math.floor(path.length / 3);
  let carIconPath;

  if (origin.lat > destination.lat) {
    carIconPath = '/car1.jpg';
  } else {
    carIconPath = '/car2.jpg';
  }

  const marker = new google.maps.Marker({
    map: map,
    icon: carIconPath,
  });

  let step = 0;
  const intervalId = setInterval(() => {
    if (step <= stoppingPointIndex) {
      marker.setPosition(path[step]);
      step++;
    } else {
      clearInterval(intervalId);
      const remainingDistance = (route.legs[0].distance.value * (1 - 1/3) / 1000).toFixed(2) + " km";
      const remainingDuration = (route.legs[0].duration.value * (1 - 1/3) / 60).toFixed(0) + " minutes";
      infoPanel.value.innerHTML = `<strong>Remaining Distance:</strong> ${remainingDistance} <br><strong>Remaining Duration:</strong> ${remainingDuration}`;
    }
  }, 100);
}
</script>

<script>
import Sidebar from '../partials/Sidebar.vue'
import Header from '../partials/Header.vue'
export default {
  name: 'Road',
  components: {
    Sidebar,
    Header
  },
  setup() {
    return {
      sidebarOpen
    }
  }
}
</script>

<style>
html, body, #map {
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
}

#infoPanel {
  position: absolute;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(255, 255, 255, 0.8);
  padding: 10px;
  border-radius: 8px;
  z-index: 1000;
}
</style>
