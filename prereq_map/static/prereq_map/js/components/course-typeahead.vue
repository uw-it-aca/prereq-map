<template>
  <div class="row course-search">
    <div class="col">
      <b-form @submit.prevent="processForm">
        <b-input-group>
          <b-form-input
            v-bind:size="$route.path == '/course/' ? 'md': 'lg'"
            v-model="course_name"
            type="text"
            aria-label="Enter course name or code... (e.g Calculus, MATH 124)"
            placeholder="Enter course name or code... (e.g Calculus, MATH 124)"
            list="my-course-list-id"
            autocomplete="off"
          />
          <b-form-datalist id="my-course-list-id" :options="course_list" />
          <b-input-group-append>
            <b-button v-bind:variant="$route.path == '/course/' ? 'light': 'primary'" class="border-left" type="submit">
              Search
            </b-button>
          </b-input-group-append>
        </b-input-group>
      </b-form>
    </div>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    data() {
      return {
        course_code: undefined,
        course_name: undefined,
        course_list: undefined,
      };
    },
    watch: {
      // make sure course codes persists between query param changes
      "$route.query.course": function() {
        this.course_code = this.$route.query.course;
      }
    },
    mounted() {
      this.course_code = this.$route.query.course;
      // get curric data from api
      this.getCourseData();
    },
    methods: {
      processForm: function(e) {
        e.preventDefault();

        // get the course_code from the course_name by stripping everything after :
        this.course_code = this.course_name.substring(0, this.course_name.indexOf(':'));

        // don't allow empty searches
        if ( this.course_code.length > 0) {
          // eslint-disable-next-line no-unused-vars
          this.$router.push("/course/?course=" + this.course_code.toUpperCase()).catch(err => {});
        }


      },
      uppercase(value) {
        return value.toUpperCase();
      },
      getCourseData: function() {

        // get the list of currics and store in an array
        return axios
          .get("/api/course_typeahead")
          .then(response => {
            // store the response data into an object
            this.course_list = response.data;
          })
          .catch(() => {});
      }
    }
  };
</script>

<style lang="scss">
</style>
