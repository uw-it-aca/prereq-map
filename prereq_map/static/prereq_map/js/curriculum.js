import Vue from 'vue/dist/vue.js';
import CourseInfoBox from "./components/course-infobox.vue";
import Typeahead from "./components/typeahead.vue";
import Onboarding from "./components/onboarding.vue";
import Graph from "./components/curric-graph.vue";

console.log("I am Vue!")

new Vue({
  delimiters: ['[[', ']]'],
  el: '#vue_curriculum',
  components: {
    'course-infobox': CourseInfoBox,
    'typeahead': Typeahead,
    'onboarding' : Onboarding,
    'typeahead' : Typeahead,
    'curric-graph': Graph
  }
})
