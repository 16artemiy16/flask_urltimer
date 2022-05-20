import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import StatsList from '@/views/stats-list.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    component: StatsList,
  }
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
