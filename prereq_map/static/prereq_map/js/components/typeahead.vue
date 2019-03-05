<template>

    <div id="main-search" class="search-width">

        <vue-bootstrap-typeahead
                class="woot"
                v-model="query"
                :data="curric_list"
                @hit="selected_curric = $event"
                placeholder="Search GitHub Users.."
        >
            <template slot="suggestion" slot-scope="{ data, htmlText }">
                <div class="d-flex align-items-center">
                    <!-- Note: the v-html binding is used, as htmlText contains
                         the suggestion text highlighted with <strong> tags -->
                    <span class="ml-4" v-html="htmlText"></span>
                </div>
            </template>
        </vue-bootstrap-typeahead>

        <h3>Selected User JSON</h3>
        <pre>{{ selected_curric}}</pre>

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
        mounted: function (){
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

        data: function () {
            return {
                query: '',
                selected_curric: null,
                curric_list: []
            }
        },
        methods: {
        },

        watch: {
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
