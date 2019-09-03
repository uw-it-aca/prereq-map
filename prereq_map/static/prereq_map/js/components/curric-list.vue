<template>
  <div v-if="curric_param !== undefined" style="outline: solid 1px #f00;">
    <p>The following is a list of courses in this Curriculum that have an association.</p>

    <div v-if="list_error === true">
      <p>
        The curriculum <strong>{{ curric_param }}</strong> did not display a
        list. Here are some possible reasons:
      </p>

      <ul>
        <li>The curriculum code does not exist</li>
        <li>The map does not display graduate curriculum</li>
        <li>The curriculum does not have courses with prerequisites</li>
      </ul>

      <p>Remember to talk to your adviser when course planning.</p>
    </div>

    <ul v-if="list_error === false" class="list-unstyled">
      <li v-for="course in course_list">
        <router-link :to="'/course/?course=' + course.courseCode">
          {{ course.courseCode }}
        </router-link> {{ course.title }}

        <curric-list-prereqs />
      </li>
    </ul>
  </div>
</template>

<script>
  import axios from "axios";
  import CurricListPrereqs from "../components/curric-list-prereqs.vue";

  export default {
    components: {
      "curric-list-prereqs": CurricListPrereqs
    },
    data() {
      return {
        curric_param: undefined,
        curric_data: {},
        course_list: [],
        list_error: undefined
      };
    },
    watch: {
      "$route.query.curric": function() {
        // react to route changes...
        this.curric_param = this.$route.query.curric;

        if (this.curric_param !== undefined) {
          this.getCurric();

          // update page title
          document.title =
            this.curric_param + " - Curriculum Search - Prereq Map";
        }
      }
    },
    mounted() {
      this.curric_param = this.$route.query.curric;

      if (this.curric_param !== undefined) {
        this.getCurric();
      }
    },
    methods: {
      getCurric: function() {
        return axios
          .get("/api/curric/" + encodeURI(this.curric_param))
          .then(response => {
            // store the response data into an object
            this.curric_data = response.data;
            this.list_error = false;
          })
          .then(() => {
            // get the corresponding list of courses
            this.get_courses();
          })
          .catch(() => {
            // show the graph error and clear previous curric data
            this.list_error = true;
            this.curric_data = [];
            this.course_list = [];
          });
      },
      get_courses: function() {

        // start with a fresh empty list of courses
        this.course_list= [];

        let nodes = this.curric_data.x.nodes;
        let nodeslen = Object.values(nodes.course_number).length;

        // loop through the nodes
        for (let i = 0; i < nodeslen; i++) {
          let courseObj = {};
          // get the specific node object and assign it to the temp courseObj
          courseObj.courseCode = nodes.department_abbrev[i] + " " + nodes.course_number[i];
          courseObj.title = nodes.course_title[i];
          // save the courseObj to the global course list used by the template
          this.course_list.push(courseObj);
        }

      },
    }
  };
</script>
