<template>
    <div class="hero is-fullheight">
        <div>
            <p class="wtg-title has-text-weight-bold is-1">
                {{project.name}}
            </p>
            <p class="subtitle">
                {{project.description}}
            </p>
            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc bibendum nulla tempus, feugiat sem eu, rhoncus lorem. Nulla vestibulum orci nec ante euismod, eget porta neque luctus. Ut eros nunc, finibus nec leo pulvinar, sagittis pharetra neque. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur vehicula nibh vitae metus condimentum, quis bibendum nunc maximus. Nulla erat purus, placerat id iaculis eu, eleifend eget felis. In hac habitasse platea dictumst. Phasellus elementum sapien sit amet diam posuere, nec suscipit nisi vehicula. Sed rutrum tincidunt sapien ut tempor. Nullam consequat at lectus a commodo. Duis feugiat nulla nec arcu efficitur, et convallis orci ultricies. Nunc ac viverra neque.
            </p>
            <br>
            <p>
                <div class="field is-grouped">
                    <div  v-if="project.webpage != ''" class="control">
                        <a :href="project.webpage">Visit</a>
                    </div>
                    <div class="control">
                        <a href="">View Source</a>
                    </div>
                </div>
            </p>
            <div class="columns">
                <div class="column">
                    <img :src="project.getImageUrl()" v-if="project.hasImage()" class="has-border-wtg" />

                </div>
                <div class="column">
                    <p class="subtitle has-text-weight-bold">
                        Contributors
                    </p>
                    <div class="prof-img-holder">
                        <a v-for="contributor in project.contributors" :key="contributor.username" :href="contributor.profileURL">
                            <img :title="contributor.username" :alt="contributor.username" class="contributor-img" :src="contributor.avatarURL" />
                        </a>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>
<script lang="ts">
import Vue from 'vue';
import Project from '../models/project';

export default Vue.extend({
    props: {
        project: {
            type: Project,
        },
    },
});
</script>
<style lang="scss" scoped>

    .contributor-img{
        width: 75px;
        height: 75px;
        margin: 10px;
        // border-style: solid;
        // border-width: 2px;
        // box-shadow: 0 3px 8px 0 #ED1C24;
        // border-color: #ED1C24;
    }

    .prof-img-holder{
        display: flex;
        flex-flow: row wrap;
        justify-content: center;
        
    }

</style>
