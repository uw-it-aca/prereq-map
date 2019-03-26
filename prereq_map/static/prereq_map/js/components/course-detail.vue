<template>
<div class="col course-detail" v-cloak v-if="this.course_param !== undefined ">

    <h2 class="pt-3"><span>{{ course_param }}</span> – <span class="text-danger">{{ course_title }}</span></h2>

    <p>{{course_description}}</p>

    <div class="row">
        <div class="col-md-5 pb-5">

            <div>
                <course-graph></course-graph>
            </div>

        </div>
        <div class="col-md-7">

            <table class="table" id="prereq-table">
                <tbody>
                    <tr>
                        <th class="w-25" scope="row">Has these prerequisites<span class="info-popover"><i class="fa fa-info-circle" aria-hidden="true" tabindex="0" data-placement="top" data-toggle="popover" data-trigger="focus" title="" data-content="#"
                                    data-original-title="Declared Majors"></i></span></th>
                        <td class="w-75">
                            <ul class="">
                                <li v-if="prereqs.length === 0">none</li>
                                <li v-for="prereq in prereqs">
                                    {{prereq}}
                                </li>
                            </ul>
                        </td>

                    </tr>
                    <tr>
                        <th class="w-25" scope="row">Is a prerequisite for<span class="info-popover"><i class="fa fa-info-circle" aria-hidden="true" tabindex="0" data-placement="top" data-toggle="popover" data-trigger="focus" title="" data-content="#"
                                    data-original-title="Declared Majors"></i></span></th>
                        <td class="w-75">
                            <ul class="">
                                <li v-if="postreqs.length === 0">none</li>
                                <li v-for="postreq in postreqs">
                                    {{postreq}}
                                </li>
                            </ul>
                        </td>

                    </tr>
                    <tr>
                        <th class="w-25" scope="row">Is a co-requisite for<span class="info-popover"><i class="fa fa-info-circle" aria-hidden="true" tabindex="0" data-placement="top" data-toggle="popover" data-trigger="focus" title="" data-content="#"
                                    data-original-title="Declared Majors"></i></span></th>
                        <td class="w-75">
                            <ul class="">
                                <li v-if="concurrents.length === 0">none</li>
                                <li v-for="concurrent in concurrents">
                                    {{concurrent}}
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
    data() {
        return {
            course_title: '',
            course_param: '',
            course_description: '',
            prereqs: [],
            postreqs: [],
            concurrents: []
        }
    },
    mounted() {
        //let uri = window.location.search.substring(1);
        //let params = new URLSearchParams(uri);
        //this.course_param = params.get("course");
        this.course_param = this.$route.query.course;
        dataBus.$on('course_data', (data) => {
            this.course_description = data.course_description;
            this.course_title = data.course_title;
            this.prereqs = this.get_prereqs(this.course_param, data.x.edges.from);
            this.postreqs = this.get_postreqs(this.course_param, data.x.edges.to);
            this.concurrents = this.get_concurrent_courses(data);
        });

        console.log(this.prereqs)
    },
    watch: {

        '$route.query.course': function () {
            // react to route changes...
            //console.log("route changed")
            //console.log(this.$route.query.course)
            this.course_param = this.$route.query.course
        }

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

        get_concurrent_courses: function (course_data){
            var concurrent_ids = this.get_concurrent_ids(course_data.x.edges.pr_concurrency);
            var concurrent_courses = [];
            concurrent_ids.forEach(function(id) {
                if(id in course_data.x.edges.to){
                    concurrent_courses.push(course_data.x.edges.to[id]);
                }
                else if (id in course_data.x.edges.from){
                    concurrent_courses.push(course_data.x.edges.from[id]);
                }
            });
            return concurrent_courses;

        },

        get_concurrent_ids: function (pr_concurrency){
            var concurrent_ids = [];
            Object.keys(pr_concurrency).forEach(function(id) {
                if(pr_concurrency[id] === "Y"){
                    concurrent_ids.push(id);
                }
            });
            return concurrent_ids;
        }
    }

}
</script>
