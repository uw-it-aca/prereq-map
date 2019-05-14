<template>
<div id="curriculum" class="container py-1 mt-2" role="main">

    <onboarding></onboarding>

    <h1 class="pt-4 pb-2">Curriculum Search</h1>
    <p class="instruction-text pb-4">View the prerequisite map of courses in a curriculum. </p>

    <typeahead></typeahead>

    <div class="row mt-5 mb-5">
        <div class="col-md-9 mb-3">
            <curric-graph></curric-graph>
        </div>
        <div class="col-sm-12 col-md-3">
            <course-infobox ref="infobox"></course-infobox>
        </div>
    </div>

</div>
</template>

<script>
import Onboarding from "../../components/onboarding.vue";
import CourseInfoBox from "../../components/course-infobox.vue";
import Typeahead from "../../components/typeahead.vue";
import Graph from "../../components/curric-graph.vue";

export default {
  name: 'Curriculum',
  components: {
      'onboarding' : Onboarding,
      'typeahead': Typeahead,
      'curric-graph': Graph,
      'course-infobox': CourseInfoBox
  },
}
</script>

<style lang="scss">

</style>
