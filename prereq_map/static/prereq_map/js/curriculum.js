import Vue from 'vue/dist/vue.js';
import {_} from 'vue-underscore';
const axios = require('axios');

import ButtonCounter from "./components/button-counter.vue";
import CourseInfoBox from "./components/course-infobox.vue";
import VueBootstrapTypeahead from 'vue-bootstrap-typeahead';


console.log("I am Vue!")

new Vue({
  delimiters: ['[[', ']]'],
  el: '#vue_curriculum',
  components: {
    'button-counter' : ButtonCounter,
    'course-infobox' : CourseInfoBox,
    VueBootstrapTypeahead
  },
  data() {
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
})
