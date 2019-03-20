<template>
    <div>
        <!--
        <p>click on course codes to see infobox (inside of component)</p>
        <ul>
            <li><a href="#" v-on:click.prevent="show('CSE 142')">CSE 142</a></li>
            <li><a href="#" v-on:click.prevent="show('CSE 143')">CSE 143</a></li>
        </ul> -->
        <div class="card" id="infobox" v-if="course_code">
            <div class="card-header bg-white">
                <h5 class="infobox-title">{{ course_code }}</h5>
                <span class="card-close clickable close-icon" data-effect="fadeOut"><i class="fas fa-times"></i></span>
                <p class="card-title text-danger">Lorem ipsum dolor set amet dapibus ac facilisis in</p>
            </div>
            <div class="card-header card-body">
                <h6 class="card-title">Has these prerequisites<span class="info-popover"><i class="fa fa-info-circle" aria-hidden="true" tabindex="0" data-placement="top" data-toggle="popover" data-trigger="focus" title="" data-content="#"
                            data-original-title="Declared Majors"></i></span></h6>
                <ul class="list text-danger">
                    <li class="#">ABCD 123</li>
                    <li class="#">ZYX 123</li>
                    <li class="#">ABCD 123</li>
                    <li class="#">ZYX 123</li>
                    <li class="#">ABCD 123</li>
                </ul>
            </div>
            <div class="card-header card-body">
                <h5 class="card-title">Is a prerequisite for<span class="info-popover"><i class="fa fa-info-circle" aria-hidden="true" tabindex="0" data-placement="top" data-toggle="popover" data-trigger="focus" title="" data-content="#" data-original-title="Declared Majors"></i></span></h5>
                <ul class="list text-danger">
                    <li class="#">ABCD 123</li>
                    <li class="#">ZYX 123</li>
                    <li class="#">ABCD 123</li>
                    <li class="#">ZYX 123</li>
                    <li class="#">ABCD 123</li>
                </ul>
            </div>
            <div class="card-body text-center">
                <a v-bind:href="'/course-search/?course=' + course_code" class="btn btn-primary btn-block btn-lg btn-default">More details &amp; related curricula</a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            course_code: '',
            last_selected: ''
        }
    },
    mounted() {

        this.course_code = this.$route.query.course

        // global click handler for node click event
        $(document).on('showCourseInfo', (event, course_code) => {
            //console.log(course_code)
            this.show(course_code)

        });

    },
    methods: {
        show: function (code) {
            this.course_code = code

            this.$router.push({ query: Object.assign({}, this.$route.query, { course: this.course_code }) });

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

            this.course_code = this.$route.query.course

            console.log("course changed")
            //this.curric_param = this.$route.query.curric
            this.show(this.course_code)
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

.info-popover i {
    margin-left: 0.5rem;
    font-size: 85%;
    color: #8f9bcc;
    cursor: pointer;
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
