<template>
  <div class="prereq" :aria-hidden="[!userAccepted]">
    <header>
      <nav class="navbar navbar-expand-md navbar-dark prereq-bar" aria-label="Utility Menu">
        <div class="d-flex flex-row order-2 order-md-3">
          <ul class="navbar-nav flex-row nav-feedback">
            <li class="nav-item">
              <a href="/about/" class="nav-link px-2">
                About Prereq Map
              </a>
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
        <b-container aria-label="Banner" class="p-3">
          <b-row>
            <b-col sm="5">
              <router-link to="/" class="nav-link p-0">
                <b-img src="/static/prereq_map/img/gr-PreReqMap-logo.png" fluid alt="PreReq Map" />
              </router-link>
            </b-col>
            <b-col sm="7" class="prereq-banner-inputs mt-auto mb-auto">
              <curric-typeahead v-if="$route.path == '/curriculum/'" />
              <course-typeahead v-if="$route.path == '/course/'" />
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

    <user-accept />

  </div>
</template>

<script>
  import Vue from "vue";
  import VueCookies from "vue-cookies";
  Vue.use(VueCookies);

  import CourseTypeahead from "./components/course-typeahead.vue";
  import CurricTypeahead from "./components/curric-typeahead.vue";
  import UserAccept from "./components/user-accept.vue";

  export default {
    components: {
      "user-accept": UserAccept,
      "course-typeahead": CourseTypeahead,
      "curric-typeahead": CurricTypeahead,
    },
    data() {
      return {
        // set initial value to false
        userAccepted: false
      }
    },
    mounted() {
      // check if valid cookie exists and user has accepted terms
      if (this.$cookies.get("prereq-accepted") == "false") {
        //console.log("user accepted false");
        this.userAccepted = false
      } else {
        //console.log("user accepted true");
        this.userAccepted = true
      }

    },
  };
</script>

<style lang="scss">

  // import custom bootstrap theme and base styling for app
  @import '../css/_variables.scss';
  @import '../css/custom.scss';
  @import '../css/base.scss';

  body { background: #444; }

  .prereq { background: #fff; }

  /* branding */

  .prereq-banner {
    background-color: $uw-purple;
  }
</style>
