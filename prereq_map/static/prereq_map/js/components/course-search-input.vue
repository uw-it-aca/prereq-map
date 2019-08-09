<template>
  <div class="row course-search">
    <div class="col-md-9 offset-md-1">
      <form id="signup-form" @submit.prevent="processForm">
        <div id="main-search" class="search-width">
          <div class="input-group mb-3">
            <input
              v-model="course_code"
              class="form-control form-control-lg form-styling"
              placeholder="e.g. MATH 124"
            >
            <div class="input-group-append">
              <button class="btn btn-primary button-styling">
                <i class="py-1 fas fa-search" />
              </button>
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
        course_code: undefined
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
    },
    methods: {
      processForm: function(e) {
        e.preventDefault();

        // don't allow empty searches
        if (this.course_code === "" || this.course_code === undefined) {
          // eslint-disable-next-line no-unused-vars
          this.$router.push("/course/").catch(err => {});
        } else {
          this.$router.push(
            "/course/?course=" + this.course_code.toUpperCase()
          // eslint-disable-next-line no-unused-vars
          ).catch(err => {});
        }
      }
    }
  };
</script>

<style lang="scss">
  .search-width {
    input {
      font-size: 1.25rem;
      height: 3rem;
      text-transform: uppercase;
    }
  }
</style>
