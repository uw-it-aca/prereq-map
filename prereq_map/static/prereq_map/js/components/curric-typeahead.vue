<template>
  <div>
    <div class="row curric-search">
      <div class="col-md-9 offset-md-1">
        <b-form @submit.prevent="processForm">
          <b-input-group class="mt-3">
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
    <h2 class="mt-4">
      {{ curric_name }}
    </h2>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    filters: {},
    data() {
      return {
        query: "",
        selected_curric: null,
        curric_list: [],
        curric_objs: null,
        curric_name: undefined,
      };
    },

    mounted() {
      axios.get("/api/curric_typeahead").then(res => {
        this.curric_objs = res.data;
        var curric_list = [];

        $(res.data).each(function(idx, value) {
          curric_list.push(...Object.keys(value));
        });
        this.curric_list = curric_list;

        // eslint-disable-next-line no-console
        console.log(this.curric_objs);

      });
    },

    methods: {
      processForm: function(e) {
        e.preventDefault();

        var curric_code = this.curric_objs[this.query];
        this.curric_name = this.query;

        if (curric_code !== undefined){
          // eslint-disable-next-line no-unused-vars
          this.$router.push("/curriculum/?curric=" + curric_code).catch(err => {});
        } else {
          // eslint-disable-next-line no-unused-vars
          this.$router.push("/curriculum/").catch(err => {});
        }
      },
    }
  };
</script>

<style lang="scss">
</style>
