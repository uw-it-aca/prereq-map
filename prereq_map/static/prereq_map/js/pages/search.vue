// search.vue

<template>
  <div id="course" class="container">
    <user-accept />

    <h1>Search</h1>

    <div class="row course-search mt-5 mb-5">
      <div class="col-md-9 offset-md-1">
        <curric-typeahead v-if="dataReady" :curricObj="curric_objs" />

        <div class="mt-1 text-muted">
          Find prerequisite information for Curriculum or Courses
        </div>
      </div>
    </div>

    <h2>Discover</h2>
    <b-container class="bv-example-row">
      <b-row>
        <b-col sm="6">
          <h5>Curriculum</h5>
          <ul>
            <li><a href="/curriculum/?curric=MATH">Mathematics (MATH)</a></li>
            <li>Computer Science &amp; Engineering (CSE)</li>
            <li>Anthropology (ANTH)</li>
          </ul>
        </b-col>
        <b-col sm="6">
          <h5>Courses</h5>
          <ul>
            <li><a href="/course/?course=MATH 124">MATH 124</a></li>
            <li>CSE 142</li>
            <li>ANTH 200</li>
          </ul>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
  import axios from "axios";
  import UserAccept from "../components/user-accept.vue";
  import Typeahead from "../components/curric-typeahead.vue";

  export default {
    name: "Search",
    components: {
      "user-accept": UserAccept,
      "curric-typeahead": Typeahead,
    },
    data() {
      return {
        curric_name: undefined,
        curric_param: undefined,
        curric_objs: {},
        dataReady: false
      };
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
