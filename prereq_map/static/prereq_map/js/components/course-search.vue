<template>
<div class="course-search">
    <form id="signup-form" @submit.prevent="processForm">
        <div id="main-search" class="search-width">
            <div class="d-table-cell w-100">
                <input class="form-control form-control-lg form-styling" placeholder="e.g. BIOL 300" v-model="course">
            </div>
            <div class="d-table-cell align-middle">
                <button class="btn btn-primary button-styling"><i class="py-1 fas fa-search"></i></button>
            </div>
        </div>
    </form>
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

        this.course = this.$route.query.course
    },

    methods: {
        processForm: function() {

            // send course
            //location.href = "/course-search/?course=" + this.course;
            // /history.pushState( {} , '', '/course-search/?course=' + this.course );
            this.$router.push('/course-search/?course=' + this.course)

        }
    }

}
</script>
