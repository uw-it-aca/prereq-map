// search.vue

<template>
  <div id="course" class="container">
    <h1>Search</h1>

    <div class="row course-search mt-5 mb-5">
      <div class="col-md-9 offset-md-1">
        <b-form @submit.prevent="processForm">
          <b-input-group>
            <b-form-input
              v-model="course_code"
              :formatter="uppercase"
              type="text"
              aria-label="Enter a search term... (e.g MATH 124)"
              placeholder="Enter a search term... (e.g MATH or MATH 124)"
              size="lg"
              autocomplete="off"
            />
            <b-input-group-append>
              <b-button variant="primary" type="submit">
                Search
              </b-button>
            </b-input-group-append>
          </b-input-group>
          <div class="mt-1 text-muted">
            Find prerequisite information for Curriculum or Courses
          </div>
        </b-form>
      </div>
    </div>

    <h2>Discover</h2>
    <b-container class="bv-example-row">
      <b-row>
        <b-col sm="6">
          <h5>Curriculum</h5>
          <ul>
            <li><a href="/curriculum/?curric=MATH">Mathematics (MATH)</a></li>
            <li>Computer Science &amp; Engineering (CSE)</li>
            <li>Anthropology (ANTH)</li>
          </ul>
        </b-col>
        <b-col sm="6">
          <h5>Courses</h5>
          <ul>
            <li><a href="/course/?course=MATH 124">MATH 124</a></li>
            <li>CSE 142</li>
            <li>ANTH 200</li>
          </ul>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
  export default {
    name: "Search"
  };
</script>

<style lang="scss">
</style>
