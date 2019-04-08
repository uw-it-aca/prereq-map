<template>
<div class="col course-detail" v-cloak>

    <div class="row">
        <div class="col-md-5 pb-5">
            <div>
                <course-graph
                    v-bind:course-param="this.courseParam"
                    v-bind:course-data="this.courseData"
                ></course-graph>
            </div>
        </div>
        <div class="col-md-7">

            <h2 class="pt-3"><span>{{ courseParam }}</span> – <span class="text-danger">{{ course_title }}</span></h2>
            <p>{{course_description}}</p>

            <table class="table" id="prereq-table">
                <tbody>
                    <tr>
                        <th class="w-25" scope="row">Has these prerequisites</th>
                        <td class="w-75">
                            <ul class="prereq-list">
                                <li v-if="prereqs.length === 0">none</li>
                                <li v-for="prereq in prereqs">
                                    <a v-bind:href="'/course-search/?course=' + prereq">{{prereq}}</a>
                                </li>
                            </ul>
                        </td>

                    </tr>
                    <tr>

                        <th class="w-25" scope="row">Is a prerequisite for</th>
                        <td class="w-75">
                            <ul class="prereq-list">
                                <li v-if="postreqs.length === 0">none</li>
                                <li v-for="postreq in postreqs">
                                    <a v-bind:href="'/course-search/?course=' + postreq">{{postreq}}</a>
                                </li>
                            </ul>
                        </td>

                    </tr>
                </tbody>
            </table>

        </div>
    </div>

</div>
</template>

<script>
import Graph from "./course-graph.vue";
import { dataBus } from "../course";
export default {
    components: {
        'course-graph': Graph
    },
    props: {
        courseParam: String,
        courseData: Object
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
            this.prereqs = this.get_prereqs(this.courseParam, data.x.edges.from);
            this.postreqs = this.get_postreqs(this.courseParam, data.x.edges.to);
        });

        /*
        this.course_title = this.courseData.course_title;
        this.course_description = this.courseData.course_description;
        this.prereqs = this.get_prereqs(this.courseParam, this.courseData.x.edges.from);
        this.postreqs = this.get_postreqs(this.courseParam, this.courseData.x.edges.to);
        */
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
