<template>
    <div>
        <div id="graph_container" style="width: 100%; height: 100%; border: 1px solid rgba(0,0,0,.125);"></div>
    </div>
</template>

<script>
    const axios = require('axios');
    export default {
        mounted: function () {
            let $this = this;
            let uri = window.location.search.substring(1);
            let params = new URLSearchParams(uri);
            this.course_param = params.get("course");

            if(this.course_param !== null){
                axios.get('/api/course/' + encodeURI(this.course_param))
                    .then(response => ($this.course_data = response))

            }
        },
        data: function () {
            return {
                course_param: '',
                course_data: undefined
            }
        },
        watch: {
            course_data: function(){
                show_graph(this.course_data.data)
            }
        }

    }
</script>

<style>
</style>
