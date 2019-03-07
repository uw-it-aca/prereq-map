import Vue from 'vue/dist/vue.js';

import CourseInfoBox from "./components/course-infobox.vue";
import Typeahead from "./components/typeahead.vue";
import Boardal from "./components/boardal.vue";

console.log("I am Vue!")

new Vue({
  delimiters: ['[[', ']]'],
  el: '#vue_curriculum',
  components: {
    'course-infobox': CourseInfoBox,
    'typeahead': Typeahead,
    'blah': Boardal
  },
  data: {
    modal: {
      isOpen: false,
      hasMask: true,
      canClickMask: false,
      hasX: false
    },
    step: 1,
    max: 1,
    showDots: true,
    orientation: 'row',
    // xray: 'hidden'
  },
  computed: {
    isFirstStep: function() {
      return (this.step === 1)
    },
    isLastStep: function() {
      return (this.step === this.max)
    },
    hasDots: function() {
      return (this.max > 1 && this.showDots)
    },
    x_multiplier: function() {
      return (this.orientation === 'row' ? -1 : 0)
    },
    y_multiplier: function() {
      return (this.orientation === 'row' ? 0 : -1)
    },
    axis: function() {
      return (this.orientation === 'row' ? 'row' : 'column')
    },
    axisReverse: function() {
      return (this.orientation === 'row' ? 'row-reverse' : 'column-reverse')
    },
    cross: function() {
      return (this.orientation === 'row' ? 'column' : 'row')
    },
    crossReverse: function() {
      return (this.orientation === 'row' ? 'column-reverse' : 'row-reverse')
    },
    nextIcon: function() {
      return (this.orientation === 'row' ? 'fa-arrow-right' : 'fa-arrow-down')
    },
    backIcon: function() {
      return (this.orientation === 'row' ? 'fa-arrow-left' : 'fa-arrow-up')
    },

  },
  watch: {
    orientation: 'setCssVars',
    // xray: 'setCssVars'
  },
  methods: {
    toggleModal: function(step) {
      step = step || 1
      this.modal.isOpen = !this.modal.isOpen
      if (this.modal.isOpen) {
        let self = this
        setTimeout(function() {
          self.$sections = self.$el.querySelectorAll('section')
          self.max = self.$sections.length
          self.goToStep(step)
        }, 1)
      }
    },
    setCssVars: function() {
      this.$el.style.setProperty('--x', (((this.step * 100) - 100) * this.x_multiplier) + '%')
      this.$el.style.setProperty('--y', (((this.step * 100) - 100) * this.y_multiplier) + '%')
      this.$el.style.setProperty('--axis', this.axis)
      this.$el.style.setProperty('--axis-reverse', this.axisReverse)
      this.$el.style.setProperty('--cross', this.cross)
      this.$el.style.setProperty('--cross-reverse', this.crossReverse)
      // this.$el.style.setProperty('--vision', this.xray)
    },
    goToStep: function(step) {
      this.step = step > this.max ? this.max : step < 1 ? 1 : step
      this.currentSection = this.$sections[this.step - 1]
      this.$sections.forEach(function(section) {
        section.classList.remove('current')
      })
      this.currentSection.classList.add('current')
      this.currentSection.scrollTop = 0
      this.setCssVars()
    },
    skip: function(step) {
      this.step += step
      this.goToStep(this.step)
    },
    reset: function() {
      this.goToStep(1)
    },
    finish: function() {
      this.toggleModal()
    }
  }
})
