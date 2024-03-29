// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path:'/',
    redirect: '/catalog'
  },
  {
    path: '/catalog',
    component: () => import('@/layouts/default/View.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (Home-[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import('@/views/Home.vue'),
      },      
      {
        path: '/catalog/:productId',
        name: 'ProductDetail',
        // route level code-splitting
        // this generates a separate chunk (Home-[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import('@/views/ProductDetail.vue'),
      },      
    ],
  },
  {
    path: '/cart',
    name: 'Cart',
    component: () => import('@/views/Cart.vue'),    
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
