// curriculum.vue

<template>
  <div id="curriculum" class="container">
    <user-accept />
    <h1>Curriculum Search</h1>
    <p>View the prerequisite map of courses in a curriculum</p>

    <curric-typeahead />

    <div class="row">
      <div class="col-md-12">
        <h2>{{ curric_name }}</h2>
      </div>
    </div>
    <div class="row">
      <div class="col-md-9">
        <curric-graph />
      </div>
      <div class="col-sm-12 col-md-3">
        <course-infobox />
      </div>
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  import UserAccept from "../components/user-accept.vue";
  import CourseInfoBox from "../components/course-infobox.vue";
  import Typeahead from "../components/curric-typeahead.vue";
  import Graph from "../components/curric-graph.vue";

  export default {
    name: "Curriculum",
    components: {
      "user-accept": UserAccept,
      "curric-typeahead": Typeahead,
      "curric-graph": Graph,
      "course-infobox": CourseInfoBox
    },
    data() {
      return {
        curric_name: undefined,
        curric_param: undefined,
      };
    },
    watch: {
      // watch changes in curric param route changes
      "$route.query.curric": function() {
        this.curric_param = this.$route.query.curric;
        if (this.curric_param !== undefined) {
          // set the curric name based on the curric code
          this.curric_name = this.getCurricName(this.curric_param);
        } else {
          this.curric_name = undefined;
        }
      }
    },
    mounted() {
      document.title = "Curriculum Search - Prereq Map";

      // if the param was included in the request... convert it
      this.curric_param = this.$route.query.curric;
      if (this.curric_param !== undefined) {
        // set the curric name based on the curric param in the request
        this.curric_name = this.getCurricName(this.curric_param);
      } else {
        this.curric_name = undefined;
      }
    },
    methods: {
      getCurricName: function(curric) {
        return axios
          .get("/api/curric_typeahead/")
          .then(response => {
            var data = response.data;
            // find key by curric value
            const key = Object.keys(data).find(key => data[key] === curric);
            this.curric_name = key;
          })
          .catch(() => {
          });
      }
    }
  };
</script>

<style lang="scss">
</style>
