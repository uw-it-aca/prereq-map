<template>
<div v-cloak v-if="this.course_param !== undefined ">
    <div id="graph_container"></div>
</div>
</template>

<script>
const axios = require('axios');
export default {

    data() {
        return {
            course_param: '',
            course_data: undefined
        }
    },

    mounted() {

        //let $this = this;
        //let uri = window.location.search.substring(1);
        //let params = new URLSearchParams(uri);
        //this.course_param = params.get("course");

        //console.log("first load")
        this.course_param = this.$route.query.course
        //console.log(this.course_param);

        if (this.course_param !== undefined) {
            axios.get('/api/course/' + encodeURI(this.course_param))
                .then(response => (this.course_data = response))
        }
    },

    watch: {
        course_data: function() {
            show_graph(this.course_data.data)
        },

        '$route'(to, from) {
            // react to route changes...
            //console.log("route changed")
            //console.log(this.course_data)

            this.course_param = this.$route.query.course

            if (this.course_param !== undefined) {
                axios.get('/api/course/' + encodeURI(this.course_param))
                    .then(response => (this.course_data = response))

            }
        }
    },

}
</script>
