import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import DaysCalendar from '../views/DaysCalendar.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    
    component: () => import( '../views/About.vue')
  }, 
  {
    path: '/reminders',
    name: 'Reminders',
    component: () => import('../views/Reminders.vue')
  },
   {
    path: '/calendar',
    name: 'Calendar',
    component: DaysCalendar
  },
  {
    path: '/recommended',
    name: 'Recommended',
    component: () => import('../views/Recommended.vue')
  },
  {
    path: '/social',
    name: 'Social',
    component: () => import('../views/Social.vue')
  },
  {
    path: '/calculators',
    name: 'Calculators',
    component: () => import('../views/Calculators.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
