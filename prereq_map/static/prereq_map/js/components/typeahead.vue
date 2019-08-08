<template>
  <div class="row curric-search">
    <div class="col-md-9 offset-md-1">
      <vue-bootstrap-typeahead
        v-model="query"
        class="mb-3"
        :data="curric_list"
        placeholder="E.G. MATH"
        @hit="selected_curric = $event"
      />
    </div>
  </div>
</template>

<script>
  const axios = require("axios");
  import VueBootstrapTypeahead from "vue-bootstrap-typeahead";

  export default {
    components: {
      VueBootstrapTypeahead
    },
    filters: {},
    data() {
      return {
        query: "",
        query2: "",
        selected_curric: null,
        curric_list: [],
        curric_objs: null
      };
    },

    watch: {
      selected_curric(curric_query) {
        var curric_code = this.curric_objs[curric_query];
        //location.href = "?curric=" + curric_code;
        this.$router.push("/curriculum/?curric=" + curric_code);
      }
    },
    mounted() {
      axios.get("/api/curric_typeahead").then(res => {
        this.curric_objs = res.data;
        var curric_list = [];

        $(res.data).each(function(idx, value) {
          curric_list.push(...Object.keys(value));
        });
        this.curric_list = curric_list;
      });

      this.scrollList();
    },

    methods: {

      // handle up/down arrow events for keyboard navigating typeahead list
      // allows user to use tab and arrow buttons to move up and down to change focus selection
      scrollList: function() {
        $(".vbt-autcomplete-list").keydown(function(e) {
          if (e.keyCode == 38) {
            // up
            $(".vbst-item:focus").prev().focus();
          }
          if (e.keyCode == 40) {
            // down
            $(".vbst-item:focus").next().focus();
          }
        });

      }
    }
  };
</script>

<style lang="scss">
  // char's note: scoped css is "broken" for this component because
  //  vue-bootstrap-typeahead is already a scoped component by default... so it
  // cannot be scoped again. just be aware of this in the future!

  .curric-search {
    input {
      color: #000;
      font-size: 1.25rem;
      height: 3rem;
    }

    .vbt-autcomplete-list {
      box-shadow: none !important;
    }
  }
</style>
