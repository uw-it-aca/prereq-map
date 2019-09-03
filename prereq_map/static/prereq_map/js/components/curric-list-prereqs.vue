<template>
  <div>
    <p>
      Prerequisite: none<br>
      Is a prerequisite for: ANTH 303, BIO A 420, asdfjasdfkl
    </p>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    data() {
      return {
        course_code: "",
        course_data: undefined,
        prereqs: [],
        postreqs: [],
      };
    },

    watch: {

    },
    mounted() {
      this.course_code = this.$route.query.course;

    },
    methods: {
      load_course: function(course_code) {
        axios.get("/api/course/" + encodeURI(course_code)).then(response => {
          this.course_data = response;
          this.loading = false;
        });
      },
      get_prereqs: function(course, from_list) {
        var keys = Object.keys(from_list);
        var from = [];
        keys.forEach(function(key) {
          var value = from_list[key];
          if (course !== value && !from.includes(value)) {
            from.push(value);
          }
        });
        return from.sort();
      },
      get_postreqs: function(course, to_list) {
        var keys = Object.keys(to_list);
        var to = [];
        keys.forEach(function(key) {
          var value = to_list[key];
          if (course !== value && !to.includes(value)) {
            to.push(value);
          }
        });
        return to.sort();
      }
    }
  };
</script>

<style lang="scss">

</style>
