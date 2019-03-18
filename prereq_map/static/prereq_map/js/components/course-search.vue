<template>
<div style="margin-bottom:25px;" class="course-search">
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

    methods: {
        processForm: function() {

            // send course
            window.location.href = "/course-search/?course=" + this.course;

        }
    }

}
</script>

<style scoped>
.course-search {
    border: solid 1px lime;
    padding: 10px;
}
</style>
