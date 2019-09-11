<template>
  <div v-if="curric_param !== undefined">
    <div class="row">
      <p class="col-sm-12">
        The following is a graph of courses, in this, Curriculum that have an association.
      </p>
      <div class="col-sm-9">
        <div v-bind:class="{'card shadow-sm prereq-graph' : graph_error === false}">
          <div id="graph_container" />
          <div v-if="graph_error === true">
            <p>
              The curriculum <strong>{{ curric_param }}</strong> did not display a
              graph. Here are some possible reasons:
            </p>

            <ul>
              <li>The curriculum code does not exist</li>
              <li>The map does not display graduate curriculum</li>
              <li>The curriculum does not have courses with prerequisites</li>
            </ul>

            <p>Remember to talk to your adviser when course planning.</p>
          </div>
        </div>
      </div>
      <div class="col-sm-3 pl-0">
        <curric-infobox v-if="graph_error === false" />
      </div>
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  import CurricInfoBox from "../components/curric-infobox.vue";

  export default {
    components: {
      "curric-infobox": CurricInfoBox
    },
    data() {
      return {
        curric_param: undefined,
        course_param: undefined,
        curric_data: [],
        course_list: [],
        graph_error: false,
        dataReady: false
      };
    },
    watch: {
      curric_data: function() {
        if (this.curric_data.length != 0) {
          this.graph_error = false;
          window.show_graph(this.curric_data, this.course_param);
        } else {
          this.graph_error = true;
          // hide the graph
          window.hide_graph();
        }
      },

      "$route.query.curric": function() {
        // react to route changes...
        this.curric_param = this.$route.query.curric;
        this.course_param = this.$route.query.course;

        // reset the graph state by showing the loading message and hiding the graphy
        //window.hide_graph();
        this.dataReady = false;

        // get the curric data
        if (this.curric_param !== undefined) {
          this.getCurric();
          // update page title
          document.title = this.curric_param + " - Curriculum Search - Prereq Map";
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
            this.graph_error = false;
          })
          .then(() => {
            this.dataReady = true;
          })
          .catch(() => {
            // show the graph error and clear previous curric data
            this.graph_error = true;
            this.curric_data = [];
          });
      }
    }
  };
</script>

<style lang="scss">
  .prereq-graph {
    height: 502px;
  }
</style>