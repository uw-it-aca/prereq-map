<template>
  <div class="row curric-search">
    <div class="col">
      <b-form @submit.prevent="processForm">
        <b-input-group>
          <b-form-input
            v-bind:size="$route.path == '/curriculum/' ? 'md': 'lg'"
            v-model="query"
            :state="isValid"
            type="text"
            aria-label="Enter curriculum code... (e.g MATH, BIOL)"
            placeholder="Enter curriculum code... (e.g MATH. BIOL)"
            list="my-list-id"
            autocomplete="off"
          />
          <b-input-group-append>
            <b-button v-if="$route.path == '/curriculum/'" :variant="isValid == false ? 'danger' : 'light'" class="border-left-0 rounded-right" type="submit">
              Search
            </b-button>
            <b-button v-else :variant="isValid == false ? 'danger' : 'primary'" class="border-left-0 rounded-right" type="submit">
              Search
            </b-button>
          </b-input-group-append>
          <b-form-invalid-feedback id="input-curric-feedback" role="alert">
            You must select a curriculum from the list provided.
          </b-form-invalid-feedback>
          <b-form-datalist id="my-list-id" :options="curric_list" />
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
        isValid: null,
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

        // don't allow empty searches
        if (curric_code !== undefined) {
          this.isValid = null;
          // eslint-disable-next-line no-unused-vars
          this.$router.push("/curriculum/?curric=" + encodeURIComponent(curric_code)).catch(err => {});
        } else {
          this.isValid = false;
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
