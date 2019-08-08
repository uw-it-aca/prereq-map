<template>
  <div id="index" class="container py-1 mt-2" role="main">
    <nav>
      <router-link to="/">
        Home
      </router-link>
      <router-link to="/curriculum/">
        Curriculum
      </router-link>
      <router-link to="/course/">
        Course
      </router-link>
    </nav>
    <router-view />
  </div>
</template>

<script>
  export default {
    watch: {
      $route(to) {
        if (to.path == "/curriculum/") {
          $(".nav-curric").addClass("active");
          $(".nav-course").removeClass("active");
        } else if (to.path == "/course/") {
          $(".nav-curric").removeClass("active");
          $(".nav-course").addClass("active");
        }
      }
    },
    mounted() {
      if (this.$route.path == "/curriculum/") {
        $(".nav-curric").addClass("active");
        $(".nav-course").removeClass("active");
      } else if (this.$route.path == "/course/") {
        $(".nav-curric").removeClass("active");
        $(".nav-course").addClass("active");
      }
    }
  };
</script>

<style lang="scss">
</style>
