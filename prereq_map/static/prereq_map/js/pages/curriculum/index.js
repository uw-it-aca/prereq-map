import Vue from 'vue/dist/vue.js'
import VueRouter from 'vue-router/dist/vue-router.js'
import VueAnalytics from 'vue-analytics'
import App from './app.vue'

const gaCode = $("body").data("google-analytics");
const isProd = false

Vue.use(VueRouter)

var router = new VueRouter({
    mode: 'history',
    routes: [{
        path: '/curriculum-search/'
    }, ]
});

Vue.use(VueAnalytics, {
    id: gaCode,
    router,
    debug: {
        enabled: true
        //enabled: !isProd
    }
})

new Vue({
    render: h => h(App),
    router
}).$mount('#curriculum')
