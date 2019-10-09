// course.vue

<template>
  <div id="course" class="container">
    <div v-if="loading" class="pr-loading">
      <div>
        <i class="fas fa-spinner fa-spin" />
        <span class="sr-only">Loading...</span>
      </div>
    </div>
    <div v-cloak v-if="course_param !== undefined">
      <div v-if="course_valid && loading === false" class="row">
        <course-detail :course-param="course_param" />
      </div>
      <div v-cloak v-if="course_valid === false" class="row">
        <div class="col">
          <h1 class="h3 mb-3">
            No Prerequisite Info
          </h1>
          <p class="font-weight-lighter">
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

          <p class="font-weight-lighter">
            Remember to talk to your adviser when course planning.
          </p>
        </div>
      </div>
    </div>
    <div v-else>
      <h1 class="h3 mb-3">
        Courses
      </h1>
      <p class="font-weight-lighter">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus
        elementum dignissim imperdiet. Vivamus maximus felis sed risus eleifend
        condimentum. Aliquam id lacus condimentum, tempus justo quis, mollis
        odio. Etiam feugiat efficitur maximus. Etiam dignissim pharetra congue.
        Donec laoreet condimentum orci, eu condimentum nulla condimentum
        consectetur. Etiam et urna aliquam, suscipit ante in, pharetra turpis.
        Phasellus ut finibus dolor. Quisque gravida nisi mi, ac gravida felis
        dapibus eget. Sed at lectus venenatis, convallis dui eu, venenatis
        dolor. Nunc sed leo sagittis, ornare tortor a, pretium leo. Quisque enim
        nunc, fringilla at sapien sodales, tincidunt ultrices eros.
      </p>
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  //import CourseSearch from "../components/course-search.vue";
  import CourseDetail from "../components/course-detail.vue";

  export default {
    name: "Course",
    components: {
      //"course-search": CourseSearch,
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
          document.title =
            this.course_param +
            " - Course - Prereq Map - University of Washington";
        } else {
          this.loading = undefined;
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
        document.title =
          this.course_param + " - Course - Prereq Map - University of Washington";
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
            this.loading = undefined;
            //console.log("error " + error);
          });
      }
    }
  };
</script>

<style lang="scss">
</style>
