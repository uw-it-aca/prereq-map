import Vue from 'vue/dist/vue.js'
import VueRouter from 'vue-router/dist/vue-router.js'
import axios from 'axios';

import CourseSearchInput from "./components/course-search-input.vue";
import CourseDetail from "./components/course-detail.vue";

Vue.use(VueRouter)

var router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/course-search/', component: CourseSearchInput },
    ]
});

export const dataBus = new Vue();

new Vue({
    delimiters: ['[[', ']]'],
    el: '#vue_course',
    router,
    components: {
        'course-search-input': CourseSearchInput,
        'course-detail': CourseDetail,

    },
    data() {
        return {
            course_param: undefined,
            course_data: [],
            course_number: '',
            course_valid: undefined
        }
    },
    methods: {

        getCourse: function() {
            return axios
                .get('/api/course/' + encodeURI(this.course_param))
                .then(response => {
                    this.course_data = response.data
                    this.course_number = this.course_data.x.nodes.course_number

                    // check to see if course_list is empty
                    if (Object.keys(this.course_number).length !== 0) {
                        this.course_valid = true
                    } else {
                        this.course_valid = false
                    }

                })
                .catch(error => {
                    this.course_valid = false
                    console.log("error " + error)
                })
        }
    },
    mounted() {

        this.course_param = this.$route.query.course

        if (this.course_param !== undefined) {
            this.getCourse()
        }

    },
    watch: {

        '$route.query.course': function() {

            this.course_param = this.$route.query.course

            if (this.course_param !== undefined) {
                this.getCourse()
            }

        }
    },

});
