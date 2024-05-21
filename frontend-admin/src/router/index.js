import Vue from 'vue'
 import Router from 'vue-router'
 import HelloWorld from '@/components/HelloWorld'
 import Login from '@/views/UserLogin.vue'
 import Main from '@/views/MainComponent.vue'

 Vue.use(Router)

 export default new Router({
  routes: [
   {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
        {
            // Main 页面
            path: '/main',
            name: 'Main',
            component: Main
        },
        {
            // 登陆页面
            path: '/login',
            name: 'Login',
            component: Login
        },
  ]
})