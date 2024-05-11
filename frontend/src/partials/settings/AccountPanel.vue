<template>
  <div class="grow">
    <!-- Panel body -->
    <div class="p-6 space-y-6">
      <h2 class="text-2xl text-slate-800 dark:text-slate-100 font-bold mb-5">My Account</h2>
      <!-- Picture -->
      <section>
        <div class="flex items-center">
          <div class="mr-4">
            <img class="w-20 h-20 rounded-full" src="../../images/user-avatar-80.png" width="80" height="80" alt="User upload" />
          </div>
          <button class="btn-sm bg-indigo-500 hover:bg-indigo-600 text-white">Change</button>
        </div>
      </section>
      <!-- Business Profile -->
      <section>
        <h3 class="text-xl leading-snug text-slate-800 dark:text-slate-100 font-bold mb-1">Profile</h3>
        <div class="text-sm">Fill in more personal information to help us better understand you!</div>
        <div class="sm:flex sm:items-center space-y-4 sm:space-y-0 sm:space-x-4 mt-5">
          <div class="sm:w-1/3">
            <label class="block text-sm font-medium mb-1" for="name">Full Name</label>
            <input id="name" class="form-input w-full" type="text" />
          </div>
        </div>
      </section>
      <!-- Email -->
      <section>
        <h3 class="text-xl leading-snug text-slate-800 dark:text-slate-100 font-bold mb-1">Email</h3>
        <div class="text-sm">Please be sure to contact your supervisor before changing your email address</div>
        <div class="flex flex-wrap mt-5">
          <div class="mr-2">
            <label class="sr-only" for="email">Business email</label>
            <input id="email" class="form-input" type="email" />
          </div>
          <button class="btn border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600 shadow-sm text-indigo-500">Change</button>
        </div>
      </section>
      <!-- Password -->
      <section>
        <h3 class="text-xl leading-snug text-slate-800 dark:text-slate-100 font-bold mb-1">Password</h3>
        <div class="text-sm">You can set a permanent password if you don't want to use temporary login codes.</div>
        <div class="mt-5">
          <button class="btn border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600 shadow-sm text-indigo-500">Set New Password</button>
        </div>
      </section>
      <!-- Smart Sync -->
      <section>
        <h3 ref="syncTitle" class="text-xl leading-snug text-slate-800 dark:text-slate-100 font-bold mb-1">Smart Sync update for Mac</h3>
        <div ref="syncDescription" class="text-sm">With this update, online-only files will no longer appear to take up hard drive space.</div>
      </section>
      <div class="m-1.5">
          <!-- Language Buttons -->
          <div class="flex flex-wrap -space-x-px">
            <button class="btn bg-indigo-600 text-white rounded-none border-l-indigo-400 first:rounded-l last:rounded-r first:border-l-transparent" @click="changeLanguage('zh')">中文</button>
            <button class="btn bg-indigo-500 hover:bg-indigo-600 text-indigo-100 rounded-none border-l-indigo-400 first:rounded-l last:rounded-r first:border-r-transparent" @click="changeLanguage('en')">English</button>
            <button class="btn bg-indigo-500 hover:bg-indigo-600 text-indigo-100 rounded-none border-l-indigo-400 first:rounded-l last:rounded-r first:border-r-transparent" @click="changeLanguage('ga')">Gaeilge</button>
          </div>
      </div>
    </div>
    <!-- Panel footer -->
    <footer>
      <div class="flex flex-col px-6 py-5 border-t border-slate-200 dark:border-slate-700">
        <div class="flex self-end">
          <button class="btn dark:bg-slate-800 border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600 text-slate-600 dark:text-slate-300">Cancel</button>
          <button class="btn bg-indigo-500 hover:bg-indigo-600 text-white ml-3">Save Changes</button>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios';

export default {
  name: 'AccountPanel',
  setup() {
    const sync = ref('Off');
    const syncTitle = ref(null);
    const syncDescription = ref(null);
    const apiKey = 'AIzaSyA09g-Nb2xujhJc0jEsR8iPPqmUbvRqLuw';  // 替换为你的Google API密钥
    const changeLanguage = async (lang) => {
      syncTitle.value.textContent = await translateText(syncTitle.value.textContent, lang);
      syncDescription.value.textContent = await translateText(syncDescription.value.textContent, lang);
    };
    const translateText = async (text, targetLang) => {
      try {
        const response = await axios.post(`https://translation.googleapis.com/language/translate/v2?key=${apiKey}`, {
          q: text,
          target: targetLang
        }, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        return response.data.data.translations[0].translatedText;
      } catch (error) {
        console.error('Request URL:', error.config.url);  // 查看请求的URL
        console.error('Error status:', error.response.status);  // 查看错误状态码
        console.error('Error body:', error.response.data);  // 查看响应体中的错误消息
        return text; // 如果翻译失败，返回原文
      }
    };


    return {
      sync,
      syncTitle,
      syncDescription,
      changeLanguage,
      translateText
    };
  }
}
</script>
