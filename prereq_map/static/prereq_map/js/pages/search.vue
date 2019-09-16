// search.vue

<template>
  <div id="course" class="container">
    <user-accept />

    <h1>Search</h1>

    <div class="row course-search mt-5 mb-5">
      <div class="col-md-9 offset-md-1">
        <b-form-group label="Find prerequisite information by:">
          <b-form-radio-group
            v-model="selected"
            :options="options"
            name="radio-inline"
          />
        </b-form-group>
        <curric-typeahead v-if="dataReady && selected === 'curric'" :curricObj="curric_objs" />
        <course-search v-if="selected === 'course'" />
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
  import CourseSearch from "../components/course-search.vue";
  import UserAccept from "../components/user-accept.vue";
  import Typeahead from "../components/curric-typeahead.vue";

  export default {
    name: "Search",
    components: {
      "user-accept": UserAccept,
      "curric-typeahead": Typeahead,
      "course-search": CourseSearch
    },
    data() {
      return {
        curric_name: undefined,
        curric_param: undefined,
        curric_objs: {},
        dataReady: false,
        selected: 'curric',
        options: [
          { text: 'Curriculum', value: 'curric' },
          { text: 'Course', value: 'course' },
        ]
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
          .catch(() => {});
      },
      getCurricName: function() {
        // get the curric param from the queary params
        this.curric_param = this.$route.query.curric;

        if (this.curric_param !== undefined) {
          // assign data from global curric_objs after it has been populated
          let data = this.curric_objs;
          // find key by curric value
          let key = Object.keys(data).find(
            key => data[key] === this.curric_param
          );
          this.curric_name = key;
          // clean up the display name by doing a quick regex string replace
          this.curric_name = this.curric_name.replace(/.*: /, "");
          return this.curric_name;
        } else {
          this.curric_name = undefined;
        }
      },
      getCourse: function() {
        return axios
          .get("/api/course/" + encodeURI(this.course_param))
          .then(response => {
            this.course_data = response.data;
            this.course_number = this.course_data.x.nodes.course_number;

            // check to see if course_list is empty
            if (Object.keys(this.course_number).length !== 0) {
              this.course_valid = true;
            } else {
              this.course_valid = false;
            }

            // hide the loading spinner to show responses
            this.loading = false;
          })
          .catch(() => {
            this.course_valid = false;
            // hide the loading spinner to show responses
            this.loading = undefined;
            //console.log("error " + error);
          });
      }
    }
  };
</script>

<style lang="scss">
</style>
