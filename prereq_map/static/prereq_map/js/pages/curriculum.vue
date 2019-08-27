// curriculum.vue

<template>
  <div id="curriculum" class="container">
    <user-accept />
    <h1>Curriculum Search</h1>
    <p>View the prerequisite map of courses in a curriculum</p>

    <curric-typeahead v-if="dataReady" :myList="curric_list" :myObj="curric_objs" />

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
        curric_list: [],
        curric_objs: {},
        name: "Bob",
        dataReady: false
      };
    },
    watch: {
      // watch changes in curric param route changes
      "$route.query.curric": function() {
        this.curric_param = this.$route.query.curric;
        if (this.curric_param !== undefined) {
          // set the curric name based on the curric code
          this.getCurricName(this.curric_param);
        } else {
          this.curric_name = undefined;
        }
      }
    },
    created() {
      document.title = "Curriculum Search - Prereq Map";
      console.log("parent created");

      // get curric data from api
      this.getCurricData();

      // if the param was included in the request... convert it
      this.curric_param = this.$route.query.curric;
      if (this.curric_param !== undefined) {
        // set the curric name based on the curric param in the request
        this.getCurricName(this.curric_param);
      } else {
        this.curric_name = undefined;
      }
    },
    mounted() {
      console.log('parent mounted');
    },
    methods: {
      getCurricData: function() {
        // get the list of currics and store in an array
        axios
          .get("/api/curric_typeahead")
          .then(res => {
            // first, store the response data into an object
            this.curric_objs = res.data;

            // next, take the response data and create an array of currics
            let data = [];
            $(res.data).each(function(idx, value) {
              data.push(...Object.keys(value));
            });
            // save those in the curric list
            this.curric_list = data;
            
            console.log("getting data");
            //console.log(this.curric_objs);
            //console.log(this.curric_list);

            // THIS IS CRUCIAL WHEN DEALING WITH ASYC DATA CALLS... GUARD AGAINST RACE CONDITIONS!!!
            this.dataReady = true;
          
          })
          .catch(() => {
          });

          
      },
      getCurricName: function(curric) {
        return axios
          .get("/api/curric_typeahead/")
          .then(response => {
            var data = response.data;
            // find key by curric value
            let key = Object.keys(data).find(key => data[key] === curric);
            this.curric_name = key;
            // clean up the display name by doing a quick regex string replace
            this.curric_name = this.curric_name.replace(/.*: /, "");
          })
          .catch(() => {
          });
      }
    }
  };
</script>

<style lang="scss">
</style>
