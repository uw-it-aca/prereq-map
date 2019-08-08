import Vue from 'vue';
import VueRouter from 'vue-router';
import VueAnalytics from "vue-analytics";

import App from "./app.vue";
import Curriculum from './curriculum.vue';
import Course from './course.vue';

const gaCode = $("body").data("google-analytics");
const debugMode = $("body").data("django-debug");

Vue.use(VueRouter);

var router = new VueRouter({
  mode: "history",
  routes: [
    { path: '/', redirect: '/curriculum/' },
    { path: '/curriculum/', component: Curriculum },
    { path: '/course/', component: Course },
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

export const dataBus = new Vue();

new Vue({
  router,
  render: h => h(App)
}).$mount("#index");
