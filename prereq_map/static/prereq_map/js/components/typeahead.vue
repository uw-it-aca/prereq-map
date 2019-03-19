<template>

    <div id="main-search" class="search-width">

        <vue-bootstrap-typeahead
                class="woot"
                v-model="query"
                :data="curric_list"
                @hit="selected_curric = $event"
                placeholder="Search curricula.."
        >
            <template slot="suggestion" slot-scope="{ data, htmlText }">
                <div class="d-flex align-items-center">
                    <!-- Note: the v-html binding is used, as htmlText contains
                         the suggestion text highlighted with <strong> tags -->
                    <span class="ml-4" v-html="htmlText"></span>
                </div>
            </template>
        </vue-bootstrap-typeahead>


    </div>

</template>

<script>
    import {_} from 'vue-underscore';
    const axios = require('axios');
    import VueBootstrapTypeahead from 'vue-bootstrap-typeahead';

    export default {

        components: {
            VueBootstrapTypeahead
        },

        data() {
            return {
                query: '',
                selected_curric: null,
                curric_list: [],
                curric_objs: null
            }
        },
        mounted() {
            var self = this;
            axios.get('/api/curric_typeahead')
                .then((res) => {
                    this.curric_objs = res.data;
                    var curric_list = [];

                    $(res.data).each(function(idx, value){
                       curric_list.push(...Object.keys(value));
                    });
                    this.curric_list = curric_list;
                });
        },

        watch: {
            selected_curric(curric_query){
                var curric_code = this.curric_objs[curric_query];
                //location.href = "?curric=" + curric_code;
                this.$router.push('/curriculum-search/?curric=' + curric_code)

            },

            '$route'(to, from) {
                // react to route changes...
            }

        },

        filters: {
        },

    }
</script>

<style>

    .search-width {
    input {
        height: 3rem;
        border-radius: 0;
        border: 0.04688rem solid #333;
    }
    }

    .vbt-autcomplete-list { box-shadow: none !important; }

</style>
