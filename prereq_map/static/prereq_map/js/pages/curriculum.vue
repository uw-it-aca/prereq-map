// curriculum.vue

<template>
  <div id="curriculum" class="container">
    <user-accept />
    <h1>Curriculum Search</h1>
    <p>View the prerequisite map of courses in a curriculum</p>

    <curric-typeahead v-if="dataReady" :curricObj="curric_objs" />

    <div v-if="curric_name" class="row mb-4">
      <div class="col-md-12">
        <h2>{{ curric_name }}</h2>
      </div>
    </div>

    <div v-if="$mq == 'desktopxxxx'" class="row sr-only">
      <div class="col-md-12">
        <curric-list />
      </div>
    </div>
    <div v-else class="row">
      <div class="col-md-12">
        <curric-list />
      </div>
    </div>

    <div v-if="$mq == 'desktop'" aria-hidden="true">
      <curric-graph />
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  import UserAccept from "../components/user-accept.vue";
  import Typeahead from "../components/curric-typeahead.vue";
  import CurricGraph from "../components/curric-graph.vue";
  import CurricList from "../components/curric-list.vue";

  export default {
    name: "Curriculum",
    components: {
      "user-accept": UserAccept,
      "curric-typeahead": Typeahead,
      "curric-graph": CurricGraph,
      "curric-list": CurricList
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
      // watch changes in curric param route changes and get the curric name
      "$route.query.curric": function() {
        this.getCurricName();
      }
    },
    mounted() {
      document.title = "Curriculum Search - Prereq Map";
      // get curric data from api
      this.getCurricData();
    },
    methods: {
      getCurricData: function() {
        // get the list of currics and store in an array
        return axios
          .get("/api/curric_typeahead")
          .then(response => {
            // store the response data into an object
            this.curric_objs = response.data;
          })
          .then(() => {
            this.dataReady = true;
            // once the data is ready... get the curric name if one is passed in the params
            // on first load
            this.getCurricName();
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
