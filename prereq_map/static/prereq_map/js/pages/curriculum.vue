// curriculum.vue

<template>
  <div id="curriculum" class="container">
    <div v-if="curric_name === undefined">
      <b-container class="bv-example-row">
        <b-row>
          <b-col sm>
            <h3>Seattle</h3>
            <ul>
              <li><a href="/curriculum/?curric=MATH">Mathematics (MATH)</a></li>
              <li>aslkjfd</li>
              <li>aslkjfd</li>
              <li>aslkjfd</li>
              <li>aslkjfd</li>
            </ul>
          </b-col>
          <b-col sm>
            <h3>Bothell</h3>
            <ul>
              <li>aslkjfd</li>
              <li>aslkjfd</li>
              <li>aslkjfd</li>
              <li>aslkjfd</li>
              <li>aslkjfd</li>
            </ul>
          </b-col>
          <b-col sm>
            <h3>Tacoma</h3>
            <ul>
              <li>aslkjfd</li>
              <li>aslkjfd</li>
              <li>aslkjfd</li>
              <li>aslkjfd</li>
              <li>aslkjfd</li>
            </ul>
          </b-col>
        </b-row>
      </b-container>
    </div>
    <div v-else>
      <div class="row mb-4">
        <div class="col-md-12">
          <h1 v-if="curric_name" class="h3">
            {{ curric_name }}
          </h1>
          <h1 v-else class="h3">
            Curriculum
          </h1>
        </div>
      </div>

      <div v-if="$mq == 'desktop'" class="row sr-only">
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
  </div>
</template>

<script>
  import axios from "axios";
  import CurricGraph from "../components/curric-graph.vue";
  import CurricList from "../components/curric-list.vue";

  export default {
    name: "Curriculum",
    components: {
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
      document.title = this.curric_name + " - Curriculum - Prereq Map";
      // get curric data from api
      this.getCurricData();
      document.title = this.curric_name + " - Curriculum - Prereq Map";
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

          document.title = this.curric_name + " - Curriculum - Prereq Map - University of Washington";

          return this.curric_name;
        } else {
          this.curric_name = undefined;

          document.title = "Curriculum - Prereq Map - University of Washington";

        }

      }
    }
  };
</script>

<style lang="scss">
</style>
