<template>
  <div class="row course-search">
    <div class="col-md-9">
      <b-form @submit.prevent="processForm">
        <b-input-group>
          <b-form-input
            v-model="course_name"
            type="text"
            aria-label="Enter a course code... (e.g MATH 124)"
            placeholder="Enter a course code... (e.g MATH 124)"
            size="lg"
            list="my-course-list-id"
            autocomplete="off"
          />
          <b-form-datalist id="my-course-list-id" :options="course_list" />
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
        course_code: undefined,
        course_name: undefined,
        course_list: [
          'A A 260: Thermodynamics',
          'A S 101: Foundations of the United States Air Force I',
          'ANTH 203: Introduction to Anthropological Linguistics',
          'ANTH 208: The Culture Concept',
          'CSE 142: Computer Programming I',
          'CSE 143: Computer Programming II',
          'CSE 154: Web Programming',
          'CSE 160: Data Programming',
          'CSE 311: Foundations of Computing I',
          'MATH 100: Algebra',
          'MATH 102: Algebra',
          'MATH 103: Introduction to Elementary Functions',
          'MATH 108: International Baccalaureate (IB) Mathematical Studies',
          'MATH 111: Algebra with Applications',
          'MATH 120: Precalculus',
          'MATH 124: Calculus with Analytic Geometry I',
          'MATH 300: Introduction to Mathematical Reasoning'
        ]
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

        // get the course_code from the course_name by stripping everything after :
        this.course_code = this.course_name.substring(0, this.course_name.indexOf(':'));

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
