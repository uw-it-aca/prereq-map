import Vue from 'vue/dist/vue.js';
import VueRouter from 'vue-router/dist/vue-router.js'
import App from './App.vue'

Vue.use(VueRouter)

var router = new VueRouter({
    mode: 'history',
    routes: [{
        path: '/course-search/'
    }, ]
});

export const dataBus = new Vue();

new Vue({
    render: h => h(App),
    router
}).$mount('#course')
