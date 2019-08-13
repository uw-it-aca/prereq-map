<template>
  <div v-cloak class="col course-detail">
    <div class="row">
      <div class="col-md-5 pb-5">
        <div>
          <course-graph :course-param="courseParam" />
        </div>
      </div>
      <div class="col-md-7">
        <div class="mb-4">
          <h2 class="pt-3">
            <span>{{ courseParam }}</span>
            <span v-if="course_title">- {{ course_title }}</span>
          </h2>
          <!--  eslint-disable-next-line vue/no-v-html -->
          <div v-if="course_description" v-html="course_description">
            {{ course_description }}
          </div>
        </div>

        <div class="mb-4">
          <strong>Is a prerequisite for:</strong>
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

        <strong>Additional information:</strong>
        <p>
          <a
            :href="'https://myplan.uw.edu/course/#/courses/' + courseParam"
            @keydown="
              $ga.event(
                'outbound',
                'click',
                'https://myplan.uw.edu/course/#/courses/' + courseParam
              )
            "
            @click="
              $ga.event(
                'outbound',
                'click',
                'https://myplan.uw.edu/course/#/courses/' + courseParam
              )
            "
            target="_blank"
          >
            View {{ courseParam }} course details and schedule on MyPlan
          </a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
  import Graph from "./course-graph.vue";
  import { dataBus } from "../main.js";

  export default {
    name: "CourseDetail",
    components: {
      "course-graph": Graph
    },
    props: {
      courseParam: {
        type: String,
        default: ""
      }
    },
    data() {
      return {
        course_title: "",
        course_description: "",
        prereqs: [],
        postreqs: []
      };
    },
    watch: {},
    mounted() {
      // get the course title, desc, and prereqs from the databus
      dataBus.$on("course_data", data => {
        this.course_title = data.course_title;
        this.course_description = data.course_description;

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

        this.prereqs = this.get_prereqs(this.courseParam, data.x.edges.from);
        this.postreqs = this.get_postreqs(this.courseParam, data.x.edges.to);
      });
    },
    methods: {
      get_prereqs: function(course, from_list) {
        var keys = Object.keys(from_list);
        var from = [];
        keys.forEach(function(key) {
          var value = from_list[key];
          if (course !== value && !from.includes(value)) {
            from.push(value);
          }
        });
        return from;
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
        return to;
      }
    }
  };
</script>
