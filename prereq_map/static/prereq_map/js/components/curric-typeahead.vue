<template>
  <div>
    <div class="row curric-search">
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
    <div class="row">
      <div class="col-md-12">
        <h2>{{ curric_name }}</h2>
      </div>
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
        curric_name: undefined,
        course_param: undefined,
      };
    },
    watch: {
      // watch changes in curric param route changes
      "$route.query.curric": function() {
        this.curric_param = this.$route.query.curric;
        if (this.curric_param !== undefined) {
          // set the curric name based on the curric code
          this.curric_name = this.getCurricName(this.curric_param);
        }
      }
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

        // if the param was included in the request... convert it
        this.curric_param = this.$route.query.curric;
        if (this.curric_param !== undefined) {
          // set the curric name based on the curric param in the request
          this.curric_name = this.getCurricName(this.curric_param);
        }

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

        // set the curric name based on the curric code
        this.curric_name = this.getCurricName(curric_code);

      },
      getCurricName: function(curric) {
        var data = this.curric_objs;
        // find key by curric value
        const key = Object.keys(data).find(key => data[key] === curric);
        return key;
      }
    }
  };
</script>

<style lang="scss">
</style>
