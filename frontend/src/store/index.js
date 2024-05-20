// src/store/index.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    language: 'en', // 默认语言
  },
  mutations: {
    setLanguage(state, lang) {
      state.language = lang;
    },
  },
  actions: {
    changeLanguage({ commit }, lang) {
      commit('setLanguage', lang);
    },
  },
  getters: {
    currentLanguage: (state) => state.language,
  },
});
