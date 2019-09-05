<template>
  <div>
    <div v-if="dataReady">
      <div class="d-flex">
        <div class="w-100">
          <small><span class="text-uppercase">Prerequisites</span> ({{ prereqs.length }})</small>
          <ul v-if="prereqs.length > 0" class="prereq-list mb-2">
            <li v-for="prereq in prereqs" :key="prereq">
              <router-link :to="'/course/?course=' + prereq">{{ prereq }}</router-link>
            </li>
          </ul>
          <p v-else>
            This course has no prerequisites.
          </p>
        </div>
        <div class="w-100">
          <small v-if="postreqs.length > 5"><span class="text-uppercase">Postrequisites</span> (showing 5 of {{ postreqs.length }})</small>
          <small v-else><span class="text-uppercase">postreqs</span> ({{ postreqs.length }})</small>
          <ul v-if="postreqs.length > 0" class="prereq-list mb-2">
            <li v-for="(postreq, index) in postreqs" v-if="index < 5" :key="postreq">
              <router-link :to="'/course/?course=' + postreq">{{ postreq }}</router-link>
            </li>
          </ul>
          <p v-else>
            This course has no postrequisites.
          </p>
          <div v-if="postreqs.length > 5">
            <router-link :to="'/course/?course=' + courseParam">View {{ courseParam }} course details to see more postrequisites</router-link>
          </div>
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
