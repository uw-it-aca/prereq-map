<template>
  <div>
    <b-container v-if="dataReady" class="">
      <b-row>
        <b-col sm="6" class="p-0 mb-3">
          <div>
            <small><strong class="text-dark">Prerequisites</strong> <span class="badge badge-pill badge-light border">{{ prereqs.length }}</span><span class="sr-only">courses</span></small>
          </div>
          <ul v-if="prereqs.length > 0" class="prereq-list">
            <li v-for="prereq in prereqs" :key="prereq">
              <router-link :to="'/course/?course=' + prereq" class="badge badge-light border">{{ prereq }}</router-link>
            </li>
          </ul>
          <div v-else>
            <small>This course has no prerequisites.</small>
          </div>
        </b-col>
        <b-col sm="6" class="p-0">
          <div>
            <small><strong class="text-dark">Available upon completion</strong> <span class="badge badge-pill badge-light border">{{ postreqs.length }}</span><span class="sr-only">courses</span></small>
          </div>
          <ul v-if="postreqs.length > 0" class="prereq-list">
            <li v-for="postreq in postreqs.slice(0, 7)" :key="postreq">
              <router-link :to="'/course/?course=' + postreq" class="badge badge-light border">{{ postreq }}</router-link>
            </li>
            <li v-if="postreqs.length > 7">
              <router-link :to="'/course/?course=' + courseParam" title="Click for a full list of courses"><small>view more...</small></router-link>
            </li>
          </ul>
          <div v-else>
            <small>This course is not a prerequisite for any other courses.</small>
          </div>
        </b-col>
      </b-row>
    </b-container>
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
  .badge { font-weight: normal; }
</style>
