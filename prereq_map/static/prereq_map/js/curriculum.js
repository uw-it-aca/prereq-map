import Vue from 'vue/dist/vue.js';
import VueRouter from 'vue-router/dist/vue-router.js'
import axios from 'axios';

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
        'course-infobox': CourseInfoBox,
        'typeahead': Typeahead,
        'typeahead' : Typeahead,
        'curric-graph': Graph
    },
    data() {
        return {
            curric_param: '',
            curric_data: [],
            course_list: [],
            curric_emtpy: undefined
        }
    },
    methods: {

        getCurric: function() {
            return axios
                .get('/api/curric/' + encodeURI(this.curric_param))
                .then(response => {
                    this.curric_data = response.data
                    //filter the data to just course_number
                    this.course_list = this.curric_data.x.nodes.course_number

                    // check to see if course_list is empty
                    if (Object.keys(this.course_list).length !== 0) {
                        this.curric_emtpy = false
                    } else {
                        this.curric_emtpy = true
                    }

                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
    mounted() {

        this.curric_param = this.$route.query.curric

        if (this.curric_param !== undefined) {
            this.getCurric()
        }

    },
    watch: {

        '$route.query.curric': function () {
            //console.log("curric changed")
            this.curric_param = this.$route.query.curric

            if (this.curric_param !== undefined) {
                this.getCurric()
            }
        }

    },
});
