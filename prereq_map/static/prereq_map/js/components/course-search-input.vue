<template>
  <div class="row course-search">
    <div class="col-md-9 offset-md-1">
      <form id="signup-form" @submit.prevent="processForm">
        <div id="main-search" class="search-width">
          <div class="input-group mb-3">
            <input
              class="form-control form-control-lg form-styling"
              placeholder="e.g. MATH 124"
              v-model="course_code"
            >
            <div class="input-group-append">
              <button class="btn btn-primary button-styling">
                <i class="py-1 fas fa-search"></i>
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

  mounted() {
    this.course_code = this.$route.query.course;
  },
  watch: {},
  methods: {
    processForm: function(e) {
      e.preventDefault();

      // don't allow empty searches
      if (this.course_code === "" || this.course_code === undefined) {
        this.$router.push("/course-search/");
      } else {
        this.$router.push(
          "/course-search/?course=" + this.course_code.toUpperCase()
        );
      }
    }
  }
};
</script>

<style lang="scss">
  .search-width {
    input {
      height: 3rem;
      font-size: 1.25rem;
      text-transform: uppercase;
    }
  }
</style>
