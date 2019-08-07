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
  export default {};
</script>

<style lang="scss">
</style>
