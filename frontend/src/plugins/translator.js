import { ref, provide, inject } from 'vue';
import axios from 'axios';

const apiKey = 'AIzaSyA09g-Nb2xujhJc0jEsR8iPPqmUbvRqLuw'; // 替换为你的Google API密钥

const useTranslator = () => {
  const currentLanguage = ref('en');

  const translateText = async (text, targetLang) => {
    try {
      const response = await axios.post(`https://translation.googleapis.com/language/translate/v2?key=${apiKey}`, {
        q: text,
        target: targetLang,
      }, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      return response.data.data.translations[0].translatedText;
    } catch (error) {
      console.error('Request URL:', error.config.url);  // 查看请求的URL
      console.error('Error status:', error.response.status);  // 查看错误状态码
      console.error('Error body:', error.response.data);  // 查看响应体中的错误消息
      return text; // 如果翻译失败，返回原文
    }
  };

  const changeLanguage = (lang) => {
    currentLanguage.value = lang;
  };

  provide('translator', {
    currentLanguage,
    translateText,
    changeLanguage,
  });
};

const useTranslate = () => {
  const translator = inject('translator');
  if (!translator) {
    throw new Error('Translator is not provided');
  }
  return translator;
};

export { useTranslator, useTranslate };
