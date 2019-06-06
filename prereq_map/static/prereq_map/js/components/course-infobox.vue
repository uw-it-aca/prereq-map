<template>
  <div>
    <div v-if="course_code" class="card mt-4">
      <div v-if="loading">
        <div class="card-header bg-white">
          Loading.....
        </div>
      </div>
      <div v-else>
        <div class="card-header bg-white">
          <h5 class="m-0">
            {{ course_code }}
          </h5>

          <p v-if="course_description" class="card-title">
            {{ course_description }}
          </p>

          <a
            :href="'/course-search/?course=' + course_code"
            class="btn btn-primary btn-sm prereq-infobox-button"
            >More details</a
          >
        </div>
        <div class="card-body bg-light">
          <h5 class="card-title h6">
            Is a prerequisite for:
          </h5>
          <ul class="prereq-list">
            <li v-if="postreqs.length === 0">
              none
            </li>
            <li v-for="postreq in postreqs" :key="postreq">
              <a :href="'/course-search/?course=' + postreq">{{ postreq }}</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
//import { dataBus } from "../pages/course/";
import Vue from "vue/dist/vue.esm.js";

const axios = require("axios");
export default {
  data() {
    return {
      loading: true,
      course_code: "",
      last_selected: "",
      prereqs: [],
      postreqs: [],
      course_data: undefined,
      course_description: ""
    };
  },
  mounted() {
    this.course_code = this.$route.query.course;
    if (this.course_code !== undefined) {
      this.show(this.course_code);

      // update page title
      document.title = this.course_code + " - Curriculum Search - Prereq Map";
    }

    // global click handler for show node event
    $(document).on("showCourseInfo", (event, course_code) => {
      this.show(course_code);

      // https://developers.google.com/analytics/devguides/collection/analyticsjs/events
      // google event category, action, label, value
      this.$ga.event("curric map", "clicked course node", course_code);
    });

    // global click handler for close node event

    $(document).on("closeCourseInfo", event => {
      this.close();
    });
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
    },
    show: function(code) {
      this.loading = true;
      this.course_code = code;
      this.$router.push({
        query: Object.assign({}, this.$route.query, {
          course: this.course_code
        })
      });

      if (this.course_code !== undefined) {
        this.load_course(code);
      }
    },

    close: function() {
      // set course param to undefined in order to clear it out from query
      this.$router.replace({
        query: Object.assign({}, this.$route.query, { course: undefined })
      });
    }
  },

  watch: {
    "$route.query.course": function() {
      this.course_code = this.$route.query.course;
      this.show(this.course_code);

      if (this.course_code !== undefined) {
        // update page title
        document.title = this.course_code + " - Curriculum Search - Prereq Map";
      } else {
        // update page title
        document.title =
          this.$route.query.curric + " - Curriculum Search - Prereq Map";
      }
    },
    course_data: function() {
      this.prereqs = this.get_prereqs(
        this.course_code,
        this.course_data.data.x.edges.from
      );
      this.postreqs = this.get_postreqs(
        this.course_code,
        this.course_data.data.x.edges.to
      );
      this.course_description = this.course_data.data.course_description;
    }
  }
};
</script>

<style lang="scss">
.prereq-infobox-close {
  position: absolute;
  top: 0.375rem;
  right: 0.375rem;
  z-index: 10;
  display: block;
  padding: 0.25rem 0.5rem;
  color: #000;

  &:hover {
    color: #666;
  }
}

.prereq-infobox-button {
  background-color: #4d307f;
  color: #fff;
  border: none;
}
</style>
