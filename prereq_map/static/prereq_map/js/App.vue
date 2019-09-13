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
        <b-container aria-label="Main Menu">
          <b-row>
            <b-col sm="4">
              <router-link to="/" class="nav-link px-2">
                <img class="d-block mx-auto" alt="PreReq Map" src="/static/prereq_map/img/gr-PreReqMap-logo.png">
              </router-link>
            </b-col>
            <b-col sm="8">
              <div v-if="['curriculum', 'course'].indexOf($route.name) > -1" class="mt-2 mb-3">
                <b-input-group>
                  <b-form-input
                    type="text"
                    aria-label="Enter a curric code... (e.g MATH)"
                    placeholder="Enter a curric search term... (e.g MATH, MATH 120)"
                    size="md"
                    autocomplete="off"
                  />

                  <b-input-group-append>
                    <b-button variant="primary" type="submit">
                      Search
                    </b-button>
                  </b-input-group-append>
                </b-input-group>
              </div>
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
  export default {};
</script>

<style lang="scss">

  // import custom bootstrap theme and base styling for app
  @import '../css/custom.scss';
  @import '../css/base.scss';

  // vue router-links styling overrides
  .prereq-banner {
    .router-link-active {
      color: #000 !important;
    }
  }

</style>
