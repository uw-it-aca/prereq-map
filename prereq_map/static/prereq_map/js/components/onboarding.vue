<template>
  <div>
    <b-modal id="bv-modal-example" size="lg" centered hide-header hide-footer>
      <div class="d-block">
        <b-carousel
          id="carousel-1"
          :interval="0"
          controls
          indicators
          img-width="1024"
          img-height="880"
        >
          <!-- Slides with custom text -->
          <b-carousel-slide img-src="/static/prereq_map/img/modal-bg.jpg" img-alt="fsdaasdf">
            <div class="text-left text-dark">
              <p class="mb-4 h2">
                Discover courses and plan your schedule more effectively
              </p>
              <p>
                It can be tough figuring out which courses to take. How do
                you find courses similar to ones you’ve really enjoyed? Of
                the courses you’ve already taken, which ones provide a
                foundation for more advanced coursework? What sequence of
                courses is best? The <strong>Prereq Map</strong> helps you
                discover interesting courses and enables you to be strategic
                about planning your course schedule. (What’s a prereq?
                Prereq is short for prerequisites: the courses that act as a
                foundation for other courses.)
              </p>
              <p>Remember to talk to your adviser when course planning.</p>
            </div>
          </b-carousel-slide>

          <!-- Slides with custom text -->
          <b-carousel-slide img-src="/static/prereq_map/img/modal-bg.jpg" img-alt="fsdaasdf">
            <div class="text-left text-dark">
              <p class="mt-4 mb-4 h3">
                See the prerequisite map for a curriculum
                <small>(e.g. Biology, BIOL)</small>
              </p>
              <p>
                Begin exploring the Prereq Map by choosing a curriculum
                (subjects comprising a discipline, e.g., Biology or BIOL)
                you’re interested in. Follow the lines to view prerequisites
                for courses. View courses that have prereqs and courses that
                are prereqs for other courses.
              </p>
            </div>
          </b-carousel-slide>

          <!-- Slides with custom text -->
          <b-carousel-slide img-src="/static/prereq_map/img/modal-bg.jpg" img-alt="fsdaasdf">
            <div class="text-left text-dark">
              <p class="mt-4 mb-4 h3">
                Get additional info about a course
              </p>
              <p>
                Each square on the map represents a specific course. Click
                the square to view prerequisite information for the course.
                Click the links in the sidebar to learn more.
              </p>
            </div>
          </b-carousel-slide>

          <!-- Slide with blank fluid image to maintain slide aspect ratio -->
          <b-carousel-slide img-src="/static/prereq_map/img/modal-bg.jpg" img-alt="asdfad">
            <div class="text-left text-dark">
              <p class="mt-4 mb-4 h3">
                Get more course detail and find related curricula
              </p>
              <p>
                On the Course Search page, click links to browse related
                course offerings. You can also explore related curricula and
                their prerequisite maps.
              </p>

              <p class="h6">
                <strong>Important notes:</strong>
              </p>

              <ul>
                <li>
                  Prereq Map shows current prerequisites. When planning
                  several quarters out, keep in mind that prerequisites may
                  change over time.
                </li>
                <li>
                  Prereq Map is based solely on course prerequisites and
                  does not take into account specific requirements for
                  graduation.
                </li>
                <li>
                  Not all equivalencies (e.g. placement tests) are
                  represented in the map – just courses. You can find some
                  equivalencies in the text description.
                </li>
                <li>
                  Remember to talk to your adviser when course planning.
                </li>
              </ul>
              <div class="text-center mt-3">
                <div>
                  <a
                    @click="
                      $ga.event(
                        'outbound',
                        'click',
                        'https://itconnect.uw.edu/learn/tools/prereq-map/'
                      )
                    "
                    @keydown="
                      $ga.event(
                        'outbound',
                        'click',
                        'https://itconnect.uw.edu/learn/tools/prereq-map/'
                      )
                    "
                    href="https://itconnect.uw.edu/learn/tools/prereq-map/"
                    target="_blank"
                  >
                    Additional details
                  </a>
                </div>
              </div>
              <div class="text-center mt-2">
                <button
                  @click="accept"
                  @keydown="accept"
                  class="btn btn-primary prereq-purple"
                >
                  Got it!
                </button>
              </div>
            </div>
          </b-carousel-slide>
        </b-carousel>
      </div>
    </b-modal>
  </div>

  <!-- Modal -->
  <!--
  <div
    id="onboardingModal"
    class="modal fade"
    tabindex="-1"
    role="dialog"
    aria-labelledby=""
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button
            @click="$ga.event('onboarding', 'click', 'close button')"
            @keydown="$ga.event('onboarding', 'click', 'close button')"
            type="button"
            class="close"
            data-dismiss="modal"
            aria-label="Close"
          >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div id="carouselExampleIndicators" class="carousel slide">
            <ol class="carousel-indicators">
              <li
                data-target="#carouselExampleIndicators"
                data-slide-to="0"
                class="active"
              />
              <li
                data-target="#carouselExampleIndicators"
                data-slide-to="1"
              />
              <li
                data-target="#carouselExampleIndicators"
                data-slide-to="2"
              />
              <li
                data-target="#carouselExampleIndicators"
                data-slide-to="3"
              />
            </ol>
            <div class="carousel-inner rounded-lg">
              <h1 class="sr-only">
                Welcome to Prereq Map!
              </h1>
              <div
                class="carousel-item active prereq-onboarding-main"
                style="background-image: url('/static/prereq_map/img/modal-bg.jpg');"
              >
                <h2 class="mb-4" style="margin-top: 200px;">
                  Discover courses and plan your schedule more effectively
                </h2>
                <p>
                  It can be tough figuring out which courses to take. How do
                  you find courses similar to ones you’ve really enjoyed? Of
                  the courses you’ve already taken, which ones provide a
                  foundation for more advanced coursework? What sequence of
                  courses is best? The <strong>Prereq Map</strong> helps you
                  discover interesting courses and enables you to be strategic
                  about planning your course schedule. (What’s a prereq?
                  Prereq is short for prerequisites: the courses that act as a
                  foundation for other courses.)
                </p>
                <p>Remember to talk to your adviser when course planning.</p>
              </div>

              <div class="carousel-item">
                <img
                  src="/static/prereq_map/img/onboarding-biol.png"
                  style="border: solid 2px #333;
                    width: 600px;"
                  alt="Onboarding curriculum example"
                >
                <h2 class="mt-4 mb-4 h3">
                  See the prerequisite map for a curriculum
                  <small>(e.g. Biology, BIOL)</small>
                </h2>
                <p>
                  Begin exploring the Prereq Map by choosing a curriculum
                  (subjects comprising a discipline, e.g., Biology or BIOL)
                  you’re interested in. Follow the lines to view prerequisites
                  for courses. View courses that have prereqs and courses that
                  are prereqs for other courses.
                </p>
              </div>
              <div class="carousel-item">
                <img
                  src="/static/prereq_map/img/onboarding-infobox.png"
                  style="border: solid 2px #333;
                    width: 600px;"
                  alt="Onboarding Infobox example"
                >
                <h2 class="mt-4 mb-4 h3">
                  Get additional info about a course
                </h2>
                <p>
                  Each square on the map represents a specific course. Click
                  the square to view prerequisite information for the course.
                  Click the links in the sidebar to learn more.
                </p>
              </div>
              <div class="carousel-item">
                <img
                  src="/static/prereq_map/img/onboarding-course-details.png"
                  style="border: solid 2px #333;
                    width: 600px;"
                  alt="Onboarding course details example"
                >
                <h2 class="mt-4 mb-4 h3">
                  Get more course detail and find related curricula
                </h2>
                <p>
                  On the Course Search page, click links to browse related
                  course offerings. You can also explore related curricula and
                  their prerequisite maps.
                </p>

                <p class="h6">
                  <strong>Important notes:</strong>
                </p>

                <ul>
                  <li>
                    Prereq Map shows current prerequisites. When planning
                    several quarters out, keep in mind that prerequisites may
                    change over time.
                  </li>
                  <li>
                    Prereq Map is based solely on course prerequisites and
                    does not take into account specific requirements for
                    graduation.
                  </li>
                  <li>
                    Not all equivalencies (e.g. placement tests) are
                    represented in the map – just courses. You can find some
                    equivalencies in the text description.
                  </li>
                  <li>
                    Remember to talk to your adviser when course planning.
                  </li>
                </ul>

                <div class="text-center mt-3">
                  <div>
                    <a
                      @click="
                        $ga.event(
                          'outbound',
                          'click',
                          'https://itconnect.uw.edu/learn/tools/prereq-map/'
                        )
                      "
                      @keydown="
                        $ga.event(
                          'outbound',
                          'click',
                          'https://itconnect.uw.edu/learn/tools/prereq-map/'
                        )
                      "
                      href="https://itconnect.uw.edu/learn/tools/prereq-map/"
                      target="_blank"
                    >
                      Additional details
                    </a>
                  </div>
                </div>
                <div class="text-center mt-2">
                  <button
                    @click="accept"
                    @keydown="accept"
                    class="btn btn-primary prereq-purple"
                  >
                    Got it!
                  </button>
                </div>
              </div>
            </div>
            <a
              class="carousel-control-prev d-none"
              href="#carouselExampleIndicators"
              role="button"
              data-slide="prev"
            >
              <span class="carousel-control-prev-icon" aria-hidden="true" />
              <span class="sr-only">Previous</span>
            </a>
            <a
              class="carousel-control-next d-none"
              href="#carouselExampleIndicators"
              role="button"
              data-slide="next"
            >
              <span class="carousel-control-next-icon" aria-hidden="true" />
              <span class="sr-only">Next</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
  -->
