<template>
  <div v-cloak v-if="courseParam !== undefined" class="card shadow-sm">
    <div class="text-dark p-3 bg-light rounded-top rounded-sm">
      <small>Use the scroll function on your mouse or touchpad to zoom in and out</small>
    </div>
    <div id="graph_container" />
  </div>
</template>

<script>
  import axios from "axios";
  import { dataBus } from "../main.js";

  export default {
    props: {
      courseParam: {
        type: String,
        default: ""
      }
    },
    data() {
      return {
        course_data: undefined
      };
    },

    watch: {
      course_data: function() {
        window.show_graph(this.course_data.data, this.courseParam);
        dataBus.$emit("course_data", this.course_data.data);
      },

      "$route.query.course": function() {
        // react to route changes...
        if (this.courseParam !== undefined) {
          axios
            .get("/api/course/" + encodeURI(this.courseParam))
            .then(response => (this.course_data = response));
        }
      }
    },
    mounted() {
      if (this.courseParam !== undefined) {
        axios
          .get("/api/course/" + encodeURI(this.courseParam))
          .then(response => (this.course_data = response));
      }
    }
  };
</script>
