import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import Stats from '@/views/stats-page.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    component: Stats,
  }
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