</template>

<script>
  import Vue from "vue";
  import VueCookies from "vue-cookies";
  Vue.use(VueCookies);

  export default {
    data() {
      return {};
    },
    mounted() {

      

      // check if valid cookie exists and user has not yet accepted terms
      if (this.$cookies.get("prereq-onboarding-accepted") == "false") {

        // show the onboarding modal
        
        /*
        $("#onboardingModal").modal({ backdrop: "static", keyboard: false });
        this.carouselConfig();
        */

        this.$bvModal.show('bv-modal-example');

        // google analytics (vue syntax)
        this.$ga.page({
          page: "/onboarding/page-1/",
          title: "Onboarding introduction"
        });
      }
    },

    methods: {
      // handle the 'get started' button click event
      accept: function() {
        // get the end of term date and set as the expiration value
        var expires = this.$cookies.get("prereq-onboarding-expires");
        // set the accept cookie value to true and set the expiration
        this.$cookies.set("prereq-onboarding-accepted", "true", expires);
        this.$cookies.remove("prereq-onboarding-expires");

        // hide the modal (until end of the current term)
        $("#onboardingModal").modal("hide");

        // google analytics pageview
        this.$ga.page({
          page: "/onboarding/accepted/",
          title: "Onboarding accepted"
        });
      },

      /*
      carouselConfig: function() {
        var carouselLength = $(".carousel-item").length - 1;
        // If there is more than one item

        if (carouselLength) {
          $(".carousel-control-next").removeClass("d-none");
        }

        $(".carousel")
          .carousel({
            interval: false,
            wrap: false
          })
          .on("slide.bs.carousel", function(e) {
            // First one
            if (e.to == 0) {
              $(".carousel-control-prev").addClass("d-none");
              $(".carousel-control-next").removeClass("d-none");

              // google anlytics (vanilla js syntax)
              window.ga("set", "page", "/onboarding/page-1/");
              window.ga("set", "title", "Onboarding introduction");
              window.ga("send", "pageview");
            } else if (e.to == 1) {
              $(".carousel-control-prev").removeClass("d-none");
              $(".carousel-control-next").removeClass("d-none");

              // google anlytics (vanilla js syntax)
              window.ga("set", "page", "/onboarding/page-2/");
              window.ga("set", "title", "Onboarding curriculum search");
              window.ga("send", "pageview");
            } else if (e.to == 2) {
              $(".carousel-control-prev").removeClass("d-none");
              $(".carousel-control-next").removeClass("d-none");

              // google anlytics (vanilla js syntax)
              window.ga("set", "page", "/onboarding/page-3/");
              window.ga("set", "title", "Onboarding course details");
              window.ga("send", "pageview");
            }
            // Last one
            else if (e.to == 3) {
              $(".carousel-control-prev").removeClass("d-none");
              $(".carousel-control-next").addClass("d-none");

              // google anlytics (vanilla js syntax)
              window.ga("set", "page", "/onboarding/page-4/");
              window.ga("set", "title", "Onboarding acceptance");
              window.ga("send", "pageview");
            }
          });
      }
      */ 

    }
  };
