<template>
    <div>
        <div class="card" v-if="course_code">
            <div class="card-header bg-white">
                <h5 class="m-0">{{ course_code }}</h5>
                <a href="#" class="prereq-infobox-close" v-on:click.stop.prevent="close"><i class="fas fa-times"></i></a>
                <p class="card-title" v-if="course_description">{{ course_description }}</p>
            </div>
            <div class="card-body bg-light">

                <div v-if="loading">Loading.....</div>
                <div v-else>

                    <h5 class="card-title">Has these prerequisites</h5>
                    <ul class="prereq-list">
                        <li v-if="prereqs.length === 0">none</li>
                        <li v-for="prereq in prereqs">
                            <a v-bind:href="'/course-search/?course=' + prereq">{{prereq}}</a>
                        </li>
                    </ul>

                    <h5 class="card-title">Is a prerequisite for</h5>
                    <ul class="prereq-list">
                        <li v-if="postreqs.length === 0">none</li>
                        <li v-for="postreq in postreqs">
                            <a v-bind:href="'/course-search/?course=' + postreq">{{postreq}}</a>
                        </li>
                    </ul>

                </div>
            </div>
            <div class="card-footer bg-white text-center">
                <a v-bind:href="'/course-search/?course=' + course_code" class="btn btn-primary btn-lg  prereq-infobox-button">More details</a>
            </div>
        </div>
    </div>
</template>

<script>
//import { dataBus } from "../course";
const axios = require('axios');
export default {
    data() {
        return {
            loading: true,
            course_code: '',
            last_selected: '',
            prereqs: [],
            postreqs: [],
            course_data: undefined,
            course_description: ''
        }
    },
    mounted() {

        this.course_code = this.$route.query.course;
        if(this.course_code !== undefined){
            this.show(this.course_code);
        }

        // global click handler for show node event
        $(document).on('showCourseInfo', (event, course_code) => {
            this.show(course_code);
        });

        // global click handler for close node event
        $(document).on('closeCourseInfo', (event) => {
            this.close();
        });

    },
    methods: {
        load_course: function(course_code) {
            axios.get('/api/course/' + encodeURI(course_code))
                .then(response => {
                    this.course_data = response
                    this.loading = false
                })
        },
        get_prereqs: function (course, from_list) {
            var keys = Object.keys(from_list);
            var from = [];
            keys.forEach(function(key){
                var value = from_list[key];
                if(course !== value && !from.includes(value)){
                    from.push(value)
                }
            });
            return from;
        },
        get_postreqs: function (course, to_list){
            var keys = Object.keys(to_list);
            var to = [];
            keys.forEach(function(key){
                var value = to_list[key];
                if(course !== value && !to.includes(value)){
                    to.push(value)
                }
            });
            return to;
        },
        show: function (code) {

            this.loading = true
            this.course_code = code;
            this.$router.push({ query: Object.assign({}, this.$route.query, { course: this.course_code }) });

            if (this.course_code !== undefined) {
                this.load_course(code);
            }
        },

        close: function() {
            // set course param to undefined in order to clear it out from query
            this.$router.replace({ query: Object.assign({}, this.$route.query, { course: undefined }) });
        },

    },

    watch: {

        '$route.query.course': function () {
            this.course_code = this.$route.query.course;
            this.show(this.course_code)
        },
        course_data: function () {
            this.prereqs = this.get_prereqs(this.course_code, this.course_data.data.x.edges.from);
            this.postreqs = this.get_postreqs(this.course_code, this.course_data.data.x.edges.to);
            this.course_description = this.course_data.data.course_description;
        }

    },
}
</script>

<style lang="scss">

.prereq-infobox-close {
    position: absolute;
    top: 0.375rem;
    right: 0.375rem;
    z-index: 10;
    display: block;
    padding: 0.25rem 0.5rem;
    color: #000;

    &:hover { color: #666; }
}

.prereq-infobox-button {
    background-color: #4d307f;
    color: #FFF;
    border: none;
}
</style>
