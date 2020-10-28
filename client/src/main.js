import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.use(BootstrapVue)

Vue.config.productionTip = false
Vue.prototype.$http = axios

Vue.prototype.serverUrl = 'https://osam-server.run.goorm.io/'

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
