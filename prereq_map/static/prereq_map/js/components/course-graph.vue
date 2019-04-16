<template>
<div v-cloak v-if="this.courseParam !== undefined ">
    <small class="text-secondary">Use the mouse scroll wheel to control zoom-in and zoom-out.</small>
    <div id="graph_container"></div>
</div>
</template>

<script>
const axios = require('axios');
import { dataBus } from "../course";

export default {
    props: {
        courseParam: String,
    },
    data() {
        return {
            course_data: undefined
        }
    },
    mounted() {

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
            if (this.courseParam !== undefined) {
                axios.get('/api/course/' + encodeURI(this.courseParam))
                    .then(response => (this.course_data = response))

            }
        }
    },

}
</script>
