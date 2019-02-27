import Vue from 'vue/dist/vue.js';

import ButtonCounter from "./components/button-counter.vue";
import CourseInfoBox from "./components/course-infobox.vue";

console.log("I am Vue!")

new Vue({
  delimiters: ['[[', ']]'],
  el: '#vue_curriculum',
  components: {
    'button-counter' : ButtonCounter,
    'course-infobox' : CourseInfoBox
  }
})
