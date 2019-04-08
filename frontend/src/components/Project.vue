<template>
    <div class="hero is-fullheight">
        <div>
            <p class="wtg-title is-1">
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
                    <div class="control">
                        <a href="">Visit</a>

                    </div>
                    <div class="control">
                        <a href="">View Source</a>
                    </div>
                </div>
            </p>
        </div>
    </div>
</template>
<script lang="ts">
import Vue from 'vue';
import Project from '../models/project';

export default Vue.extend({
    props: {
        project:{
            type: Project,
        }
    }
});
</script>
<style lang="scss" scoped>

</style>
