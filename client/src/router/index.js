import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
// import Login from '../views/Login.vue'
import Upload from '../views/Upload.vue'
import Recent from '../views/Recent.vue'
import Main from '../views/Main.vue'
import Profile from '../views/Profile.vue'
import Dashboard from '../views/Dashboard.vue'

Vue.use(VueRouter)

const requireAuth = () => (to, from, next) =>{
	if (sessionStorage.getItem("userid")){
		return next();
	}
	alert('잘못된 접근입니다. 로그인 해주세요');
	next('/login');
}

const routes = [
  { 
    path: '/',
    name: 'Home',
    component: Home
  },
  {
	path : '/dashboard',
	name : 'Dashboard',
	component : Dashboard,
	children : [
		{ // 로그인해야들어갈수있음
			path: '/upload',
			name: 'Upload',
			component: Upload,
			beforeEnter : requireAuth()
		},
		{ 
			path: '/main',
			name: 'Main',
			component: Main
		},
		{ 
			path: '/recent',
			name: 'Recent',
			component: Recent
		},
		{
			path : '/profile',
			name : 'Profile',
			component : Profile,
			beforeEnter : requireAuth()
		}
	],
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

