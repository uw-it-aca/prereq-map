<template>
<div v-cloak>
    <!-- Modal -->
    <div class="modal fade" id="onboardingModal" tabindex="-1" role="dialog" aria-labelledby="" aria-hidden="true">
        <div class="modal-dialog modal-lg modal-dialog-centered" role="document">

            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">

                    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel" data-interval="false">
                        <ol class="carousel-indicators">
                            <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                            <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                            <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                            <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
                        </ol>
                        <div class="carousel-inner rounded-lg">
                            <div class="carousel-item active prereq-blah" style="background-image:url('/static/prereq_map/img/modal-bg.jpg');">
                                <h2 class="text-white mb-5">Discover courses and plan your schedule more effectively</h2>

                                <p class="text-white">It can be tough figuring out which courses to take. How do you find courses similar to ones you’ve really enjoyed? Of the courses you’ve already taken, which ones provide a foundation for more advanced coursework? What sequence of courses is best? The Prereq Map helps you discover interesting courses and enables you to be strategic about planning your course schedule. (What’s a prereq? Prereq is short for prerequisites: the courses that act as a foundation for other courses.)</p>

                                <p class="text-white">The Prereq Map shows current prerequisites. When planning several quarters out, keep in mind that prerequisites may change. Also note that the Prereq Map is based solely on course prerequisites and does not take into account specific requirements for graduation.</p>

                                <div class="text-center mt-3">
                                    <div><a href="#" target="_blank">Further details</a></div>
                                </div>

                                <div class="text-center mt-2">
                                    <button v-on:click="accept" class="btn btn-primary">Got it!</button>
                                </div>

                            </div>
                            <div class="carousel-item">
                                <h2 class="mb-5">See the prerequisite map for a curriculum (e.g. Biology, BIOL)</h2>
                                <p>Begin exploring the Prereq Map by choosing a curricula (subjects comprising a course of study) you’re interested in. Follow the lines to see the prerequisites for courses. View courses that have prereqs and courses that are prereqs for other courses. </p>
                            </div>
                            <div class="carousel-item">
                                <h2 class="mb-5">Get additional info about a course</h2>
                                <p>Each node on the map represents a specific course. Click the node to view prerequisite information for the course. Click the links inside the node to learn more.</p>
                            </div>
                            <div class="carousel-item">
                                <h2 class="mb-5">Get more course detail and find related curricula.</h2>
                                <p>On the Course Search page, click links to browse related course offerings. You can also explore related curricula and their prerequisite maps.</p>
                            </div>
                        </div>
                        <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="sr-only">Previous</span>
                        </a>
                        <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="sr-only">Next</span>
                        </a>
                    </div>

                </div>

            </div>

        </div>
    </div>

</div>
</template>

<script>
import Vue from 'vue'
import VueCookies from 'vue-cookies'
Vue.use(VueCookies)

export default {
    data() {
        return { }
    },
    mounted() {
        // check if valid cookie exists and user has not yet accepted terms
        if ($cookies.get('prereq-onboarding-accepted') == 'false') {
            // show the onboarding modal
            $('#onboardingModal').modal({backdrop: 'static', keyboard: false})
        }
    },
    methods: {

        // handle the 'get started' button click event
        accept: function(event) {
            // get the end of term date and set as the expiration value
            var expires = $cookies.get('prereq-onboarding-expires')
            // set the accept cookie value to true and set the expiration
            $cookies.set('prereq-onboarding-accepted', 'true', expires)
            $cookies.remove("prereq-onboarding-expires");

            // hide the modal (until end of the current term)
            $('#onboardingModal').modal('hide')
        }

    }

}
</script>

<style lang="scss">

@import '../../css/_mixins.scss';

.modal-backdrop {
    opacity: 0.8 !important;
}
.modal-content {
    background: transparent;
    border: none;
}
.modal-header {
    border-bottom: none;
    position: relative;
    z-index: 999;
    top: 60px;
    button {
        color: #000;
    }
}
.modal-body {
    padding: 0;
    height: 600px;
}

.carousel-inner {
    height: 600px;
}
.carousel-item {
    height: 600px;
    overflow: scroll;

    padding: 40px 50px;

    @include breakpoint(tablet) {
        padding: 40px 70px !important;
    }

    @include breakpoint(desktop) {
        padding: 40px 100px !important;
    }

    border: none;
    background: #fff;
}

.carousel-indicators > li {
    border-radius: 50%;
    height: 10px;
    width: 10px;
    background-color: #000;
}

.carousel-control-prev-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23000' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E");
}

.carousel-control-next-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23000' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E");
}

.prereq-blah {
    background-size: cover;
}
</style>
