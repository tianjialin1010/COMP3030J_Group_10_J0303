import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import store from './store';  // 引入 store

import 'aos/dist/aos.css';
import './css/style.css'

const app = createApp(App)
app.use(router)
app.use(store);  // 使用 store
app.mount('#app')
