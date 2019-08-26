// curriculum.vue

<template>
  <div id="curriculum" class="container py-1 mt-2">
    <user-accept />

    <h1 class="pt-4 pb-2">
      Curriculum Search
    </h1>
    <p class="instruction-text pb-4">
      View the prerequisite map of courses in a curriculum
    </p>

    <curric-typeahead />

    <div class="row mt-2 mb-5">
      <div class="col-md-9">
        <curric-graph />
      </div>
      <div class="col-sm-12 col-md-3">
        <course-infobox />
      </div>
    </div>
  </div>
</template>

<script>
  import UserAccept from "../components/user-accept.vue";
  import CourseInfoBox from "../components/course-infobox.vue";
  import Typeahead from "../components/curric-typeahead.vue";
  import Graph from "../components/curric-graph.vue";

  export default {
    name: "Curriculum",
    components: {
      "user-accept": UserAccept,
      "curric-typeahead": Typeahead,
      "curric-graph": Graph,
      "course-infobox": CourseInfoBox
    },
    mounted() {
      document.title = "Curriculum Search - Prereq Map";
    }
  };
</script>

<style lang="scss">
</style>
