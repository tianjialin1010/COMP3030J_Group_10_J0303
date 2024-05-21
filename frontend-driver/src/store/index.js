// store/index.js
import { createStore } from 'vuex'

export default createStore({
  state: {
    username: '',
    role: ''
  },
  mutations: {
    login(state, { username, role }) {
      state.username = username;
      state.role = role;
    },
    logout(state) {
      state.username = '';
      state.role = '';
    }
  },
  actions: {
    login({ commit }, { username, role }) {
      commit('login', { username, role });
    },
    logout({ commit }) {
      commit('logout');
    }
  },
  getters: {
    isLoggedIn: state => !!state.username,
    userRole: state => state.role
  }
});
