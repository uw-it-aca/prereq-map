<template>
  <div class="prereq">
    <header>
      <nav class="navbar navbar-expand-md navbar-dark prereq-bar" aria-label="Utility Menu">
        <div class="d-flex flex-row order-2 order-md-3">
          <ul class="navbar-nav flex-row nav-feedback">
            <li class="nav-item">
              <router-link to="/about/" class="nav-link px-2">
                About Prereq Map
              </router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link px-2" href="mailto:help@uw.edu?subject=PreReq%20Map%20&minus;%20Comment,%20Request,%20Suggestion&amp;body=Hello,%0A%0A%3CInclude%20your%20comment%20or%20question%20about%20the%20PreReq%20Map%20tool%20here%3e%0A%0A%0A"><i class="fa fa-envelope" /> Send Us Feedback</a>
            </li>
          </ul>
        </div>

        <b-navbar-toggle class="border-0" target="navbarSupportedContent" />
        <b-collapse id="navbarSupportedContent" is-nav class="order-3 order-md-2">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item border-0">
              <a class="nav-link" href="http://www.washington.edu/" target="_blank">UW.edu</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="https://my.uw.edu" target="_blank">MyUW</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="https://myplan.uw.edu/" target="_blank">MyPlan</a>
            </li>
          </ul>
        </b-collapse>
      </nav>

      <div class="prereq-banner">
        <b-container aria-label="Banner">
          <b-row>
            <b-col sm="5">
              <router-link to="/" class="nav-link pl-0">
                <img class="d-inline-block" alt="PreReq Map" src="/static/prereq_map/img/gr-PreReqMap-logo.png">
              </router-link>
            </b-col>
            <b-col sm="7" class="prereq-banner-inputs ">
              <curric-typeahead v-if="$route.path == '/curriculum/'" />
              <course-search v-if="$route.path == '/course/'" />
            </b-col>
          </b-row>
        </b-container>
      </div>
    </header>

    <main class="prereq-content mt-5 mb-5">
      <router-view />
    </main>

    <footer class="prereq-footer">
      <div>
        <div class="footer-links">
          <ul>
            <li>
              <a href="https://itconnect.uw.edu/learn/tools/prereq-map/" target="_blank">Help</a>
            </li>
            <li>
              <a href="mailto:help@uw.edu?subject=Prereq%20Map%20&minus;%20Comment,%20Request,%20Suggestion&amp;body=Hello,%0A%0A%3CInclude%20your%20comment%20or%20question%20about%20the%20PreReq%20Map%20tool%20here%3e%0A%0A%0A">
                Send Us Feedback</a>
            </li>
          </ul>
        </div>
        <!-- end of footer links -->
        <p class="credit">
          &copy; {{ new Date().getFullYear() }} University of Washington
        </p>
      </div>
      <!-- end of footer content -->
    </footer>
  </div>
</template>

<script>
  import CourseSearch from "./components/course-search.vue";
  import Typeahead from "./components/curric-typeahead.vue";

  export default {
    components: {
      "course-search": CourseSearch,
      "curric-typeahead": Typeahead,
    }
  };
</script>

<style lang="scss">

  // import custom bootstrap theme and base styling for app
  @import '../css/_variables.scss';
  @import '../css/custom.scss';
  @import '../css/base.scss';

  /* branding */

  .prereq-banner {
    background-color: $uw-purple;
  }

  .prereq-banner img {
    height: auto;
    width: 13rem;
  }

  .prereq-banner .logo-position {
    left: 1.25rem;
    position: absolute;
    top: 25%;
    transform: translate(0, -25%);

    @include media-breakpoint-up(sm) {
      left: 1.25rem;
      position: absolute;
      top: 50%;
      transform: translate(0, -50%);
    }
  }

  .prereq-banner-inputs {
    @include media-breakpoint-up(sm) {
      padding-top: 1.75rem;
    }
  }

</style>
