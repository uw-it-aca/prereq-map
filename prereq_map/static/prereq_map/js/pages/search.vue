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
        <b-form-group label="Find prerequisite information by:">
          <b-form-radio-group
            v-model="selected"
            v-on:change="rememberChoice()"
            :options="options"
            name="radio-inline"
          />
        </b-form-group>
        <curric-typeahead v-if="selected === 'curric'" />
        <course-search v-if="selected === 'course'" />
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <h2 class="h4">
          Discover
        </h2>
      </b-col>
    </b-row>
    <b-row>
      <b-col md="4" class="mb-3">
        <b-card title="Bothell" sub-title="New courses" class="shadow-sm">
          <b-card-text>
            <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
            <div><a href="/curriculum/?curric=MATH">Mathematics (MATH)</a></div>
          </b-card-text>
        </b-card>
      </b-col>
      <b-col md="4" class="mb-3">
        <b-card title="Seattle" sub-title="New courses" class="shadow-sm">
          <b-card-text>
            <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
            <div><a href="/course/?course=MATH 124">MATH 124</a></div>
          </b-card-text>
        </b-card>
      </b-col>
      <b-col md="4" class="mb-3">
        <b-card title="Tacoma" sub-title="New courses" class="shadow-sm">
          <b-card-text>
            <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
            <div><a href="/course/?course=MATH 124">MATH 124</a></div>
          </b-card-text>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
  import CourseSearch from "../components/course-search.vue";
  import UserAccept from "../components/user-accept.vue";
  import Typeahead from "../components/curric-typeahead.vue";

  export default {
    name: "Search",
    components: {
      "user-accept": UserAccept,
      "curric-typeahead": Typeahead,
      "course-search": CourseSearch
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
