import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import DaysCalendar from '../views/DaysCalendar.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/calendar',
    name: 'Calendar',
    component: DaysCalendar
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/reminders',
    name: 'Reminders',
    component: () => import('../views/Reminders.vue')
  },
  {
    path: '/recommended',
    name: 'Recommended',
    component: () => import('../views/Recommended.vue')
  },  
  {
    path: '/social',
    name: 'Soical',
    component: () => import('../views/Social.vue')
  },
  {
    path: '/calculators',
    name: 'Calculators',
    component: () => import('../views/Calculators.vue')
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
