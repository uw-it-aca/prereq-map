<template>
<div class="col course-detail" v-if="this.course_param !== undefined ">

    <h2 class="pt-3"><span>{{ course_param }}</span> – <span class="text-danger">{{ course_title }}</span></h2>

    <p class="text-danger">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sit amet consectetur dui. Donec ut enim lorem. Sed sed accumsan sem. Etiam felis mauris, pulvinar in felis id, aliquam scelerisque nisi. Nullam et euismod enim. Ut a elit a
        mi
        efficitur mattis. Mauris ac porta. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sit amet consectetur dui. </p>

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
                            <ul class="list-inline comma-list text-danger">
                                <li class="#">ABCD 123</li>
                                <li class="#">ZYX 123</li>
                                <li class="#">ABCD 123</li>
                                <li class="#">ZYX 123</li>
                                <li class="#">ABCD 123</li>
                            </ul>
                        </td>

                    </tr>
                    <tr id="course-prereq-for">
                        <th class="w-25" scope="row">Is a prerequisite for<span class="info-popover"><i class="fa fa-info-circle" aria-hidden="true" tabindex="0" data-placement="top" data-toggle="popover" data-trigger="focus" title="" data-content="#"
                                    data-original-title="Declared Majors"></i></span></th>
                        <td class="w-75">
                            <ul class="list-inline comma-list text-danger">
                                <li class="#">ABCD 123</li>
                                <li class="#">ZYX 123</li>
                                <li class="#">ABCD 123</li>
                                <li class="#">ZYX 123</li>
                                <li class="#">ABCD 123</li>
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
export default {
    components: {
        'course-graph': Graph
    },
    data() {
        return {
            course_title: 'Give me a course title',
            course_param: ''
        }
    },
    mounted() {
        //let uri = window.location.search.substring(1);
        //let params = new URLSearchParams(uri);
        //this.course_param = params.get("course");
        this.course_param = this.$route.query.course
    },
    watch: {
        '$route'(to, from) {
            // react to route changes...
            //console.log("route changed")
            //console.log(this.$route.query.course)
            this.course_param = this.$route.query.course
        }
    },
}
</script>
