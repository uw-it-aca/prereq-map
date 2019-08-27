<template>
  <div class="row curric-search mt-5 mb-5">
    <div class="col-md-9 offset-md-1">
      <b-form @submit.prevent="processForm">
        <b-input-group>
          <b-form-input
            v-model="query"
            type="text"
            aria-label="Enter a curric code... (e.g MATH)"
            placeholder="Enter a curric code... (e.g MATH)"
            size="lg"
            list="my-list-id"
            autocomplete="off"
          />
          <b-form-datalist id="my-list-id" :options="curric_list" />
          <b-input-group-append>
            <b-button variant="primary" type="submit">
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
        curric_list: [],
        curric_objs: {},
        course_param: undefined,
      };
    },
    mounted() {

      // get the list of currics and store in an array
      axios.get("/api/curric_typeahead").then(res => {
        
        // first, store the response data into an object
        this.curric_objs = res.data;

        // next, take the response data and create an array of currics
        let data = [];
        $(res.data).each(function(idx, value) {
          data.push(...Object.keys(value));
        });
        // save those in the curric list
        this.curric_list = data;

      });
    },

    methods: {
      processForm: function(e) {
        e.preventDefault();

        // get the code (param) of the curric being queried
        let curric_code = this.curric_objs[this.query];

        // use the curric code and update the query param in the url
        if (curric_code !== undefined){
          // eslint-disable-next-line no-unused-vars
          this.$router.push("/curriculum/?curric=" + curric_code).catch(err => {});
        } else {
          // eslint-disable-next-line no-unused-vars
          this.$router.push("/curriculum/").catch(err => {});
        }

      }
    }
  };
</script>

<style lang="scss">
</style>
