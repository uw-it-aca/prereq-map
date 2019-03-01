import Vue from 'vue/dist/vue.js';

import ButtonCounter from "./components/button-counter.vue";

console.log("I am Vue!")

new Vue({
  delimiters: ['[[', ']]'],
  el: '#vue_course',
  components: {
    'button-counter' : ButtonCounter
  }
})
