<template>
  <div class="grow">
    <!-- Panel body -->
    <div class="p-6 space-y-6">
      <h2 class="text-2xl text-slate-800 dark:text-slate-100 font-bold mb-5">{{ translatedTexts.account }}</h2>
      <!-- Picture -->
      <section>
        <div class="flex items-center">
          <div class="mr-4">
            <img class="w-20 h-20 rounded-full" :src="avatarUrl" width="80" height="80" alt="User upload" />
          </div>
          <input type="file" @change="onFileChange" class="hidden" ref="fileInput">
          <button class="btn-sm bg-indigo-500 hover:bg-indigo-600 text-white" @click="triggerFileInput">{{ translatedTexts.change }}</button>
        </div>
      </section>
      <!-- Business Profile -->
      <section>
        <h3 class="text-xl leading-snug text-slate-800 dark:text-slate-100 font-bold mb-1">{{ translatedTexts.profile }}</h3>
        <div class="text-sm">{{ translatedTexts.profileDesc }}</div>
        <div class="sm:flex sm:items-center space-y-4 sm:space-y-0 sm:space-x-4 mt-5">
          <div class="sm:w-1/3">
            <label class="block text-sm font-medium mb-1" for="name">{{ translatedTexts.fullName }}</label>
            <input id="name" v-model="userName" class="form-input w-full" type="text" />
          </div>
        </div>
      </section>
      <!-- Email -->
      <section>
        <h3 class="text-xl leading-snug text-slate-800 dark:text-slate-100 font-bold mb-1">{{ translatedTexts.email }}</h3>
        <div class="text-sm">{{ translatedTexts.emailDesc }}</div>
        <div class="flex flex-wrap mt-5">
          <div class="mr-2">
            <label class="sr-only" for="email">{{ translatedTexts.businessEmail }}</label>
            <input id="email" v-model="userEmail" class="form-input" type="email" />
          </div>
          <button class="btn border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600 shadow-sm text-indigo-500" @click="applyChanges">{{ translatedTexts.change }}</button>
        </div>
      </section>
      <!-- Password -->
      <section>
        <h3 class="text-xl leading-snug text-slate-800 dark:text-slate-100 font-bold mb-1">{{ translatedTexts.password }}</h3>
        <div class="text-sm">{{ translatedTexts.passwordDesc }}</div>
        <div class="mt-5">
          <button class="btn bg-indigo-500 hover:bg-indigo-600 text-white ml-3" @click="navigateToResetPassword">{{ translatedTexts.setNewPassword }}</button>
        </div>
      </section>
      <!-- Smart Sync -->
      <section>
        <h3 ref="syncTitle" class="text-xl leading-snug text-slate-800 dark:text-slate-100 font-bold mb-1">{{ translatedTexts.sync }}</h3>
        <div ref="syncDescription" class="text-sm">{{ translatedTexts.syncDesc }}</div>
      </section>
      <div class="m-1.5">
        <!-- Language Buttons -->
        <div class="flex flex-wrap -space-x-px">
          <button class="btn bg-indigo-600 text-white rounded-none border-l-indigo-400 first:rounded-l last:rounded-r first:border-l-transparent" @click="selectLanguage('zh')">中文</button>
          <button class="btn bg-indigo-500 hover:bg-indigo-600 text-indigo-100 rounded-none border-l-indigo-400 first:rounded-l last:rounded-r first:border-r-transparent" @click="selectLanguage('en')">English</button>
          <button class="btn bg-indigo-500 hover:bg-indigo-600 text-indigo-100 rounded-none border-l-indigo-400 first:rounded-l last:rounded-r first:border-r-transparent" @click="selectLanguage('ga')">Gaeilge</button>
        </div>
      </div>
    </div>
    <!-- Panel footer -->
    <footer>
      <div class="flex flex-col px-6 py-5 border-t border-slate-200 dark:border-slate-700">
        <div class="flex self-end">
          <button class="btn dark:bg-slate-800 border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600 text-slate-600 dark:text-slate-300" @click="cancelChanges">{{ translatedTexts.cancel }}</button>
          <button class="btn bg-indigo-500 hover:bg-indigo-600 text-white ml-3" @click="applyChanges">{{ translatedTexts.save }}</button>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import { ref, watchEffect, onMounted } from 'vue';
import { useTranslate } from '../../plugins/translator';
import axios from 'axios';
import { useRouter } from 'vue-router';


export default {
  name: 'AccountPanel',
  setup() {
    const { currentLanguage, translateText, changeLanguage } = useTranslate();
    const texts = {
      account: 'My Account',
      profile: 'Profile',
      profileDesc: 'Fill in more personal information to help us better understand you!',
      email: 'Email',
      emailDesc: 'Please be sure to contact your supervisor before changing your email address',
      password: 'Password',
      passwordDesc: 'You can set a permanent password if you don\'t want to use temporary login codes.',
      sync: 'Smart Sync update for Mac',
      syncDesc: 'With this update, online-only files will no longer appear to take up hard drive space.',
      change: 'Change',
      cancel: 'Cancel',
      save: 'Save Changes',
      fullName: 'Full Name',
      businessEmail: 'Business email',
      setNewPassword: 'Set New Password'
    };

    const translatedTexts = ref({ ...texts });
    const selectedLanguage = ref(currentLanguage.value);
    const userName = ref('');
    const userEmail = ref('');

    const updateTranslations = async (lang) => {
      for (const key in texts) {
        translatedTexts.value[key] = await translateText(texts[key], lang);
      }
    };

    watchEffect(() => {
      updateTranslations(currentLanguage.value);
    });

    const selectLanguage = (lang) => {
      selectedLanguage.value = lang;
      updateTranslations(lang);
    };

    const avatarUrl = ref('../../images/user-avatar-80.png');  // 默认头像路径

    const fetchUserAvatar = async () => {
      try {
        const response = await axios.get('/api/user-info');
        if (response.data && response.data.avatar_url) {
          avatarUrl.value = response.data.avatar_url;
          userName.value = response.data.username;
          userEmail.value = response.data.email;
        }
      } catch (error) {
        console.error('Error fetching user info:', error);
      }
    };

    onMounted(() => {
      fetchUserAvatar();
    });

    const avatarFile = ref(null);
    const triggerFileInput = () => document.querySelector('input[type="file"]').click();
    const onFileChange = (event) => {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => avatarUrl.value = e.target.result;
        reader.readAsDataURL(file);
        avatarFile.value = file;
      }
    };

    const applyChanges = async () => {
      if (avatarFile.value) {
        const formData = new FormData();
        formData.append('avatar', avatarFile.value);
        try {
          const response = await axios.post('/api/upload-avatar', formData, {
            headers: { 'Content-Type': 'multipart/form-data' }
          });
          avatarUrl.value = response.data.avatar_url;
        } catch (error) {
          console.error('Error uploading avatar:', error);
        }
      }
      // Save username and email changes
      try {
        await axios.post('/api/update-user-info', { username: userName.value, email: userEmail.value });
      } catch (error) {
        console.error('Error updating user info:', error);
      }
      changeLanguage(selectedLanguage.value);
    };

    const router = useRouter();

    const navigateToResetPassword = () => {
      router.push('/reset-password');
    };
    const cancelChanges = () => updateTranslations(currentLanguage.value);

    return {
      translatedTexts,
      selectLanguage,
      applyChanges,
      cancelChanges,
      avatarUrl,
      triggerFileInput,
      onFileChange,
      userName,
      userEmail,
      navigateToResetPassword
    };

  }
}
</script>
