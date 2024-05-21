<template>
  <main class="grow">
    <section class="relative">
      <!-- Illustration -->
      <div class="md:block absolute left-1/2 -translate-x-1/2 -mt-36 blur-2xl opacity-70 pointer-events-none -z-10" aria-hidden="true">
        <img src="../images/auth-illustration.svg" class="max-w-none" width="1440" height="450" alt="Page Illustration">
      </div>

      <div class="relative max-w-6xl mx-auto px-4 sm:px-6">
        <div class="pt-32 pb-12 md:pt-40 md:pb-20">
          <!-- Page header -->
          <div class="max-w-3xl mx-auto text-center pb-12">
            <!-- Logo -->
            <div class="mb-5">
              <router-link class="inline-flex" to="/">
                <div class="relative flex items-center justify-center w-16 h-16 border border-transparent rounded-2xl shadow-2xl [background:linear-gradient(theme(colors.slate.900),_theme(colors.slate.900))_padding-box,_conic-gradient(theme(colors.slate.400),_theme(colors.slate.700)_25%,_theme(colors.slate.700)_75%,_theme(colors.slate.400)_100%)_border-box] before:absolute before:inset-0 before:bg-slate-800/30 before:rounded-2xl">
                  <img class="relative" src="../images/logo.svg" width="42" height="42" alt="Stellar">
                </div>
              </router-link>
            </div>
            <!-- Page title -->
            <h1 class="h2 bg-clip-text text-transparent bg-gradient-to-r from-slate-200/60 via-slate-200 to-slate-200/60">Sign in to your account</h1>
          </div>

          <!-- Form -->
          <div class="max-w-sm mx-auto">
            <form @submit.prevent="handleLogin">
              <div class="space-y-4">
                <!-- Email input -->
                <div>
                  <label class="block text-sm font-medium mb-1" for="email">Email Address</label>
                  <input id="email" ref="email" class="form-input w-full" type="email" required />
                </div>

                <!-- Password input -->
                <div>
                  <label class="block text-sm font-medium mb-1" for="password">Password</label>
                  <input id="password" ref="password" class="form-input w-full" type="password" required autoComplete="on" />
                </div>

                <!-- Divider -->
                <div class="flex items-center my-6">
                  <div class="border-t border-slate-800 grow mr-3" aria-hidden="true"></div>
                  <div class="text-sm text-slate-500 italic">
                    <router-link class="text-sm font-medium text-purple-500 hover:text-purple-400 transition duration-150 ease-in-out ml-2" to="/reset-password">Forgot?</router-link>
                  </div>
                  <div class="border-t border-slate-800 grow ml-3" aria-hidden="true"></div>
                </div>

                <!-- Captcha and Forgot password -->
                <div class="flex items-center">
                  <img :src="captchaUrl" @click="refreshCaptcha" alt="Captcha" class="cursor-pointer mr-2 h-12" /> <!-- 点击图片刷新验证码，调整图像高度 -->
                  <input type="text" placeholder="Enter Captcha" v-model="captcha" class="form-input" required />
                </div>

                <!-- Sign In button -->
                <div class="mt-4">
                  <button type="submit" class="btn bg-indigo-500 hover:bg-indigo-600 text-white w-full">Sign In</button>
                </div>

                <!-- Footer -->
                <div class="pt-5 mt-6 border-t border-slate-200 dark:border-slate-700">
                  <div class="flex items-center justify-between text-sm">
                    <span>Don’t you have an account?</span>
                    <router-link class="font-medium text-indigo-500 hover:text-indigo-600 dark:hover:text-indigo-400" to="/signup">Sign Up</router-link>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Signin',
  data() {
    return {
      captchaUrl: '/api/captcha',
      captcha: '',
    };
  },
  methods: {
    handleLogin() {
      const email = this.$refs.email.value;
      const password = this.$refs.password.value;
      axios.post('/api/login', { email, password, captcha: this.captcha })
        .then(response => {
          if (response.data.success) {
            window.location.href = response.data.redirect_url;
          } else {
            alert(response.data.error || 'Login failed!');
          }
        })
        .catch(error => {
          console.error('Error during login:', error);
          alert('Login failed!');
        });
    },
    refreshCaptcha() {
      this.captchaUrl = '/api/captcha?' + Date.now();  // 刷新验证码
    }
  }
}
</script>
