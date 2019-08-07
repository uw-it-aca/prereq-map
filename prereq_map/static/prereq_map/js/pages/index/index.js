import Vue from 'vue';
import VueRouter from 'vue-router';
import VueAnalytics from "vue-analytics";

import App from "./app.vue";
import Home from './home.vue';
import Register from './register.vue';
import Login from './login.vue';

import Curriculum from '../curriculum/app.vue';
//import Course from '../course/app.vue';

const gaCode = $("body").data("google-analytics");
const debugMode = $("body").data("django-debug");

Vue.use(VueRouter);

var router = new VueRouter({
  mode: "history",
  routes: [
    { path: '/', component: Home },
    { path: '/register/', component: Register },
    { path: '/login/', component: Login },
    { path: '/curriculum/', component: Curriculum },
  ]
});

Vue.use(VueAnalytics, {
  id: gaCode,
  router,
  set: [
    { field: 'anonymizeIp', value: true }
  ],
  debug: {
    enabled: debugMode
  }
});

new Vue({
  router,
  render: h => h(App)
}).$mount("#index");
