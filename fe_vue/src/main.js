// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import BootstrapVue from 'bootstrap-vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VModal from 'vue-js-modal'
import Snackbar from 'vuejs-snackbar';

 
Vue.use(VModal)

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(VueAxios, axios)
Vue.component('snackbar', Snackbar)
Vue.axios.defaults.baseURL = process.env.API_BASE_URL;

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
