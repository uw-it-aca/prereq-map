import Vue from 'vue/dist/vue.js';
import VueRouter from 'vue-router/dist/vue-router.js'
import axios from 'axios';

import Onboarding from "./components/onboarding.vue";
import CourseInfoBox from "./components/course-infobox.vue";
import Typeahead from "./components/typeahead.vue";
import Graph from "./components/curric-graph.vue";

Vue.use(VueRouter)

var router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/curriculum-search/', component: CourseInfoBox },
    ]
});

new Vue({
    delimiters: ['[[', ']]'],
    el: '#vue_curriculum',
    router,
    components: {
        'onboarding' : Onboarding,
        'typeahead': Typeahead,
        'curric-graph': Graph,
        'course-infobox': CourseInfoBox
    },
});
