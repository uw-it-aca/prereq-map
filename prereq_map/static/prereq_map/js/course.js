import Vue from 'vue/dist/vue.js'
import VueRouter from 'vue-router/dist/vue-router.js'

import CourseSearch from "./components/course-search.vue";
import CourseDetail from "./components/course-detail.vue";

Vue.use(VueRouter)

var router = new VueRouter({
    mode: 'history',
    routes: [{
        path: '/course-search/', component: CourseSearch
    }]
});

new Vue({
    delimiters: ['[[', ']]'],
    el: '#vue_course',
    router,
    components: {
        'course-search': CourseSearch,
        'course-detail': CourseDetail,
    },

    data: function () {
        return {
            course_param: '',
        }
    },

    watch: {
        '$route' (to, from) {
          // react to route changes...
           console.log("route changed")
           console.log(this.$route.query.course)
           this.course_param = this.$route.query.course
        }
    },

    created: function () {

        //let uri = window.location.search.substring(1);
        //let params = new URLSearchParams(uri);
        //this.course_param = params.get("course");

        //console.log(this.course_param)
        console.log(this.$route.query.course)
        this.course_param = this.$route.query.course

    },


});
