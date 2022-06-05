import { createApp } from 'vue'
import 'font-awesome/scss/font-awesome.scss';
import App from './App.vue'
import router from './router'
import AppSortingBtn from '@/components/app/app-sorting-btn.vue';

createApp(App)
  .use(router)
  .component('AppSortingBtn', AppSortingBtn)
  .mount('#app')
