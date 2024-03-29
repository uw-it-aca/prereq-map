<template>
  <div>
    <div v-if="course_code" class="card">
      <div v-if="loading">
        <div class="pr-loading mt-5 mb-5">
          <div class="pr-loading-inner">
            <i class="fas fa-spinner fa-spin" />
            <span class="sr-only">Loading...</span>
          </div>
        </div>
      </div>
      <div v-else>
        <div class="card-header bg-white">
          <h2 class="m-0 h5">
            {{ course_code }}
          </h2>

          <!--  eslint-disable-next-line vue/no-v-html -->
          <p
            v-if="course_description"
            v-html="course_description"
            class="card-title"
          >
            {{ course_description }}
          </p>

          <router-link
            :to="'/course/?course=' + course_code"
            class="btn btn-primary btn-sm prereq-infobox-button"
          >
            More details
          </router-link>
        </div>
        <div class="card-body bg-light">
          <div>
            <small><strong class="text-dark">Prerequisites</strong> <span class="badge badge-pill badge-dark">{{ prereqs.length }}</span><span class="sr-only">courses</span></small>
          </div>
          <ul v-if="prereqs.length > 0" class="prereq-list">
            <li v-for="prereq in prereqs" :key="prereq">
              <router-link :to="'/course/?course=' + prereq" class="badge badge-light border">{{ prereq }}</router-link>
            </li>
          </ul>
          <div v-else class="mb-3">
            <small>This course has no prerequisites.</small>
          </div>
          <div>
            <small><strong class="text-dark">Available upon completion</strong> <span class="badge badge-pill badge-dark">{{ postreqs.length }}</span><span class="sr-only">courses</span></small>
          </div>
          <ul v-if="postreqs.length > 0" class="prereq-list">
            <li v-for="postreq in postreqs" :key="postreq">
              <router-link :to="'/course/?course=' + postreq" class="badge badge-light border">{{ postreq }}</router-link>
            </li>
          </ul>
          <div v-else>
            <small>This course is not a prerequisite for any other courses.</small>
          </div>
        </div>
      </div>
    </div>
    <b-card v-else class="shadow-sm">
      <b-card-text class="font-weight-lighter">
        Use the scroll function on your mouse or touchpad to zoom in and out The map only displays prerequisite relationships within the selected curriculum. View course details to see prerequisites from other curricula
      </b-card-text>
    </b-card>
  </div>
</template>

<script>
  import axios from "axios";
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

    watch: {
      "$route.query.course": function() {
        this.course_code = this.$route.query.course;
        this.show(this.course_code);
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
    },
    mounted() {
      this.course_code = this.$route.query.course;

      if (this.course_code !== undefined) {
        this.show(this.course_code);
      }

      // global click handler for show node event
      $(document).on("showCourseInfo", (event, course_code) => {
        this.show(course_code);
        // google event category, action, label, value
        this.$ga.event("curric map", "clicked course node", course_code);
      });

      // global click handler for close node event
      $(document).on("closeCourseInfo", () => {
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

        this.$router
          .push({
            query: Object.assign({}, this.$route.query, {
              course: this.course_code
            })
          })
          // eslint-disable-next-line no-unused-vars
          .catch(err => {});

        if (this.course_code !== undefined) {
          this.load_course(code);
        }
      },

      close: function() {
        // set course param to undefined in order to clear it out from query
        this.$router
          .replace({
            query: Object.assign({}, this.$route.query, { course: undefined })
          })
          // eslint-disable-next-line no-unused-vars
          .catch(err => {});
      }
    }
  };
</script>

<style lang="scss">
  .prereq-infobox-close {
    color: #000;
    display: block;
    padding: 0.25rem 0.5rem;
    position: absolute;
    right: 0.375rem;
    top: 0.375rem;
    z-index: 10;

    &:hover {
      color: #666;
    }
  }

  .prereq-infobox-button {
    background-color: #4d307f;
    border: transparent;
    color: #fff;
  }
</style>
