<template>
<div class="col course-detail" v-cloak>

    <div class="row">
        <div class="col-md-5 pb-5">
            <div>
                <course-graph v-bind:course-param="this.courseParam"></course-graph>
            </div>
        </div>
        <div class="col-md-7">

            <div class="mb-4">
                <h2 class="pt-3"><span>{{ courseParam }}</span> <span v-if="course_title">- {{ course_title }}</span></h2>
                <p v-if="course_description" v-html="course_description">{{course_description}}</p>
            </div>

            <div class="mb-4">

                <strong>Is a prerequisite for:</strong>
                <ul class="prereq-list">
                    <li v-if="postreqs.length === 0">none</li>
                    <li v-for="postreq in postreqs">
                        <a v-bind:href="'/course-search/?course=' + postreq">{{postreq}}</a>
                    </li>
                </ul>
            </div>

            <strong>Additional information:</strong>
            <p><a v-bind:href="'https://myplan.uw.edu/course/#/courses/' + courseParam" v-on:click="$ga.event('outbound', 'click', 'https://myplan.uw.edu/course/#/courses/' + courseParam)" target="_blank">View {{courseParam}} course details and schedule on MyPlan</a></p>

        </div>
    </div>

</div>
</template>

<script>
import Graph from "./course-graph.vue";

import { dataBus } from "../pages/course/";

export default {
    components: {
        'course-graph': Graph
    },
    props: {
        courseParam: String,
    },
    data() {
        return {
            course_title: '',
            course_description: '',
            prereqs: [],
            postreqs: [],
        }
    },
    mounted() {

        // get the course title, desc, and prereqs from the databus
        dataBus.$on('course_data', (data) => {
            this.course_title = data.course_title;
            this.course_description = data.course_description;
            
            // format the description hack!
            this.course_description = this.course_description.replace("Offered: ", "<br /><br /><strong>Blah:</strong> ");   
            console.log(this.course_description);

            this.prereqs = this.get_prereqs(this.courseParam, data.x.edges.from);
            this.postreqs = this.get_postreqs(this.courseParam, data.x.edges.to);
        });

    },
    watch: {

    },
    methods: {
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

    }

}
</script>
