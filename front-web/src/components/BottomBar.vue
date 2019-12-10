<template>
  <nav id="bottom-bar-wrapper">
    <v-bottom-navigation
        background-color="#ccc"
        color="white"
        fixed
        height=40
        horizontal
        style="z-index: 100;"
    >
        <v-btn rounded :to="{ name: 'home' }">はじめる<v-icon>fas fa-hand-point-up</v-icon></v-btn>
    </v-bottom-navigation>
  </nav>
</template>

<script>

export default {
  name: "BottomBar",

  components: {
  },

  props: {
  },

  data() {
    return {
    };
  },
};
</script>

<style>
@keyframes bb_show{
    0%{
        /* transform: translateY(100%); */
        opacity: 0;
    }
    100%{
        /* transform: translateY(0); */
        opacity: 1;
    }
}
#bottom-bar-wrapper{
    animation: bb_show 1s;
}

</style>