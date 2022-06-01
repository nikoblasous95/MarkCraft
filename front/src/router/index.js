import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: () => import('@/pages/landing/LandingPage.vue'),
  },
  {
    path: '/storeDetail/:id',
    name: 'storeDetail',
    component: () => import('@/pages/storeDetail/StoreDetailPage.vue'),
  },
  {
    path: '/storeDetail/:id/:id',
    name: 'ItemDetail',
    component: () => import('@/pages/itemDetail/ItemDetailPage.vue'),
  },
  {
    path: '/shopCart',
    name: 'ShopCart',
    component: () => import('@/pages/shopCart/ShopCartPage.vue'),
  },
  {
    path: '/adminLogin',
    name: 'adminLogin',
    component: () => import('@/pages/adminLogin/AdminLoginPage.vue'),
  },
  {
    path: '/adminStore',
    name: 'adminStore',
    component: () => import('@/pages/adminStoreModify/AdminStorePage.vue'),
  },

  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
