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

    <ul v-if="list_error === false" class="list-unstyled">
      <li>
        <strong><a href="#">ANTH 215</a> Technologies of Health (5) I&S/VLPA</strong>
        <p>
          Prerequisite: none<br>
          Is a prerequisite for: ANTH 303, BIO A 420
        </p>
      </li>
      <li>
        <strong><a href="#">ANTH 303</a> Technologies of Health (5) I&S/VLPA</strong>
        <p>
          Prerequisite: ANTH 208, ANTH 215, or ANTH 302.<br>
          Is a prerequisite for: No other courses
        </p>
      </li>
      <li>
        <strong><a href="#">ANTH 314</a> Ethnography, Transnationalism, and Community in Island Southeast Asia/Asian America (5) I&amp;S, DIV</strong>
        <p>
          Prerequisite: either one 200-level ANTH course or one AAS/AES course.<br>
          Is a prerequisite for: No other courses
        </p>
      </li>
      <li>
        <strong><a href="#">ANTH 318</a> Anthropology of Islam and Muslim Societies (3/5) I&amp;S</strong>
        <p>
          Prerequisite: one 200-level anthropology course.<br>
          Is a prerequisite for: No other courses
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
        curric_data: [],
        course_list: [],
        list_error: undefined
      };
    },
    watch: {

      curric_data: function() {
        if (this.curric_data.length != 0) {
          // show the graph
          window.show_graph(this.curric_data, this.course_param);
        } else {
          this.list_error = true;
          // hide the graph
          window.hide_graph();
        }
      },

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
      this.course_param = this.$route.query.course;

      if (this.curric_param !== undefined) {
        this.getCurric();

        // update page title
        document.title = this.curric_param + " - Curriculum Search - Prereq Map";
      }
    },
    methods: {
      getCurric: function() {
        return axios
          .get("/api/curric/" + encodeURI(this.curric_param))
          .then(response => {
            this.curric_data = response.data;
            this.list_error = false;
          })
          .catch(() => {
            // show the graph error and clear previous curric data
            this.list_error = true;
            this.curric_data = [];
          });
      }
    }
  };
</script>
