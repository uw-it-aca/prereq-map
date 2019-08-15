import Vue from 'vue';
import VueRouter from 'vue-router';
import VueAnalytics from "vue-analytics";
import VueAnnouncer from 'vue-announcer';
import BootstrapVue from 'bootstrap-vue';

import App from "./App.vue";
import Curriculum from './pages/curriculum.vue';
import Course from './pages/course.vue';

const gaCode = $("body").data("google-analytics");
const debugMode = $("body").data("django-debug");

Vue.use(VueRouter);
Vue.use(VueAnnouncer);
Vue.use(BootstrapVue);

var router = new VueRouter({
  mode: "history",
  routes: [
    { path: '/', redirect: '/curriculum/' },
    { path: '/curriculum-search/', redirect: '/curriculum/' },
    { path: '/course-search/', redirect: '/course/' },
    { path: '/curriculum/', component: Curriculum },
    { path: '/course/', component: Course },
  ]
});

Vue.use(VueAnnouncer, {}, router);

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

// vue app will be rendered inside of #main div found in index.html using webpack_loader
new Vue({
  router,
  render: h => h(App)
}).$mount("#main");
