<template>
  <div>
    <div class="section has-text-centered">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-fullwidth-tablet is-two-thirds-desktop">
            <p class="wtg-title is-danger is-superlarge-title">
            WebTech
            </p>
            <p class="subtitle is-3 has-text-grey">
              We create technological solutions to serve the students of Rensselaer Polytechnic Institute. Take a look at some of our projects below, and then get involved!
            </p>
          </div>
        </div>
        <div class="columns is-centered">
          <div class="field is-grouped">
            <div class="control">
              <button class="button is-danger">Find WebTech on GitHub</button>
            </div>
            <div class="control">
              <button class="button is-danger">Email WebTech</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="section">
      <div class="container">
        <div>
          <Project />
          <Project />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Project from '@/components/Project.vue'; // @ is an alias to /src

export default Vue.extend({
  name: 'WebTech',
  components: {
    Project,
  },
});
</script>
