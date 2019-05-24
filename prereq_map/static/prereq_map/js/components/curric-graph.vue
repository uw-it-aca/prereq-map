<template>
<div v-if="curric_param !== undefined">
    <div v-cloak v-if="curric_emtpy">
        This curriculum does not have any courses with prerequisites. Please consult an adviser.
    </div>
    <div v-else>
        <small class="text-secondary">Use the scroll function on your mouse or touchpad to zoom in and out</small>
        <div id="graph_container"></div>
    </div>
</div>
</template>

<script>
const axios = require('axios');
export default {

    data() {
        return {
            curric_param: undefined,
            course_param: undefined,
            curric_data: [],
            course_list: [],
            curric_emtpy: undefined
        }
    },
    methods: {

        getCurric: function() {
            return axios
                .get('/api/curric/' + encodeURI(this.curric_param))
                .then(response => {
                    this.curric_data = response.data

                    //filter the data to just course_number
                    this.course_list = this.curric_data.x.nodes.course_number

                    // check to see if course_list is empty
                    if (Object.keys(this.course_list).length !== 0) {
                        this.curric_emtpy = false
                    } else {
                        this.curric_emtpy = true
                    }

                    this.loading = false

                })
                .catch(error => {
                    console.log(error)
                })
        }

    },

    mounted() {

        this.curric_param = this.$route.query.curric
        this.course_param = this.$route.query.course

        if (this.curric_param !== undefined) {
            this.getCurric()
        }

    },

    watch: {
        curric_data: function() {
            show_graph(this.curric_data, this.course_param)
        },

        '$route.query.curric': function() {
            // react to route changes...

            this.curric_param = this.$route.query.curric
            this.course_param = this.$route.query.course

            if (this.curric_param !== undefined) {
                this.getCurric()
            }

        }

    }

}
</script>
