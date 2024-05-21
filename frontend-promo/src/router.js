import { createRouter, createWebHistory } from 'vue-router'
import store from './store'
import Home from './pages/Home.vue'
import SignIn from './pages/SignIn.vue'
import SignUp from './pages/SignUp.vue'
import ResetPassword from './pages/ResetPassword.vue'

const routerHistory = createWebHistory()

const router = createRouter({
  scrollBehavior(to) {
    if (to.hash) {
      window.scroll({ top: 0 })
    } else {
      document.querySelector('html').style.scrollBehavior = 'auto'
      window.scroll({ top: 0 })
      document.querySelector('html').style.scrollBehavior = ''
    }
  },  
  history: routerHistory,
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/signin',
      component: SignIn
    },
    {
      path: '/signup',
      component: SignUp
    },    
    {
      path: '/reset-password',
      component: ResetPassword
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.isLoggedIn) {
      next({ path: '/', query: { redirect: to.fullPath } })
    } else {
      const role = store.getters.userRole
      if (to.matched.some(record => record.meta.role && record.meta.role !== role)) {
        next({ path: '/' }) // or redirect to a "not authorized" page
      } else {
        next()
      }
    }
  } else {
    next()
  }
})
export default router
