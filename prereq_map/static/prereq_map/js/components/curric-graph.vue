<template>
  <div v-if="curric_param !== undefined">
    <div>
      <small
        v-if="graph_error === false"
        class="text-secondary"
      >Use the scroll function on your mouse or touchpad to zoom in and out</small>
      <div id="graph_container" />
    </div>
    <div v-if="graph_error === true">
      <p>
        The curriculum
        <strong>{{ curric_param }}</strong> did not display a graph. Here are some possible reasons:
      </p>
      <ul>
        <li>The curriculum code does not exist</li>
        <li>The map does not display graduate curriculum</li>
        <li>The curriculum does not have courses with prerequisites</li>
      </ul>
      <p>Remember to talk to your adviser when course planning.</p>
    </div>
  </div>
</template>

<script>
  const axios = require("axios");
  export default {
    data() {
      return {
        curric_param: undefined,
        course_param: undefined,
        curric_data: [],
        course_list: [],
        graph_error: undefined
      };
    },

    watch: {
      curric_data: function() {
        window.show_graph(this.curric_data, this.course_param);
      },

      "$route.query.curric": function() {
        // react to route changes...
        this.curric_param = this.$route.query.curric;
        this.course_param = this.$route.query.course;

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

            this.graph_error = false;
            this.loading = false;
          })
          // eslint-disable-next-line no-unused-vars
          .catch(error => {
            this.graph_error = true;
          });
      }
    }
  };
</script>
