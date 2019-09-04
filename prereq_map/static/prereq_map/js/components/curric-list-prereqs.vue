<template>
  <div>
    <div v-if="dataReady">
      <small>prereqs ({{ prereqs.length }})</small>
      <ul class="prereq-list">
        <li v-if="prereqs.length === 0">
          No other courses
        </li>
        <li v-for="prereq in prereqs" :key="prereq">
          <router-link :to="'/course/?course=' + prereq">
            {{ prereq }}
          </router-link>
        </li>
      </ul>
      <small>postreqs (showing 5 of {{ postreqs.length }})</small>
      <ul class="prereq-list">
        <li v-if="postreqs.length === 0">
          No other courses
        </li>
        <li v-for="(postreq, index) in postreqs" v-if="index <= 4" :key="postreq">
          <router-link :to="'/course/?course=' + postreq">
            {{ postreq }}
          </router-link>
        </li>
      </ul>
      <div v-if="postreqs.length > 4">
        There are more postres! Click details to see full list.
      </div>
    </div>
    <div v-else>
      Loading...
    </div>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    props: {
      courseParam: {
        type: String,
        required: true
      }
    },
    data() {
      return {
        course_data: undefined,
        prereqs: [],
        postreqs: [],
        dataReady: false
      };
    },

    watch: {
      course_data: function() {
        this.prereqs = this.get_prereqs(
          this.courseParam,
          this.course_data.data.x.edges.from
        );
        this.postreqs = this.get_postreqs(
          this.courseParam,
          this.course_data.data.x.edges.to
        );
      }
    },
    mounted() {
      this.load_course(this.courseParam);
    },

    methods: {
      load_course: function(course_code) {
        axios
          .get("/api/course/" + encodeURI(course_code))
          .then(response => {
            this.course_data = response;
          })
          .then(() => {
            //console.log(this.course_data);
            this.dataReady = true;
          })
          .catch(() => {});
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

  small { text-transform: uppercase; }

</style>
