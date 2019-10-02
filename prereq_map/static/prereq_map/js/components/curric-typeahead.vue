<template>
  <div class="row curric-search mb-3">
    <div class="col">
      <b-form @submit.prevent="processForm">
        <b-input-group>
          <b-form-input
            v-bind:size="$route.path == '/curriculum/' ? 'md': 'lg'"
            v-model="query"
            type="text"
            aria-label="Enter a curric code... (e.g MATH)"
            placeholder="Enter a curric code... (e.g MATH)"
            list="my-list-id"
            autocomplete="off"
          />
          <b-form-datalist id="my-list-id" :options="curric_list" />
          <b-input-group-append>
            <b-button v-bind:variant="$route.path == '/curriculum/' ? 'light': 'primary'" class="border-left" type="submit">
              Search
            </b-button>
          </b-input-group-append>
        </b-input-group>
      </b-form>
    </div>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    filters: {},
    data() {
      return {
        query: "",
        curric_list: undefined,
        curric_objs: {},
      };
    },
    mounted() {
      // get curric data from api
      this.getCurricData();
    },
    methods: {
      processForm: function(e) {
        e.preventDefault();

        // get the code (param) of the curric being queried
        // make sure it is encoded to handle & (e.g. EDC&I)
        let curric_code = this.curric_objs[this.query];

        // use the curric code and update the query param in the url
        if (curric_code !== undefined){
          // eslint-disable-next-line no-unused-vars
          this.$router.push("/curriculum/?curric=" + encodeURIComponent(curric_code)).catch(err => {});
        } else {
          // eslint-disable-next-line no-unused-vars
          this.$router.push("/curriculum/").catch(err => {});
        }

      },
      getCurricData: function() {

        // get the list of currics and store in an array
        return axios
          .get("/api/curric_typeahead")
          .then(response => {
            // store the response data into an object
            this.curric_objs = response.data;
          })
          .then(() => {
            //this.dataReady = true;
            // once the data is ready... get the curric name if one is passed in the params
            // on first load
            //this.getCurricName();

            // take the obj prop and create an array of currics to populate the datalist
            let data = [];
            $(this.curric_objs).each(function(idx, value) {
              data.push(...Object.keys(value));
            });
            this.curric_list = data;

          })
          .catch(() => {});
      }
    },
  };
</script>

<style lang="scss">
</style>
