<template>
<div class="row curric-search">
    <div class="col-md-9 offset-md-1">
        <vue-bootstrap-typeahead
            class="mb-3"
            v-model="query"
            :data="curric_list"
            @hit="selected_curric = $event"
            placeholder="E.G. ANTH"
        />
    </div>
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
                query2: '',
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

<style lang="scss">

@import '../../css/styles.scss';

// char's note: scoped css is "broken" for this component because
//  vue-bootstrap-typeahead is already a scoped component by default... so it
// cannot be scoped again. just be aware of this in the future!

.curric-search {

    input {
        height: 3rem;
        font-size: 1.25rem;
        color: #000;
    }

    .vbt-autcomplete-list {
        box-shadow: none !important;
    }
}
</style>
