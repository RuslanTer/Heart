import Vue from 'vue'
import VueRouter from 'vue-router'

const Index = () => import('@/views/Test').then(m => m.default || m)
const Home = () => import('@/views/Home').then(m => m.default || m)
const NewPatient = () => import('@/views/NewPatient').then(m => m.default || m)


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Test',
    component: Index,
    redirect: 'home',
    children: [
      {
        path: '/home',
        name: 'home',
        component: Home,
      },
      {
        path: '/new_patient',
        name: 'NewPatient',
        component: NewPatient,
      }
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
