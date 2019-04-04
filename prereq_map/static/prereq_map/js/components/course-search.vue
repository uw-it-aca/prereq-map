<template>
<div class="row course-search">
    <div class="col-md-9 offset-md-1">
        <form id="signup-form" @submit.prevent="processForm">
            <div id="main-search" class="search-width">
                <div class="input-group mb-3">
                    <input class="form-control form-control-lg form-styling" placeholder="e.g. BIOL 300" v-model="course">
                    <div class="input-group-append">
                        <button class="btn btn-primary button-styling"><i class="py-1 fas fa-search"></i></button>
                    </div>
                </div>
            </div>
        </form>
    </div>
</div>
</template>

<script>


export default {
    data() {
        return {
            course: '',
        }
    },

    mounted() {

        //let $this = this;
        //let uri = window.location.search.substring(1);
        //let params = new URLSearchParams(uri);
        //this.course_param = params.get("course");

        this.course = this.$route.query.course.toUpperCase()
    },

    methods: {
        processForm: function() {

            // send course
            //location.href = "/course-search/?course=" + this.course;
            // /history.pushState( {} , '', '/course-search/?course=' + this.course );
            this.$router.push('/course-search/?course=' + this.course.toUpperCase())

        }
    }

}
</script>

<style lang="scss">
.search-width {
    input {
        height: 3rem;
        font-size: 1.25rem;
        //border-radius: 0;
        //border: 0.04688rem solid #333;
        text-transform: uppercase;
    }
}
</style>
