import Vue from 'vue/dist/vue.js';

import ButtonCounter from "./components/button-counter.vue";
import CourseInfoBox from "./components/course-infobox.vue";
import Typeahead from "./components/Typeahead.vue"

console.log("I am Vue!")

new Vue({
  delimiters: ['[[', ']]'],
  el: '#vue_curriculum',
  components: {
    'button-counter' : ButtonCounter,
    'course-infobox' : CourseInfoBox,
    'typeahead' : Typeahead
  },

  data() {
    return {
      series: [{
          id: 1,
          title: 'Game of Thrones',
          body: 'You know nothing, Jon Snow'
        },
        {
          id: 2,
          title: 'Suits',
          body: 'You always have a choice'
        },
        {
          id: 3,
          title: 'Dr House',
          body: 'If nobody hates you, you are doing something wrong'
        },
        {
          id: 4,
          title: 'Breaking Bad',
          body: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
        },
        {
          id: 5,
          title: 'Arrow',
          body: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
        },
        {
          id: 6,
          title: 'Silicon Valley',
          body: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
        }
      ]
    }
  }

})
