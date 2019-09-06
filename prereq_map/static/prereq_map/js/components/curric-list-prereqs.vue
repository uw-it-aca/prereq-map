<template>
  <div>
    <div v-if="dataReady">
      <div class="mb-3 pb-3 border-bottom">
        <p>Prerequisites <span class="badge badge-pill badge-dark">{{ prereqs.length }}</span></p>
        <ul v-if="prereqs.length > 0" class="prereq-list mb-2">
          <li v-for="prereq in prereqs" :key="prereq">
            <router-link :to="'/course/?course=' + prereq" class="badge badge-light border">{{ prereq }}</router-link>
          </li>
        </ul>
        <p v-else>
          This course has no prerequisites.
        </p>
      </div>
      <div>
        <p>Available upon completion <span class="badge badge-pill badge-dark">{{ postreqs.length }}</span></p>
        <ul v-if="postreqs.length > 0" class="prereq-list mb-2">
          <li v-for="postreq in postreqs.slice(0, 5)" :key="postreq">
            <router-link :to="'/course/?course=' + postreq" class="badge badge-light border">{{ postreq }}</router-link>
          </li>
          <li v-if="postreqs.length > 5">
            <router-link :to="'/course/?course=' + courseParam" title="Click for a full list of courses"><small>view more...</small></router-link>
          </li>
        </ul>
        <div v-else>
          This course has no postrequisites.
        </div>
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
</style>
