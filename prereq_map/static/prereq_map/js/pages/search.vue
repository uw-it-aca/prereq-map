// search.vue

<template>
  <b-container id="search">
    <user-accept />
    <b-row class="justify-content-center">
      <b-col md="9">
        <h1 class="h3 sr-only">
          Prerequisite Map
        </h1>
        <b-card bg-variant="light" text-variant="dark">
          <b-form-group label="Find prerequisites by:">
            <b-form-radio v-model="selected" inline name="some-radios" value="course" size="lg">
              Course
            </b-form-radio>
            <b-form-radio v-model="selected" inline name="some-radios" value="curric" size="lg">
              Curriculum
            </b-form-radio>
          </b-form-group>
          <curric-typeahead v-if="selected === 'curric'" />
          <course-typeahead v-if="selected === 'course'" />
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
  import CourseTypeahead from "../components/course-typeahead.vue";
  import CurricTypeahead from "../components/curric-typeahead.vue";
  import UserAccept from "../components/user-accept.vue";

  export default {
    name: "Search",
    components: {
      "user-accept": UserAccept,
      "curric-typeahead": CurricTypeahead,
      "course-typeahead": CourseTypeahead
    },
    data() {
      return {
        selected: 'course',
      };
    },
    mounted() {
      document.title = "Prereq Map - University of Washington";
    },
    methods: {}
  };
</script>

<style lang="scss">
</style>
