<template>
  <div v-if="curric_param !== undefined" style="outline: solid 1px #f00;">
    <p>The following is a list of courses in this Curriculum that have an association.</p>
    <p>The param: {{ curric_param }}</p>

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

    <ul v-if="list_error === false" v-for="course in course_list" class="list-unstyled">
      <li>
        <a href="#">{{ course.curric }} {{ course.code }}</a> {{ course.title }}
        <p>
          Prerequisite: none<br>
          Is a prerequisite for: ANTH 303, BIO A 420
        </p>
      </li>
    </ul>
  </div>
</template>

<script>
  import axios from "axios";
  export default {
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

            this.get_courses();


          })
          .catch(() => {
            // show the graph error and clear previous curric data
            this.list_error = true;
            this.curric_data = [];
          });
      },
      get_courses: function() {

        var nodes = this.curric_data.x.nodes;
        var nodeslen = Object.values(nodes.course_number).length;

        for (let i = 0; i < nodeslen; i++) {
            var courseObj = {};
            courseObj.curric = nodes.department_abbrev[i];
            courseObj.code = nodes.course_number[i];
            courseObj.title = nodes.course_title[i];
            this.course_list.push(courseObj);
            console.log(this.course_list);
        }


        // eslint-disable-next-line no-console
        console.log(this.course_list);
        // eslint-disable-next-line no-console
        console.log(this.curric_data.x.nodes);

      },
    }
  };
</script>