</script>

<style lang="scss">
  @import '../../css/_mixins.scss';

  .modal-backdrop {
    opacity: 0.8;
  }

  .carousel-item {
    background: #fff !important;
  }

  .carousel-control-prev-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23000' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E");
  }

  .carousel-control-next-icon {
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%23000' viewBox='0 0 8 8'%3e%3cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3e%3c/svg%3e");
  }


  /*

  .modal-backdrop {
    opacity: 0.8 !important;
  }

  .modal-content {
    background: transparent;
    border: transparent;
  }

  .modal-header {
    border-bottom: transparent;
    position: relative;
    top: 60px;
    z-index: 999;

    button {
      color: #000;
    }
  }

  .modal-body {
    height: 800px;
    padding: 0;
  }

  .carousel-inner {
    height: 800px;
  }

  .carousel-item {
    background: #fff;
    border: transparent;
    height: 800px;
    overflow: scroll;

    padding: 40px 50px;

    @include breakpoint(tablet) {
      padding: 40px 70px !important;
    }

    @include breakpoint(desktop) {
      overflow: hidden;
      padding: 100px !important;
    }
  }

  .carousel-indicators > li {
    background-color: #000;
    border-radius: 50%;
    height: 10px;
    width: 10px;
  }

  .carousel-control-prev-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23000' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E");
  }

  .carousel-control-next-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23000' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E");
  }

  .prereq-onboarding-main {
    background-size: cover;
  }

  .prereq-purple {
    background-color: #4d307f;
    border-color: #4d307f;
  }
  */
</style>
