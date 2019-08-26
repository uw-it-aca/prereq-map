<template>
  <div class="row course-search mt-4 mb-4">
    <div class="col-md-9 offset-md-1">
      <b-form @submit.prevent="processForm">
        <b-input-group>
          <b-form-input
            v-model="course_code"
            :formatter="uppercase"
            type="text"
            aria-label="Enter a course code... (e.g MATH 124)"
            placeholder="Enter a course code... (e.g MATH 124)"
            size="lg"
            autocomplete="off"
          />
          <b-input-group-append>
            <b-button variant="primary" type="submit">
              Search
            </b-button>
          </b-input-group-append>
        </b-input-group>
      </b-form>
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
          this.$router
            .push("/course/?course=" + this.course_code.toUpperCase())
            // eslint-disable-next-line no-unused-vars
            .catch(err => {});
        }
      },
      uppercase(value) {
        return value.toUpperCase();
      }
    }
  };
</script>

<style lang="scss">
</style>
