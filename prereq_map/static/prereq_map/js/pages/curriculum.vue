// curriculum.vue

<template>
  <div id="curriculum" class="container">
    <div v-if="curric_param === undefined">
      <h1 class="h3 mb-3">
        Curriculum
      </h1>
      <p class="font-weight-lighter">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus
        elementum dignissim imperdiet. Vivamus maximus felis sed risus eleifend
        condimentum. Aliquam id lacus condimentum, tempus justo quis, mollis
        odio. Etiam feugiat efficitur maximus. Etiam dignissim pharetra congue.
        Donec laoreet condimentum orci, eu condimentum nulla condimentum
        consectetur. Etiam et urna aliquam, suscipit ante in, pharetra turpis.
        Phasellus ut finibus dolor. Quisque gravida nisi mi, ac gravida felis
        dapibus eget. Sed at lectus venenatis, convallis dui eu, venenatis
        dolor. Nunc sed leo sagittis, ornare tortor a, pretium leo. Quisque enim
        nunc, fringilla at sapien sodales, tincidunt ultrices eros.
      </p>
    </div>
    <div v-else>
      <div class="row mb-4">
        <div class="col-md-12">
          <h1 v-if="curric_param" class="h3">
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
      };
    },
    watch: {
      // watch changes in curric param route changes and get the curric name
      "$route.query.curric": function() {
        this.curric_param = this.$route.query.curric;

        this.getCurricName();
      }
    },
    mounted() {
      this.curric_param = this.$route.query.curric;
      document.title = this.curric_param + " - Curriculum - Prereq Map";

      this.getCurricName();

    },
    methods: {

      getCurricName: function() {

        // get the curric param from the queary params
        this.curric_param = this.$route.query.curric;

        if (this.curric_param !== undefined) {

          // get the list of currics and store in an array
          return axios
            .get("/api/curric_typeahead")
            .then(response => {
              // store the response data into an object
              this.curric_objs = response.data;
            })
            .then(() => {
              let data = this.curric_objs;
              // find key by curric value
              let key = Object.keys(data).find(key => data[key] === this.curric_param);
              this.curric_name = key;
              // clean up the display name by doing a quick regex string replace
              this.curric_name = this.curric_name.replace(/.*: /, "");
              return this.curric_name;

            })
            .catch(() => {});

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
