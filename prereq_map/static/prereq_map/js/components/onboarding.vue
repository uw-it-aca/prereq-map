<template>
<div style="margin: 30px;">

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
                            <div class="carousel-item active" style="background:purple;">
                                <h2 class="text-white">Discover courses and plan your schedule more effectively</h2>
                                <div class="text-white">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce finibus mi placerat libero feugiat fermentum. Duis posuere, nibh quis scelerisque iaculis, lorem ante mollis ante, rhoncus hendrerit nulla turpis ut
                                    est. Morbi vestibulum mi id sem vehicula sodales et in ex. Donec sit amet tincidunt massa. Nullam molestie, ligula a euismod laoreet, risus sem bibendum ante, ultricies condimentum ligula turpis nec lacus. Sed
                                    convallis lacinia nisi, eu accumsan dui vulputate et. Morbi accumsan neque a tortor lobortis ornare. Nunc facilisis laoreet erat vehicula rutrum. Integer vel dapibus metus. Quisque facilisis turpis id libero
                                    vulputate dictum. Fusce facilisis arcu congue aliquam molestie. Pellentesque eros justo, efficitur ut tortor vel, hendrerit porta ipsum. Cras posuere scelerisque massa sit amet pulvinar.</div>

                                <div class="text-center mt-5">
                                    <div><a href="#" target="_blank">Read further details on IT Connect</a></div>
                                </div>

                            </div>
                            <div class="carousel-item">
                                <h2>See the prerequisite map for a curriculum (e.g. Biology, BIOL)</h2>
                                <div>Sed nulla lacus, pharetra eget urna id, vestibulum dictum urna. Aliquam metus ipsum, aliquet ut ante eget, dapibus facilisis augue. Pellentesque urna nisi, cursus vitae scelerisque a, semper eget enim. Nullam
                                    gravida consequat felis. Mauris quis lectus tellus. Donec vitae libero ipsum. Aliquam erat volutpat.</div>
                            </div>
                            <div class="carousel-item">
                                <h2>Get more course info</h2>
                                <div>Fusce ut semper dui. Vestibulum condimentum, arcu in imperdiet dapibus, sem lorem scelerisque metus, ut vestibulum nisl dolor dignissim neque. Fusce commodo lobortis orci sed blandit. Vestibulum ante ipsum primis
                                    in faucibus orci luctus et ultrices posuere cubilia Curae; Cras lacinia libero nec enim rutrum, non pellentesque magna congue. In augue turpis, ultricies eget porta a, ornare sit amet quam. Quisque ut porttitor
                                    ipsum. Duis a dolor in risus porttitor sagittis ut in urna. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur sagittis varius lacus ut feugiat. Maecenas
                                    placerat ex tempus odio imperdiet, pharetra varius tortor fringilla. Duis sit amet semper ligula. Fusce leo velit, posuere at varius sed, ultrices in massa. Aliquam auctor placerat lacinia. Maecenas vestibulum
                                    cursus turpis, a posuere massa mattis ut. Nunc et semper odio.</div>
                            </div>
                            <div class="carousel-item">
                                <h2>Get more course details and find related curricula</h2>
                                <div>Fusce ut semper dui. Vestibulum condimentum, arcu in imperdiet dapibus, sem lorem scelerisque metus, ut vestibulum nisl dolor dignUt non massa auctor, fermentum ipsum quis, porttitor ex. Nullam dignissim congue
                                    ornare. Duis purus ipsum, mollis at luctus vel, aliquam id dui. Phasellus mattis ut mi at tincidunt. Aliquam a rhoncus augue, non tempus enim. Fusce vitae egestas ante. Morbi euismod arcu sed odio posuere
                                    tincidunt.</div>

                                <div class="text-center mt-5">
                                    <button v-on:click="accept" class="btn btn-primary">Get Started!</button>
                                </div>

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
        return {

        }
    },
    mounted() {

        // TODO: hit the term API and get the last day of current term

        // check if valid cookie exists
        if ($cookies.get('onboarding-accepted') == 'false') {
            // show the onboarding modal
            $('#onboardingModal').modal({backdrop: 'static', keyboard: false});
        }
    },
    methods: {

        accept: function(event) {
            // set a cookie to track that user has seen the onboarding and
            // TODO: set the cookie expiration to the last day of current term
            // plus 1 second
            $cookies.set('onboarding-accepted', 'true', 1);
            $('#onboardingModal').modal('hide');
        }

    }

}
</script>

<style lang="scss">

    .modal-backdrop { opacity: 0.8 !important; }
    .modal-content { background: transparent; border: none; }
    .modal-header { border-bottom: none; position: relative; z-index: 999; top: 60px;
        button { color: #000; }
    }
    .modal-body { padding: 0; height: 600px; }

    .carousel-inner { height: 600px; }
    .carousel-item { height: 600px; overflow: scroll; padding: 50px 100px !important; border: none; background: #fff; }

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

</style>
