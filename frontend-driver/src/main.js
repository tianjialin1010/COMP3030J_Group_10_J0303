// import { createApp } from 'vue'
// import router from './router'
// import App from './App.vue'
//
// import './css/style.css'
//
// const app = createApp(App)
// app.use(router)
// app.mount('#app')

// main.js
// import { createApp } from 'vue';
// import router from './router';
// import App from './App.vue';
// import { useTranslator } from './plugins/translator';
//
// import './css/style.css';
//
// const app = createApp(App);
// app.use(router);
// useTranslator(); // 使用翻译插件
// app.mount('#app');

// main.js
// import { createApp } from 'vue';
// import router from './router';
// import App from './App.vue';
// import { useTranslator } from './plugins/translator';
//
// import './css/style.css';
//
// const app = createApp(App);
// app.use(router);
// useTranslator(); // 使用翻译插件
// app.mount('#app');
// main.js
import { createApp } from 'vue';
import router from './router';
import App from './App.vue';
import TranslatorProvider from './components/TranslatorProvider.vue'; // 导入TranslatorProvider
import store from './store';  // 引入 store

import './css/style.css';

const app = createApp(App);
app.use(router);
app.use(store);  // 使用 store
// 使用TranslatorProvider包裹根组件
app.component('TranslatorProvider', TranslatorProvider);

app.mount('#app');








