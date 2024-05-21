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
            <h1 class="h2 bg-clip-text text-transparent bg-gradient-to-r from-slate-200/60 via-slate-200 to-slate-200/60">Create your free account</h1>
          </div>

          <!-- Form -->
          <div class="max-w-sm mx-auto">
            <form @submit.prevent="handleRegister">
              <div class="space-y-4">
                <div>
                  <label class="block text-sm text-slate-300 font-medium mb-1" for="email">Email Address <span class="text-rose-500">*</span></label>
                  <input id="email" ref="email" class="form-input w-full" type="email" required />
                </div>
                <div>
                  <label class="block text-sm text-slate-300 font-medium mb-1" for="name">Full Name <span class="text-rose-500">*</span></label>
                  <input id="name" ref="name" class="form-input w-full" type="text" required />
                </div>
                <div>
                  <label class="block text-sm text-slate-300 font-medium mb-1" for="role">Your department <span class="text-rose-500">*</span></label>
                  <select id="role" ref="role" class="form-select text-sm py-2 w-full" required>
                    <option>driver</option>
                    <option>warehouse</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm text-slate-300 font-medium mb-1" for="password">Password <span class="text-rose-500">*</span></label>
                  <input id="password" ref="password" class="form-input w-full" type="password" autocomplete="on" required />
                </div>
              </div>
              <div class="mt-6">
                <button type="submit" class="btn text-sm text-white bg-purple-500 hover:bg-purple-600 w-full shadow-sm group">
                  Sign Up <span class="tracking-normal text-purple-300 group-hover:translate-x-0.5 transition-transform duration-150 ease-in-out ml-1">-&gt;</span>
                </button>
              </div>
            </form>

            <div class="text-center mt-4">
              <div class="text-sm text-slate-400">
                Already have an account? <router-link class="font-medium text-purple-500 hover:text-purple-400 transition duration-150 ease-in-out" to="/signin">Sign in</router-link>
              </div>
            </div>

          </div>

        </div>
      </div>

    </section>

  </main>
</template>


<script>
import axios from 'axios';

export default {
  name: 'Signup',
  methods: {
    handleRegister() {
      //调试代码，用于确认函数被调用
      console.log("Register button clicked");

      const email = this.$refs.email.value;
      const name = this.$refs.name.value;
      const role = this.$refs.role.value.toUpperCase();  // 转换为大写
      const password = this.$refs.password.value;

      // 简单的邮箱验证正则表达式
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(email)) {
        alert('Please enter a valid email address.');
        return;
      }

      if (password.length < 6) {
        alert('Password must be at least 6 characters long.');
        return;
      }

      axios.post('/api/register', { email: email, name: name, role: role, password: password })
        .then(response => {
          if (response.data.success) {
            this.$router.push('/SignIn');
          } else {
            alert('Registration failed: ' + response.data.error);
          }
        })
        .catch(error => {
          console.error('Error during registration:', error);
          alert('Registration failed');
        });
    }
  }
}
</script>

