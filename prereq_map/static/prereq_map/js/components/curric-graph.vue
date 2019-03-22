<template>
    <div v-cloak v-if="this.curric_param !== undefined ">
        <div id="graph_container"></div>
    </div>
</template>

<script>
const axios = require('axios');
export default {

    data() {
        return {
            curric_param: '',
            curric_data: undefined
        }
    },

    mounted() {

        //console.log('FOOO');
        //let $this = this;
        //let uri = window.location.search.substring(1);
        //let params = new URLSearchParams(uri);
        //this.curric_param = params.get("curric");

        this.curric_param = this.$route.query.curric

        if (this.curric_param !== undefined) {
            axios.get('/api/curric/' + encodeURI(this.curric_param))
                .then(response => (this.curric_data = response))
        }

    },

    watch: {
        curric_data: function() {
            show_graph(this.curric_data.data)
        },

        '$route.query.curric': function() {
            // react to route changes...

            this.curric_param = this.$route.query.curric

            if (this.curric_param !== undefined) {
                axios.get('/api/curric/' + encodeURI(this.curric_param))
                    .then(response => (this.curric_data = response))
            }
        }

    }

}
</script>
