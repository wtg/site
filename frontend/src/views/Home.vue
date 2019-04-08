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
          <ProjectVue v-for="project in Projects" :project="project" :key="project.name"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import ProjectVue from '@/components/Project.vue'; // @ is an alias to /src
import Project from '../models/project';

export default Vue.extend({
  name: 'WebTech',
  components: {
    ProjectVue,
  },
  data (){
    return {
      Projects: [],
    } as {
      Projects: Project[];
    }
  }, 
  mounted(){
    this.fetchData();
  },
  methods: {
    fetchData(){
      let ret: Project[] = [];
      fetch("/api/projects").then(data => data.json()).then(val => {
        console.log(val)
        val.forEach(element => {
          let p = new Project(element.name, element.repo.html_url, element.repo.description);
          ret.push(p);
        });
        this.Projects = ret;
      });
    }
  }
});
</script>
