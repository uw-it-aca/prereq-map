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
          <h3 class="card-title h6">
            Has the following prerequisite(s):
          </h3>
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
          <h3 class="card-title h6">
            Is a prerequisite for:
          </h3>
          <ul class="prereq-list">
            <li v-if="postreqs.length === 0">
              No other courses
            </li>
            <li v-for="postreq in postreqs" :key="postreq">
              <router-link :to="'/course/?course=' + postreq">
                {{ postreq }}
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <b-card v-else class="shadow-sm">
      <b-card-text>
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

        if (this.course_description) {
          // format the description (hack!)
          this.course_description = this.course_description.replace(
            "Prerequisite: ",
            "<br /><br /><strong>Prerequisite:</strong> "
          );
          this.course_description = this.course_description.replace(
            "Offered: ",
            "<br /><br /><strong>Offered:</strong> "
          );
        }
      }
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
