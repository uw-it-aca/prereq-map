// search.vue

<template>
  <b-container id="search">
    <user-accept />
    <b-row>
      <b-col>
        <h1 class="h3">
          Prerequisite Map
        </h1>
      </b-col>
    </b-row>
    <b-row class="justify-content-center course-search mt-5 mb-5">
      <b-col md="9">
        <b-form-group label="Find prerequisite information by:" class="text-muted">
          <b-form-radio-group
            v-model="selected"
            v-on:change="rememberChoice()"
            :options="options"
            name="radio-inline"
            size="md"
            buttons
            button-variant="outline-primary"
          />
        </b-form-group>
        <curric-typeahead v-if="selected === 'curric'" />
        <course-typeahead v-if="selected === 'course'" />
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
        options: [
          { text: 'Course', value: 'course' },
          { text: 'Curriculum', value: 'curric' }
        ]
      };
    },
    mounted() {
      document.title = "Prereq Map - University of Washington";
    },
    methods: {
      rememberChoice: function() {
        // eslint-disable-next-line no-console
        console.log("remember this!");
      }
    }
  };
</script>

<style lang="scss">
</style>
