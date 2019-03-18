import Vue from 'vue/dist/vue.js';
import VueRouter from 'vue-router/dist/vue-router.js'

import CourseInfoBox from "./components/course-infobox.vue";
import Typeahead from "./components/typeahead.vue";
import Graph from "./components/curric-graph.vue";

Vue.use(VueRouter)

var router = new VueRouter({
    mode: 'history',
    routes: [{
        path: '/curriculum-search/', component: CourseInfoBox
    }]
});

new Vue({
    delimiters: ['[[', ']]'],
    el: '#vue_curriculum',
    router,
    components: {
        'course-infobox': CourseInfoBox,
        'typeahead': Typeahead,
        'curric-graph': Graph
    },

    data: function () {
        return {
            curric_param: '',
        }
    },

    watch: {
        '$route'(to, from) {
            // react to route changes...
            //console.log("route changed")
            //console.log(this.$route.query.curric)
            this.curric_param = this.$route.query.curric
        }
    },

    created: function () {

        //let uri = window.location.search.substring(1);
        //let params = new URLSearchParams(uri);
        //this.course_param = params.get("course");

        //console.log(this.course_param)
        //console.log(this.$route.query.curric)
        this.curric_param = this.$route.query.curric

    },

});
