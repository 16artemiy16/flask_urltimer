import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import StatsList from '@/views/stats-list.vue';
import StatsItem from '@/views/stats-item.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    component: StatsList,
  },
  {
    path: '/:id',
    component: StatsItem,
  }
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
