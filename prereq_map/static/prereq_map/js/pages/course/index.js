import Vue from "vue/dist/vue.esm.js";
import VueRouter from "vue-router/dist/vue-router.js";
import VueAnalytics from "vue-analytics";
import App from "./app.vue";

const gaCode = $("body").data("google-analytics");
const debugMode = $("body").data("django-debug");

Vue.use(VueRouter);

var router = new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/course-search/"
    }
  ]
});

Vue.use(VueAnalytics, {
  id: gaCode,
  router,
  debug: {
    enabled: debugMode
  }
});

export const dataBus = new Vue();

new Vue({
  render: h => h(App),
  router
}).$mount("#course");
