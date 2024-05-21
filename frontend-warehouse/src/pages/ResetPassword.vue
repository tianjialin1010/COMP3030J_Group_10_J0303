<template>
  <main class="bg-white dark:bg-slate-900">
    <div class="relative flex">
      <!-- Content -->
      <div class="w-full md:w-1/2">
        <div class="min-h-[100dvh] h-full flex flex-col after:flex-1">
          <div class="flex-1">
            <div class="flex items-center justify-between h-16 px-4 sm:px-6 lg:px-8">
              <!-- Logo -->
              <router-link class="block" to="/">
                <!-- SVG Logo here -->
              </router-link>
            </div>
          </div>
          <div class="max-w-sm mx-auto w-full px-4 py-8">
            <h1 class="text-3xl text-slate-800 dark:text-slate-100 font-bold mb-6">Reset your Password ✨</h1>
            <!-- Form -->
            <form @submit.prevent="handleResetPassword">
              <div class="space-y-4">
                <div>
                  <label class="block text-sm font-medium mb-1" for="email">Email Address <span class="text-rose-500">*</span></label>
                  <input v-model="email" id="email" class="form-input w-full" type="email" required />
                </div>
                <div>
                  <label class="block text-sm font-medium mb-1" for="newPassword">New Password <span class="text-rose-500">*</span></label>
                  <input v-model="newPassword" id="newPassword" class="form-input w-full" type="password" required />
                </div>
              </div>
              <div class="flex justify-end mt-6">
                <button type="submit" class="btn bg-indigo-500 hover:bg-indigo-600 text-white whitespace-nowrap">Reset Password</button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <!-- Image Section -->
      <!-- Image -->
      <div class="hidden md:block absolute top-0 bottom-0 right-0 md:w-1/2" aria-hidden="true">
        <img class="object-cover object-center w-full h-full" src="../images/auth-image.jpg" width="760" height="1024" alt="Authentication" />
        <img class="absolute top-1/4 left-0 -translate-x-1/2 ml-8 hidden lg:block" src="../images/auth-decoration.png" width="218" height="224" alt="Authentication decoration" />
      </div>

    </div>
  </main>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      email: '',
      newPassword: ''
    };
  },
  methods: {
    handleResetPassword() {
      axios.post('/api/reset-password', {
        email: this.email,
        new_password: this.newPassword
      }).then(response => {
        alert('Password reset successfully.');
      }).catch(error => {
        alert('Error: ' + error.response.data.error);
      });
    }
  }
}
</script>
