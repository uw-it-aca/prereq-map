<template>
<div class="mt-5 mb-5 course-detail" v-if="this.course_param !== undefined ">

    <h2 class="pt-3">{{ course_param }} – {{ course_title }}</h2>

    <p>{{course_description}}</p>

    <div class="row">
        <div class="col-md-5">

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
                            <ol class="list-group list-group-flush">
                                <li v-for="prereq in prereqs">
                                    {{prereq}}
                                </li>
                            </ol>
                        </td>

                    </tr>
                    <tr id="course-prereq-for">
                        <th class="w-25" scope="row">Is a prerequisite for<span class="info-popover"><i class="fa fa-info-circle" aria-hidden="true" tabindex="0" data-placement="top" data-toggle="popover" data-trigger="focus" title="" data-content="#"
                                    data-original-title="Declared Majors"></i></span></th>
                        <td class="w-75">
                            <ul class="list-inline comma-list">
                                <li v-for="postreq in postreqs">
                                    {{postreq}}
                                </li>
                            </ul>
                        </td>
                    </tr>
                    <tr id="course-concurrent">
                        <th class="w-25" scope="row">Can be taken concurrently with<span class="info-popover"><i class="fa fa-info-circle" aria-hidden="true" tabindex="0" data-placement="top" data-toggle="popover" data-trigger="focus" title=""
                                    data-content="#" data-original-title="Declared Majors"></i></span></th>
                        <td class="w-75">
                            <ul class="list-inline comma-list">
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


    <h2 class="pt-3">See related Prerequisite Maps</h2>

    <p>Click on the curriculum links to see related prerequisite maps. To see other campus curriculum, use the search bar on the Curriculum Search page.</p>
    <h3 class="pt-3">College of Arts and Sciences</h3>
    <ul class="list-group-flush" id="related-prereq">
        <li class="#"><a href="#">Curriculum X</a></li>
        <li class="#"><a href="#">Curriculum Y</a></li>
        <li class="#"><a href="#">Curriculum Z</a></li>
    </ul>

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
    created() {
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
    },

    watch: {
        '$route'(to, from) {
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

<style scoped>
.course-detail {
    border: solid 1px red;
    padding: 10px;
}
</style>
