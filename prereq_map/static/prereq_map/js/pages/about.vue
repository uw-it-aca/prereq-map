// about.vue

<template>
  <b-container>
    <b-row class="justify-content-center">
      <b-col md="9">
        <h1 class="h3 mb-4">About Prereq Map</h1>
        <h2 class="h4">
          Discover courses and plan your schedule more effectively
        </h2>
        <p class="font-weight-lighter">
          It can be tough figuring out which courses to take. How do you find
          courses similar to ones you’ve really enjoyed? Of the courses you’ve
          already taken, which ones provide a foundation for more advanced
          coursework? What sequence of courses is best? The
          <strong>Prereq Map</strong> helps you discover interesting courses and
          enables you to be strategic about planning your course schedule. (What’s a
          prereq? Prereq is short for prerequisites: the courses that act as a
          foundation for other courses.)
        </p>

        <b-img
          src="/static/prereq_map/img/onboarding-biol.png"
          fluid-grow
          alt="Onboarding curriculum example"
          class="border border-secondary mb-5"
        />

        <h2 class="h4">
          See the prerequisite map for a curriculum
          <small>(e.g. Biology, BIOL)</small>
        </h2>
        <p class="font-weight-lighter">
          Begin exploring the Prereq Map by choosing a curriculum (subjects
          comprising a discipline, e.g., Biology or BIOL) you’re interested in.
          Follow the lines to view prerequisites for courses. View courses that have
          prereqs and courses that are prereqs for other courses.
        </p>

        <b-img
          src="/static/prereq_map/img/onboarding-infobox.png"
          fluid-grow
          alt="Onboarding Infobox example"
          class="border border-secondary mb-5"
        />
        <h2 class="h4">
          Get additional info about a course
        </h2>
        <p class="font-weight-lighter">
          Each square on the map represents a specific course. Click the square to
          view prerequisite information for the course. Click the links in the
          sidebar to learn more.
        </p>

        <b-img
          src="/static/prereq_map/img/onboarding-course-details.png"
          fluid-grow
          alt="Onboarding course details example"
          class="border border-secondary mb-5"
        />
        <h2 class="h4">
          Get more course detail and find related curricula
        </h2>
        <p class="font-weight-lighter mb-5">
          On the Course Search page, click links to browse related course offerings.
          You can also explore related curricula and their prerequisite maps.
        </p>

        <h2 class="h4">
          Important notes:
        </h2>

        <ul class="font-weight-lighter">
          <li>
            Prereq Map shows current prerequisites. When planning several quarters
            out, keep in mind that prerequisites may change over time.
          </li>
          <li>
            Prereq Map is based solely on course prerequisites and does not take
            into account specific requirements for graduation.
          </li>
          <li>
            Not all equivalencies (e.g. placement tests) are represented in the map
            – just courses. You can find some equivalencies in the text description.
          </li>
          <li>
            Remember to talk to your adviser when course planning.
          </li>
        </ul>

        <div class="text-center">
          <a
            @click="
              $ga.event(
                'outbound',
                'click',
                'https://itconnect.uw.edu/learn/tools/prereq-map/'
              )"
            @keydown="
              $ga.event(
                'outbound',
                'click',
                'https://itconnect.uw.edu/learn/tools/prereq-map/'
              )"
            href="https://itconnect.uw.edu/learn/tools/prereq-map/" target="_blank"
          >
            Additional details
          </a>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
  export default {
    name: "About"
  };
</script>

<style lang="scss">
</style>
