<template>

  <div style="margin: 30px;">

    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter">Launch Onboarding</button>

  <!-- Modal -->
  <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">

      <div class="modal-content" v-if="step === 1">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLongTitle">Step One</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ligula leo, aliquet ac convallis eu, semper eget massa. Cras sagittis mollis aliquam. Cras eu sapien commodo dolor lobortis commodo non vitae magna. Donec vehicula quam eu malesuada malesuada. Fusce facilisis augue in nunc tristique, at efficitur nisi ultricies. Suspendisse sit amet metus suscipit, laoreet justo in, tempor odio. Duis scelerisque malesuada lorem, ut maximus arcu. Nam dictum sollicitudin est, quis feugiat justo consectetur eget. Nullam commodo eleifend lorem sit amet eleifend. Integer nec enim sed sapien tristique feugiat. Nullam ac ex eget elit efficitur hendrerit ut sit amet sem. Proin pellentesque efficitur justo sed pretium. Duis vel ipsum vitae tortor egestas tristique non vel lectus. Ut bibendum, eros id ullamcorper tempor, ligula dui scelerisque elit, sed pulvinar diam velit et purus.</p>
        </div>
        <div class="modal-footer">
          <button @click.prevent="next()">Next</button>
        </div>
      </div>


      <div class="modal-content" v-if="step === 2">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLongTitle">Step two</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ligula leo, aliquet ac convallis eu, semper eget massa. Cras sagittis mollis aliquam. Cras eu sapien commodo dolor lobortis commodo non vitae magna. Donec vehicula quam eu malesuada malesuada. Fusce facilisis augue in nunc tristique, at efficitur nisi ultricies. Suspendisse sit amet metus suscipit, laoreet justo in, tempor odio. Duis scelerisque malesuada lorem, ut maximus arcu. Nam dictum sollicitudin est, quis feugiat justo consectetur eget. Nullam commodo eleifend lorem sit amet eleifend. Integer nec enim sed sapien tristique feugiat. Nullam ac ex eget elit efficitur hendrerit ut sit amet sem. Proin pellentesque efficitur justo sed pretium. Duis vel ipsum vitae tortor egestas tristique non vel lectus. Ut bibendum, eros id ullamcorper tempor, ligula dui scelerisque elit, sed pulvinar diam velit et purus.</p>
        </div>
        <div class="modal-footer">
          <button @click.prevent="prev()">Previous</button>
          <button @click.prevent="next()">Next</button>
        </div>
      </div>

      <div class="modal-content" v-if="step === 3">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLongTitle">Step Three</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ligula leo, aliquet ac convallis eu, semper eget massa. Cras sagittis mollis aliquam. Cras eu sapien commodo dolor lobortis commodo non vitae magna. Donec vehicula quam eu malesuada malesuada. Fusce facilisis augue in nunc tristique, at efficitur nisi ultricies. Suspendisse sit amet metus suscipit, laoreet justo in, tempor odio. Duis scelerisque malesuada lorem, ut maximus arcu. Nam dictum sollicitudin est, quis feugiat justo consectetur eget. Nullam commodo eleifend lorem sit amet eleifend. Integer nec enim sed sapien tristique feugiat. Nullam ac ex eget elit efficitur hendrerit ut sit amet sem. Proin pellentesque efficitur justo sed pretium. Duis vel ipsum vitae tortor egestas tristique non vel lectus. Ut bibendum, eros id ullamcorper tempor, ligula dui scelerisque elit, sed pulvinar diam velit et purus.</p>
        </div>
        <div class="modal-footer">
          <button @click.prevent="prev()">Previous</button>
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        </div>
      </div>

    </div>
  </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      step: 1
    }
  },
  methods: {
    prev() {
      this.step--;
    },
    next() {
      this.step++;
    },
    close() {
      alert('Close the modal!');
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
