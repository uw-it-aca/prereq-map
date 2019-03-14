<template>
    <div>
        <div id="graph_container" style="width: 100%; height: 100%; border: 1px solid rgba(0,0,0,.125);"></div>
    </div>
</template>

<script>
    const axios = require('axios');
    export default {
        mounted: function () {
            console.log('FOOO');
            let $this = this;
            let uri = window.location.search.substring(1);
            let params = new URLSearchParams(uri);
            this.curric_param = params.get("curric");

            if(this.curric_param !== null){
                axios.get('/api/curric/' + encodeURI(this.curric_param))
                    .then(response => ($this.curric_data = response))

            }
        },
        data: function () {
            return {
                curric_param: '',
                curric_data: undefined
            }
        },
        watch: {
            curric_data: function(){
                show_graph(this.curric_data.data)
            }
        }

    }
</script>

<style>
</style>
