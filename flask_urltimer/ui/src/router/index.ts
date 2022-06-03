import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import PageLayout from '@/components/page-layout/page-layout.vue';
import StatsList from '@/views/stats-list.vue';
import StatsItem from '@/views/stats-item.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    component: PageLayout,
    children: [
      {
        path: '/',
        component: StatsList,
        name: 'statsList',
      },
      {
        path: '/:id',
        component: StatsItem,
      }
    ]
  }
] as RouteRecordRaw[]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
