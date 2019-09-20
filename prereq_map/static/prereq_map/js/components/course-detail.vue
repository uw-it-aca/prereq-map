<template>
  <div v-cloak class="col course-detail">
    <div class="row">
      <div class="col-md-5">
        <div class="mb-3">
          <h1 class="h3">
            {{ courseParam }}<span v-if="course_title">: {{ course_title }}</span>
          </h1>
          <!--  eslint-disable-next-line vue/no-v-html -->
          <div v-if="course_description" v-html="course_description" class="border border-danger">
            {{ course_description }}
          </div>
        </div>

        <b-row>
          <b-col class="mb-3">
            <h2 class="h6">
              Prerequisites <span class="badge badge-pill badge-dark">{{ prereqs.length }}</span><span class="sr-only">courses</span>
            </h2>
            <ul v-if="prereqs.length > 0" class="prereq-list">
              <li v-for="prereq in prereqs" :key="prereq">
                <router-link :to="'/course/?course=' + prereq" class="badge badge-light border">{{ prereq }}</router-link>
              </li>
            </ul>
            <div v-else>
              <small>This course has no prerequisites.</small>
            </div>
          </b-col>
        </b-row>
        <b-row>
          <b-col class="mb-3">
            <h2 class="h6">
              Available upon completion <span class="badge badge-pill badge-dark">{{ postreqs.length }}</span><span class="sr-only">courses</span>
            </h2>
            <ul v-if="postreqs.length > 0" class="prereq-list">
              <li v-for="postreq in postreqs" :key="postreq">
                <router-link :to="'/course/?course=' + postreq" class="badge badge-light border">{{ postreq }}</router-link>
              </li>
            </ul>
            <div v-else>
              <small>This course is not a prerequisite for any other courses.</small>
            </div>
          </b-col>
        </b-row>
        <h2 class="h6">
          Additional information
        </h2>
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
      <div class="col-md-7" aria-hidden="true">
        <course-graph :course-param="courseParam" />
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
