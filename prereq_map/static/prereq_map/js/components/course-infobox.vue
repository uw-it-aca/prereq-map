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
                <p class="card-title">Lorem ipsum dolor set amet dapibus ac facilisis in</p>
            </div>
            <div class="card-header card-body">
                <h6 class="card-title">Has these prerequisites<span class="info-popover"><i class="fa fa-info-circle" aria-hidden="true" tabindex="0" data-placement="top" data-toggle="popover" data-trigger="focus" title="" data-content="#"
                            data-original-title="Declared Majors"></i></span></h6>
                <ul class="list">
                    <li class="#">ABCD 123</li>
                    <li class="#">ZYX 123</li>
                    <li class="#">ABCD 123</li>
                    <li class="#">ZYX 123</li>
                    <li class="#">ABCD 123</li>
                </ul>
            </div>
            <div class="card-header card-body">
                <h5 class="card-title">Is a prerequisite for<span class="info-popover"><i class="fa fa-info-circle" aria-hidden="true" tabindex="0" data-placement="top" data-toggle="popover" data-trigger="focus" title="" data-content="#" data-original-title="Declared Majors"></i></span></h5>
                <ul class="list">
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
            course_code: ''
        }
    },
    mounted() {

        // global click handler for node click event
        $(document).on('myCustomEvent', (event, course_code) => {
            //console.log(course_code)
            this.show(course_code)
        });
    },
    methods: {
        show: function (code) {
            this.course_code = code
        }
    }
}
</script>

<style scoped>
.card {

}
</style>
