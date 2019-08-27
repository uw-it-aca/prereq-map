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
          <b-form-datalist id="my-list-id" :options="myList" />
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
  export default {
    filters: {},
    props: {
      myObj: {
        type: Object,
        required: true
      },
      myList: {
        type: Array,
        required: true
      }
    },
    data() {
      return {
        query: "",
      };
    },
    methods: {
      processForm: function(e) {
        e.preventDefault();

        // get the code (param) of the curric being queried
        let curric_code = this.myObj[this.query];

        //console.log("call curric code");
        //console.log(curric_code);

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
