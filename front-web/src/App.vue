<template>
  <v-app id="all-wrapper" class="grey lighten-4">
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import store from "./store";
import NavBar from "@/components/NavBar";

export default {
  name: "App",
  components: {
    NavBar
  },
  data: () => ({
    //
  }),
  computed: {
    authorized: function() {
      console.log(
        store.state.auth.token !== null && store.state.auth.token !== undefined
      );
      return (
        store.state.auth.token !== null && store.state.auth.token !== undefined
      );
    }
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=M+PLUS+Rounded+1c&display=swap');

#all-wrapper{
  font-family: 'M PLUS Rounded 1c', sans-serif;
}
</style>
