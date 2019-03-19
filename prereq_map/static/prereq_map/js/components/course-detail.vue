<template>
<div class="col mt-5 mb-5 course-detail" v-if="this.course_param !== undefined ">

    <h2 class="pt-3">{{ course_param }} – {{ course_title }}</h2>

    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sit amet consectetur dui. Donec ut enim lorem. Sed sed accumsan sem. Etiam felis mauris, pulvinar in felis id, aliquam scelerisque nisi. Nullam et euismod enim. Ut a elit a
        mi
        efficitur mattis. Mauris ac porta. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sit amet consectetur dui. </p>

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
                                <li class="#">ACCTG 225</li>
                                <li class="#">ECON 200</li>
                                <li class="#">
                                    One of MATH 112, MATH 124, MATH 125, MATH 134, MATH 135, or Q SCI 291</li>
                                <li class="#">One of ECON 311, IND E 315, QMETH 201, Q SCI 291, Q SCI 381, PSYCH 315, PSYCH 318, STAT 220, STAT 221/SOC 221/CS&SS 221, STAT 311, or STAT 390; </li>
                            </ol>
                        </td>

                    </tr>
                    <tr id="course-prereq-for">
                        <th class="w-25" scope="row">Is a prerequisite for<span class="info-popover"><i class="fa fa-info-circle" aria-hidden="true" tabindex="0" data-placement="top" data-toggle="popover" data-trigger="focus" title="" data-content="#"
                                    data-original-title="Declared Majors"></i></span></th>
                        <td class="w-75">
                            <ul class="list-inline comma-list">
                                <li class="#">ABCD 123</li>
                                <li class="#">ZYX 123</li>
                                <li class="#">ABCD 123</li>
                                <li class="#">ZYX 123</li>
                                <li class="#">ABCD 123</li>
                            </ul>
                        </td>
                    </tr>
                    <tr id="course-concurrent">
                        <th class="w-25" scope="row">Can be taken concurrently with<span class="info-popover"><i class="fa fa-info-circle" aria-hidden="true" tabindex="0" data-placement="top" data-toggle="popover" data-trigger="focus" title=""
                                    data-content="#" data-original-title="Declared Majors"></i></span></th>
                        <td class="w-75">
                            <ul class="list-inline comma-list">
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
export default {
    components: {
        'course-graph': Graph
    },
    data() {
        return {
            course_title: '',
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
