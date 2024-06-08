// store/index.js
import { createStore } from 'vuex'

const store = createStore({
  state: {
    user: null,
    isLoggedIn: false,
  },
  getters: {
    isLoggedIn: state => state.isLoggedIn,
  },
  mutations: {
    setUser(state, user) {
      state.user = user
      state.isLoggedIn = true
    },
    clearSession(state) {
      state.user = null
      state.isLoggedIn = false
    }
  },
  actions: {
    login({ commit }, user) {
      commit('setUser', user)
    },
    logout({ commit }) {
      commit('clearSession')
    }
  }
})

export default store
