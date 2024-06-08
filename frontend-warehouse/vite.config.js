import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  base: process.env.NODE_ENV === 'production' ? '/driver/' : '/',
  server: {
    proxy: {
      // 使用 proxy 实例
      '/api': {
        target: 'http://127.0.0.1:5000/',
        changeOrigin: true,
      },
    },
  },
  define: {
    'process.env': process.env
  },
  plugins: [vue()],
  resolve: {
    alias: [
      {
        find: /^~.+/,
        replacement: (val) => {
          return val.replace(/^~/, "");
        },
      },
    ],
  },
  build: {
    commonjsOptions: {
      transformMixedEsModules: true,
    }
  }
})
