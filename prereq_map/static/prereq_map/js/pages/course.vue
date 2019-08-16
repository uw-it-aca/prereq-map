// course.vue

<template>
  <div id="course" class="container py-1 mt-2">
    <h1 class="pt-4 pb-2">
      Course Search
    </h1>
    <p class="instruction-text pb-4">
      View course prerequisites and related curricula
    </p>

    <course-search-input />

    <div v-if="loading" class="pr-loading mt-5 mb-5">
      <div>
        <i class="fas fa-spinner fa-spin" />
        <span class="sr-only">Loading...</span>
      </div>
    </div>

    <div v-cloak v-if="course_param !== undefined">
      <div v-if="course_valid && loading === false" class="row mt-5 mb-5">
        <course-detail :course-param="course_param" />
      </div>

      <div v-cloak v-if="course_valid === false" class="row mt-5 mb-5">
        <div class="col">
          <p>
            No prerequisite information for
            <strong>{{ course_param }}</strong> was found. Here are some
            possible reasons:
          </p>

          <ul>
            <li>
              It does not have prereqs and/or isn't a prereq for other courses
            </li>
            <li>It is no longer offered</li>
            <li>It is a graduate level course</li>
            <li>You made a typo – the course code doesn't exist</li>
          </ul>

          <p>Remember to talk to your adviser when course planning.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  import CourseSearchInput from "../components/course-search-input.vue";
  import CourseDetail from "../components/course-detail.vue";

  export default {
    name: "Course",
    components: {
      "course-search-input": CourseSearchInput,
      "course-detail": CourseDetail
    },
    data() {
      return {
        loading: undefined,
        course_param: undefined,
        course_data: [],
        course_number: "",
        course_valid: undefined
      };
    },
    watch: {
      "$route.query.course": function() {
        this.loading = true;

        this.course_param = this.$route.query.course;
        if (this.course_param !== undefined) {
          this.getCourse();
          // update page title
          document.title = this.course_param + " - Course Search - Prereq Map";
        }
      }
    },
    mounted() {
      this.course_param = this.$route.query.course;

      if (this.course_param !== undefined) {
        // show the loading spinner when a course param is passed
        this.loading = true;
        this.getCourse();
        // update page title
        document.title = this.course_param + " - Course Search - Prereq Map";
      }
    },
    methods: {
      getCourse: function() {
        return axios
          .get("/api/course/" + encodeURI(this.course_param))
          .then(response => {
            this.course_data = response.data;
            this.course_number = this.course_data.x.nodes.course_number;

            // check to see if course_list is empty
            if (Object.keys(this.course_number).length !== 0) {
              this.course_valid = true;
            } else {
              this.course_valid = false;
            }

            // hide the loading spinner to show responses
            this.loading = false;
          })
          .catch(() => {
            this.course_valid = false;
            // hide the loading spinner to show responses
            this.loading = false;
            //console.log("error " + error);
          });
      }
    }
  };
</script>

<style lang="scss">
</style>
