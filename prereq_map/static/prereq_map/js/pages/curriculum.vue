// curriculum.vue

<template>
  <div id="curriculum" class="container">
    <user-accept />
    <h1>Curriculum Search</h1>
    <p>View the prerequisite map of courses in a curriculum</p>

    <curric-typeahead />

    <div class="row">
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
