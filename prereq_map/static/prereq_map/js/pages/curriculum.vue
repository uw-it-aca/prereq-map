// curriculum.vue

<template>
  <div id="curriculum" class="container">
    <user-accept />
    <h1>Curriculum Search</h1>
    <p>View the prerequisite map of courses in a curriculum</p>

    <curric-typeahead v-if="dataReady" :curricObj="curric_objs" />

    <div v-if="curric_name" class="row">
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
        curric_objs: {},
        dataReady: false
      };
    },
    watch: {
      // watch changes in curric param route changes
      "$route.query.curric": function() {
        this.getCurricName();
      }
    },
    mounted() {
      document.title = "Curriculum Search - Prereq Map";
      // get curric data from api
      this.getCurricData();

      // wait 1 sec until data is loaded before trying to process a curric name
      setTimeout(() => {
        this.getCurricName();
      },1000);

    },
    methods: {
      getCurricData: function() {
        // get the list of currics and store in an array
        return axios
          .get("/api/curric_typeahead")
          .then(response => {
            // store the response data into an object
            this.curric_objs = response.data;
            this.dataReady = true;
          })
          .catch(() => {
          });
      },
      getCurricName: function() {

        // get the curric param from the queary params
        this.curric_param = this.$route.query.curric;

        if (this.curric_param !== undefined) {
          // assign data from global curric_objs after it has been populated
          let data = this.curric_objs;
          // find key by curric value
          let key = Object.keys(data).find(key => data[key] === this.curric_param);
          this.curric_name = key;
          // clean up the display name by doing a quick regex string replace
          this.curric_name = this.curric_name.replace(/.*: /, "");
          return this.curric_name;
        } else {
          this.curric_name = undefined;
        }

      }
    }
  };
</script>

<style lang="scss">
</style>
