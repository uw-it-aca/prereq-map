import Vue from 'vue/dist/vue.js';
import VueRouter from 'vue-router/dist/vue-router.js'
import VueAnalytics from 'vue-analytics'
import App from './app.vue'

Vue.use(VueRouter)

var router = new VueRouter({
    mode: 'history',
    routes: [{
        path: '/curriculum-search/'
    }, ]
});

Vue.use(VueAnalytics, {
  id: 'UA-XXX-X',
  router,
  debug: {
    enabled: true
  }
})

new Vue({
    render: h => h(App),
    router
}).$mount('#curriculum')
