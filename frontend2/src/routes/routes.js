import DashboardLayout from '@/views/Layout/DashboardLayout.vue';
import ViewerLayout from '@/views/Layout/ViewerLayout.vue';
import AuthLayout from '@/views/Pages/AuthLayout.vue';

import NotFound from '@/views/NotFoundPage.vue';

const routes = [
  {
    path: '/',
    redirect: 'login',
    component: DashboardLayout,
    children: [
      {
        path: '/dashboard/:username',
        name: 'dashboard',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "demo" */'../views/Dashboard.vue')
      },

      {
        path: '/profile/:username',
        name: 'profile',
        component: () => import(/* webpackChunkName: "demo" */ '../views/Pages/UserProfile.vue')
      },
      {
        path: '/documents/:username',
        name: 'documents',
        component: () => import(/* webpackChunkName: "demo" */ '../views/Documents.vue')
      }

    ]
  },
  {
    path: '/viewer',
    redirect: 'viewer',
    component: ViewerLayout,
    children: [
    
      {
        path: '/viewer/:username',
        name: 'viewer',
        component: () => import(/* webpackChunkName: "demo" */ '../views/Viewer.vue')
      }

    ]
  },


  {
    path: '/',
    redirect: 'login',
    component: AuthLayout,
    children: [
      {
        path: '/login',
        name: 'login',
        component: () => import(/* webpackChunkName: "demo" */ '../views/Pages/Login.vue')
      },
      {
        path: '/register',
        name: 'register',
        component: () => import(/* webpackChunkName: "demo" */ '../views/Pages/Register.vue')
      },
      { path: '*', component: NotFound }

    ]
  }
];

export default routes;
