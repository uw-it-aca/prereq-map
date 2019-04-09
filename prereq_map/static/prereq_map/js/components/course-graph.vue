<template>
<div v-cloak v-if="this.courseParam !== undefined ">
    <div id="graph_container"></div>
</div>
</template>

<script>
const axios = require('axios');
import { dataBus } from "../course";

export default {
    props: {
        courseParam: String,
        courseData: Object
    },
    data() {
        return {
            //course_param: '',
            course_data: undefined
        }
    },
    mounted() {

        console.log("mounted")
        console.log(this.courseParam)
        console.log(this.courseData)

        //this.course_param = this.$route.query.course;

        if (this.courseParam !== undefined) {
            axios.get('/api/course/' + encodeURI(this.courseParam))
                .then(response => (this.course_data = response))
        }
    },

    watch: {


        course_data: function() {
            show_graph(this.course_data.data);
            dataBus.$emit("course_data", this.course_data.data)
        },


        '$route.query.course': function () {

            // react to route changes...
            console.log("watch")
            console.log(this.courseParam)
            console.log(this.courseData)

            //this.course_param = this.$route.query.course;

            if (this.courseParam !== undefined) {
                axios.get('/api/course/' + encodeURI(this.courseParam))
                    .then(response => (this.course_data = response))

            }
        }
    },

}
</script>
