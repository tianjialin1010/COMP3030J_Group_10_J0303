<template>
  <div class="relative bg-indigo-200 dark:bg-indigo-500 p-4 sm:p-6 rounded-sm overflow-hidden mb-8">
    <!-- Background illustration -->
    <div class="absolute right-0 top-0 -mt-4 mr-16 pointer-events-none hidden xl:block" aria-hidden="true">
      <svg width="319" height="198" xmlns:xlink="http://www.w3.org/1999/xlink">
        <defs>
          <path id="welcome-a" d="M64 0l64 128-64-20-64 20z" />
          <path id="welcome-e" d="M40 0l40 80-40-12.5L0 80z" />
          <path id="welcome-g" d="M40 0l40 80-40-12.5L0 80z" />
          <linearGradient x1="50%" y1="0%" x2="50%" y2="100%" id="welcome-b">
            <stop stop-color="#A5B4FC" offset="0%" />
            <stop stop-color="#818CF8" offset="100%" />
          </linearGradient>
          <linearGradient x1="50%" y1="24.537%" x2="50%" y2="100%" id="welcome-c">
            <stop stop-color="#4338CA" offset="0%" />
            <stop stop-color="#6366F1" stop-opacity="0" offset="100%" />
          </linearGradient>
        </defs>
        <g fill="none" fill-rule="evenodd">
          <g transform="rotate(64 36.592 105.604)">
            <mask id="welcome-d" fill="#fff">
              <use xlink:href="#welcome-a" />
            </mask>
            <use fill="url(#welcome-b)" xlink:href="#welcome-a" />
            <path fill="url(#welcome-c)" mask="url(#welcome-d)" d="M64-24h80v152H64z" />
          </g>
          <g transform="rotate(-51 91.324 -105.372)">
            <mask id="welcome-f" fill="#fff">
              <use xlink:href="#welcome-e" />
            </mask>
            <use fill="url(#welcome-b)" xlink:href="#welcome-e" />
            <path fill="url(#welcome-c)" mask="url(#welcome-f)" d="M40.333-15.147h50v95h-50z" />
          </g>
          <g transform="rotate(44 61.546 392.623)">
            <mask id="welcome-h" fill="#fff">
              <use xlink:href="#welcome-g" />
            </mask>
            <use fill="url(#welcome-b)" xlink:href="#welcome-g" />
            <path fill="url(#welcome-c)" mask="url(#welcome-h)" d="M40.333-15.147h50v95h-50z" />
          </g>
        </g>
      </svg>
    </div>

    <!-- Content -->
    <div class="relative p-4 bg-white dark:bg-slate-800">
      <div class="mb-6">
        <p v-if="username" class="text-2xl md:text-3xl text-slate-800 dark:text-slate-100 font-bold mb-1">Good afternoon, {{ username }}. 👋</p>
      </div>
      <div class="weather-section">
        <button class="btn-primary" @click="fetchWeather">Get weather(requires your position)</button>
        <div v-if="weather" class="mb-4">
          <p class="text-lg">
            Today's temperature:
            <span v-if="weather.temp_min === weather.temp_max">{{ weather.temp_min }}°C</span>
            <span v-else>{{ weather.temp_min }}°C - {{ weather.temp_max }}°C</span>
            {{ weather.emoji }}
          </p>
          <p class="text-lg">Weather: {{ weather.description }}</p>
          <p class="text-2xl md:text-3xl text-slate-800 dark:text-slate-100 font-bold mb-4">{{ weather.message }}</p>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'WelcomeBanner',
  data() {
    return {
      weather: null,
      username: ''
    };
  },
  created() {
    this.fetchUserSession();
  },
  methods: {
    fetchUserSession() {
      axios.get('/api/user-session')
        .then(response => {
          if (response.data) {
            this.username = response.data.username;
            localStorage.setItem('username', response.data.username); // Store username in local storage
          }
        })
        .catch(error => {
          console.error('Failed to fetch user session:', error);
        });
    },
    fetchWeather() {
      navigator.geolocation.getCurrentPosition(position => {
        const { latitude, longitude } = position.coords;
        this.getWeather(latitude, longitude);
      }, error => {
        console.error(error);
      });
    },
    getWeather(lat, lon) {
      axios.get(`/api/weather?lat=${lat}&lon=${lon}`)
        .then(response => {
          const data = response.data;
          this.weather = {
            temp_min: data.temp_min,
            temp_max: data.temp_max,
            description: data.description,
            ...this.getWeatherDetails(data.description)
          };
        })
        .catch(error => {
          console.error('Failed to fetch weather:', error);
        });
    },
    getWeatherDetails(description) {
      const weatherConditions = {
        clear: {
          emoji: '☀️',
          message: "It's a sunny day! Don't forget your sunglasses! 😎"
        },
        clouds: {
          emoji: '☁️',
          message: "It's a bit cloudy today. A perfect day for a walk! 🌥️"
        },
        rain: {
          emoji: '🌧️',
          message: "Don't forget your umbrella! 🌧️ And watch out for slippery roads! 🚶‍♂️💦"
        },
        snow: {
          emoji: '❄️',
          message: "It's snowing! Stay warm and drive safely! ❄️🚗"
        },
        thunderstorm: {
          emoji: '⛈️',
          message: "There's a thunderstorm. Stay indoors and stay safe! ⚡🏠"
        },
        default: {
          emoji: '🌡️',
          message: "Have a great day, regardless of the weather! 😊"
        }
      };

      for (const [key, value] of Object.entries(weatherConditions)) {
        if (description.includes(key)) {
          return value;
        }
      }

      return weatherConditions.default;
    }
  }
}
</script>

<style scoped>
.btn-primary {
  background-color: #4f46e5; /* Indigo */
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-primary:hover {
  background-color: #4338ca; /* Darker Indigo */
}

.weather-section p {
  margin-bottom: 0.5rem;
}

.weather-section .text-lg {
  font-size: 1.125rem; /* 18px */
  line-height: 1.75rem; /* 28px */
}
</style>
