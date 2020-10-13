import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Upload from '../views/Upload.vue'
import Main from '../views/Main.vue'

Vue.use(VueRouter)

const requireAuth = () => (to, from, next) =>{
	if (sessionStorage.getItem("userid")){
		return next();
	}
	alert('로그인 해주세요');
	next('/login');
}

const routes = [
  { 
    path: '/',
    name: 'Home',
    component: Home
  },
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
    path: '/login',
    name: 'Login',
    component: Login
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

