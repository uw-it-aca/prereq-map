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
      },

      // watch the curric_obj for when it gets populated with data
      curric_objs: function() {

        // handle manual url changes and page loads
        // ensure that curric_objs is not empty so that it can get processed
        this.curric_param = this.$route.query.curric;

        if (this.curric_param !== undefined) {
          // set the curric name based on the curric code
          this.getCurricName(this.curric_param);
        } else {
          this.curric_name = undefined;
        }

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
          .then(res => {
            // first, store the response data into an object
            this.curric_objs = res.data;

            // next, take the response data and create an array of currics
            let data = [];
            $(res.data).each(function(idx, value) {
              data.push(...Object.keys(value));
            });
            // save those in the curric list and set data ready flag true
            this.curric_list = data;
            this.dataReady = true;
            
          })
          .catch(() => {
          });

      },
      getCurricName: function(curric) {
        
        // assign data from global curric_objs after it has been populated
        let data = this.curric_objs;
  
        // find key by curric value
        let key = Object.keys(data).find(key => data[key] === curric);
        this.curric_name = key;
        // clean up the display name by doing a quick regex string replace
        this.curric_name = this.curric_name.replace(/.*: /, "");
        return this.curric_name;
      }

    }
  };
</script>

<style lang="scss">
</style>
