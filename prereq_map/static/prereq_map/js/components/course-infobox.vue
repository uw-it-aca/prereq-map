<template>
    <div>
        <!--
        <p>click on course codes to see infobox (inside of component)</p>
        <ul>
            <li><a href="#" v-on:click.prevent="show('CSE 142')">CSE 142</a></li>
            <li><a href="#" v-on:click.prevent="show('CSE 143')">CSE 143</a></li>
        </ul> -->
        <div class="card" v-if="course_code">
            <div class="card-header bg-white">
                <h5 class="infobox-title">{{ course_code }}</h5>
                <span class="card-close clickable close-icon hidden" data-effect="fadeOut" v-on:click="close"><i class="fas fa-times"></i></span>
                <p class="card-title text-danger">{{ course_description }}</p>
            </div>
            <div class="card-header card-body">
                <h5 class="card-title">Has these prerequisites <span class="info-popover"><i class="fa fa-info-circle" tabindex="0" data-container="body" data-toggle="popover" data-placement="top" data-trigger="focus" data-content="Vivamus sagittis lacus vel augue laoreet rutrum faucibus."></i></span></h5>
                <ul class="prereq-list">
                    <li v-if="prereqs.length === 0">none</li>
                    <li v-for="prereq in prereqs">
                        <a v-bind:href="'/course-search/?course=' + prereq">{{prereq}}</a>
                    </li>
                </ul>
            </div>
            <div class="card-header card-body">
                <h5 class="card-title">Is a prerequisite for <span class="info-popover"><i class="fa fa-info-circle" tabindex="0" data-container="body" data-toggle="popover" data-placement="top" data-trigger="focus" data-content="Vivamus sagittis lacus vel augue laoreet rutrum faucibus."></i></span></h5>
                <ul class="prereq-list">
                    <li v-if="postreqs.length === 0">none</li>
                    <li v-for="postreq in postreqs">
                        <a v-bind:href="'/course-search/?course=' + postreq">{{postreq}}</a>
                    </li>
                </ul>
            </div>
            <div class="card-body text-center">
                <a v-bind:href="'/course-search/?course=' + course_code" class="btn btn-primary btn-block btn-lg btn-default">More details &amp; related curricula</a>
            </div>
        </div>
    </div>
</template>

<script>
import { dataBus } from "../course";
const axios = require('axios');
export default {
    data() {
        return {
            course_code: '',
            last_selected: '',
            prereqs: [],
            postreqs: [],
            course_data: undefined,
            course_description: ''
        }
    },
    mounted() {

        this.course_code = this.$route.query.course;
        if(this.course_code !== undefined){
            this.show(this.course_code);
        }

        // global click handler for show node event
        $(document).on('showCourseInfo', (event, course_code) => {
            this.show(course_code);
        });

        // global click handler for close node event
        $(document).on('closeCourseInfo', (event) => {
            this.close();
        });

    },
    methods: {
        load_course: function(course_code) {
            axios.get('/api/course/' + encodeURI(course_code))
                .then(response => (
                    this.course_data = response
                ))
        },
        get_prereqs: function (course, from_list) {
            var keys = Object.keys(from_list);
            var from = [];
            keys.forEach(function(key){
                var value = from_list[key];
                if(course !== value && !from.includes(value)){
                    from.push(value)
                }
            });
            return from;
        },
        get_postreqs: function (course, to_list){
            var keys = Object.keys(to_list);
            var to = [];
            keys.forEach(function(key){
                var value = to_list[key];
                if(course !== value && !to.includes(value)){
                    to.push(value)
                }
            });
            return to;
        },
        show: function (code) {
            this.course_code = code;
            this.$router.push({ query: Object.assign({}, this.$route.query, { course: this.course_code }) });
            this.load_course(code);

        },

        close: function() {
            this.course_code = ''
            this.$router.replace({ query: Object.assign({}, this.$route.query, { course: undefined }) });
            //window.network.nodes.unselectAll()
        },

    },

    watch: {

        /**
        '$route'(to, from) {
            // react to route changes...
            console.log("route changed")
            //console.log(this.$route.query.curric)

        },**/

        '$route.query.course': function () {

            this.course_code = this.$route.query.course;

            //this.curric_param = this.$route.query.curric
            this.show(this.course_code)
        },
        course_data: function () {
            console.log(this.course_data);
            this.prereqs = this.get_prereqs(this.course_code, this.course_data.data.x.edges.from);
            this.postreqs = this.get_postreqs(this.course_code, this.course_data.data.x.edges.to);
            this.course_description = this.course_data.data.course_title;
        }

    },
}
</script>

<style lang="scss">
#infobox {
    //width: 16rem;
}

#infobox .card-body {
    background: #E8E8E8;
}
#infobox .btn {
    white-space: normal !important;
    max-width: 100%;
}

#infobox .btn-default {
    background-color: #4d307f;
    color: #FFF;
    font-family: "Open Sans",Helvetica,Arial,sans-serif;
    font-size: 0.875rem;
    font-weight: 700;
    line-height: 1.125rem;
    padding-top: 0.875rem;
    padding-bottom: 0.875rem;
    border: 0;
}
#infobox .btn-default:hover,
.btn-default.a:focus,
.btn-default:active,
.btn-default:focus {
    background-color: #2F1956 !important;
    color: #FFF;
}

#infobox .button.navbar-toggler {
    padding-left: 0;
    outline: none;
    border: 0;
}

.infobox-title {
    font-size: 1.063rem;
    font-weight: 700;
    text-transform: uppercase;
    margin-bottom: 0.375rem;
    padding-top: 0.5rem;
}

#infobox .card-title {
    font-size: 0.875rem;
    line-height: 1.125rem;
    margin-bottom: 0.375rem;
}

#infobox .card-text,
#infobox li {
    font-size: 0.6875rem;
    margin-bottom: 0.375rem;
}

#infobox ol > li {
    font-size: 0.6875rem;
    margin-bottom: 0.375rem;
    margin-left: 1.1rem;
}

#infobox .comma-list {
    line-height: 1.2;
}
.comma-list li {
    display: inline;
    white-space: nowrap;
}

#infobox .comma-list li::after {
    content: ", ";
}

#infobox .comma-list li:last-child::after {
    content: "";
}

.card-close {
    position: absolute;
    top: 0.375rem;
    right: 0.375rem;
    z-index: 10;
    display: block;
    padding: 0.25rem 0.5rem;
}
</style>
