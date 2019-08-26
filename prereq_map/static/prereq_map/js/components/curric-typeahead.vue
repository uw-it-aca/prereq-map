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
        curric_objs: null,
        course_param: undefined,
      };
    },
    mounted() {

      // get the list of currics and store in an object
      axios.get("/api/curric_typeahead").then(res => {
        this.curric_objs = res.data;
        var curric_list = [];

        $(res.data).each(function(idx, value) {
          curric_list.push(...Object.keys(value));
        });
        this.curric_list = curric_list;

      });
    },

    methods: {
      processForm: function(e) {
        e.preventDefault();

        var curric_code = this.curric_objs[this.query];

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
