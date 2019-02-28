<template>

  <div id="main-search" class="search-width">

    <vue-bootstrap-typeahead
      class="woot"
      v-model="query"
      :data="users"
      :serializer="item => item.login"
      @hit="selectedUser = $event"
      placeholder="Search GitHub Users.."
    />

    <h3>Selected User JSON</h3>
    <pre>{{ selectedUser | stringify }}</pre>

  </div>

</template>

<script>
import {_} from 'vue-underscore';
const axios = require('axios');
import VueBootstrapTypeahead from 'vue-bootstrap-typeahead';

export default {

  components: {
    VueBootstrapTypeahead
  },
  data: function () {
    return {
      query: '',
      selectedUser: null,
      users: []
    }
  },
  methods: {

    searchUsers(newQuery) {
      axios.get(`https://api.github.com/search/users?q=${newQuery}`)
        .then((res) => {
          console.log(res.data)
          this.users = res.data.items
        })
    }

  },

  watch: {
    query: _.debounce(function(newQuery) { this.searchUsers(newQuery) }, 250)
  },

  filters: {
    stringify(value) {
      return JSON.stringify(value, null, 2)
    }
  },

}
</script>

<style>

  .search-width {
    input {
      height: 3rem;
      border-radius: 0;
      border: 0.04688rem solid #333;
    }
  }

  .vbt-autcomplete-list { box-shadow: none !important; }

</style>
