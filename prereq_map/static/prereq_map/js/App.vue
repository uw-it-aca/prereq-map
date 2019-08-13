<template>
  <div class="prereq">
    <header>
      <div class="line" />
      <!-- Separator on mobile nav -->

      <nav
        class="navbar navbar-expand-md navbar-dark"
        aria-label="Utility Menu"
      >
        <div class="d-flex flex-row order-2 order-md-3">
          <ul class="navbar-nav flex-row nav-feedback">
            <li class="nav-item">
              <a class="nav-link px-2" href="mailto:help@uw.edu?subject=PreReq%20Map%20&minus;%20Comment,%20Request,%20Suggestion&amp;body=Hello,%0A%0A%3CInclude%20your%20comment%20or%20question%20about%20the%20PreReq%20Map%20tool%20here%3e%0A%0A%0A"><i class="fa fa-envelope" /> Send Us Feedback</a>
            </li>
          </ul>
        </div>
        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <!-- <span class="close"><i class="material-icons">close</i></span>
          <button class="navbar-toggler collapsed" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"> -->
          <span class="navbar-toggler-icon" />
        </button>
        <div id="navbarSupportedContent" class="collapse navbar-collapse order-3 order-md-2">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <a class="nav-link" href="http://www.washington.edu/" target="_blank">UW.edu</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="https://my.uw.edu" target="_blank">MyUW</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="https://myplan.uw.edu/" target="_blank">MyPlan</a>
            </li>
          </ul>
        </div>
      </nav>
      <nav
        class="navbar navbar-expand navbar-dark banner-row flex-nowrap justify-content-center"
        aria-label="Main Menu"
      >
        <div class="logo-position">
          <img alt="PreReq Map" src="/static/prereq_map/img/gr-PreReqMap-logo.png">
        </div>
        <div class="nav nav-pills nav-justified tabs-med">
          <router-link to="/curriculum/" class="nav-link">
            Curriculum
          </router-link>
          <router-link to="/course/" class="nav-link">
            Course
          </router-link>
        </div>
      </nav>
    </header>

    <main class="prereq-content">
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
  // vue router-links styling overrides
  .router-link-active {
    background-color: #fff !important;
    color: #000 !important;
  }
</style>
