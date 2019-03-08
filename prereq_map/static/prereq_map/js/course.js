import Vue from 'vue/dist/vue.js';

import ButtonCounter from "./components/button-counter.vue";
import CourseSearch from "./components/course-search.vue";
import CourseDetail from "./components/course-detail.vue";

console.log("I am Vue!")

new Vue({
  delimiters: ['[[', ']]'],
  el: '#vue_course',
  components: {
    'button-counter' : ButtonCounter,
    'course-search' : CourseSearch,
    'course-detail' : CourseDetail
  }
})
