<template>
  <v-app id="main-wrapper" class="grey lighten-4">
    <NavBar />
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
#main-wrapper{
  transition: 1s;
}

</style>