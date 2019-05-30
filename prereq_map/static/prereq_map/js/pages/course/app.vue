<template>
  <div 
    id="course" 
    class="container py-1 mt-2" 
    role="main"
  >
    <h1 class="pt-4 pb-2">
      Course Search
    </h1>
    <p class="instruction-text pb-4">
      View course prerequisites and related curricula
    </p>

    <course-search-input />

    <div 
      v-cloak 
      v-if="course_param !== undefined"
    >
      <div 
        v-if="course_valid" 
        class="row mt-5 mb-5"
      >
        <course-detail :course-param="course_param" />
      </div>

      <div 
        v-cloak 
        v-if="course_valid === false" 
        class="row mt-5 mb-5"
      >
        <div class="col">
          <p>
            The course
            <strong>{{ course_param }}</strong> was not found. Here are some possible reasons:
          </p>

          <ul>
            <li>The course code does not exist</li>
            <li>The course is no longer offered</li>
            <li>The course is graduate level</li>
          </ul>

          <p>Remember to talk to your adviser when course planning.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  import CourseSearchInput from "../../components/course-search-input.vue";
  import CourseDetail from "../../components/course-detail.vue";

  export default {
    name: "Curriculum",
    components: {
      "course-search-input": CourseSearchInput,
      "course-detail": CourseDetail
    },
    data() {
      return {
        course_param: undefined,
        course_data: [],
        course_number: "",
        course_valid: undefined
      };
    },
    watch: {
      "$route.query.course": function() {
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
          })
          .catch(error => {
            this.course_valid = false;
            // eslint-disable-next-line no-console
            console.log("error " + error);
          });
      }
    }
  };
</script>

<style lang="scss">
</style>
