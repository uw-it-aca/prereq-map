// about.vue

<template>
  <div id="course" class="container">
    <h1>About Prereq Map</h1>
    <h2 class="h3">
      Discover courses and plan your schedule more effectively
    </h2>
    <p>
      It can be tough figuring out which courses to take. How do you find
      courses similar to ones you’ve really enjoyed? Of the courses you’ve
      already taken, which ones provide a foundation for more advanced
      coursework? What sequence of courses is best? The
      <strong>Prereq Map</strong> helps you discover interesting courses and
      enables you to be strategic about planning your course schedule. (What’s a
      prereq? Prereq is short for prerequisites: the courses that act as a
      foundation for other courses.)
    </p>
    <p>Remember to talk to your adviser when course planning.</p>

    <b-img
      src="/static/prereq_map/img/onboarding-biol.png"
      fluid
      alt="Onboarding curriculum example"
      style="border: solid 2px #333;"
    />
    <p class="mt-4 mb-4 h3">
      See the prerequisite map for a curriculum
      <small>(e.g. Biology, BIOL)</small>
    </p>
    <p>
      Begin exploring the Prereq Map by choosing a curriculum (subjects
      comprising a discipline, e.g., Biology or BIOL) you’re interested in.
      Follow the lines to view prerequisites for courses. View courses that have
      prereqs and courses that are prereqs for other courses.
    </p>

    <b-img
      src="/static/prereq_map/img/onboarding-infobox.png"
      fluid
      alt="Onboarding Infobox example"
      style="border: solid 2px #333;"
    />
    <p class="mt-4 mb-4 h3">
      Get additional info about a course
    </p>
    <p>
      Each square on the map represents a specific course. Click the square to
      view prerequisite information for the course. Click the links in the
      sidebar to learn more.
    </p>

    <b-img
      src="/static/prereq_map/img/onboarding-course-details.png"
      fluid
      alt="Onboarding course details example"
      style="border: solid 2px #333;"
    />
    <p class="mt-4 mb-4 h3">
      Get more course detail and find related curricula
    </p>
    <p>
      On the Course Search page, click links to browse related course offerings.
      You can also explore related curricula and their prerequisite maps.
    </p>

    <p class="h6">
      <strong>Important notes:</strong>
    </p>

    <ul>
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

    <div>
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
  </div>
</template>

<script>
  export default {
    name: "About"
  };
</script>

<style lang="scss">
</style>
