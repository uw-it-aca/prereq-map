<template>
  <div style="margin-bottom:25px;">
    <button class="blah" v-on:click="count++">You clicked me {{ count }} times. {{ blah }}. (single file component)</button>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        count: 0,
        blah: 'This is extra!'
      }
    }
  }
</script>

<style>
.blah { color: red; }
</style>
