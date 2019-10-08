<template>
  <v-container fluid>
    <v-row align="center" justify="center" class="display-4">FUKFood</v-row>
  </v-container>
</template>

<script>
export default {
  name: "LoginView",

  components: {},
  data() {
    return {};
  },

  methods: {
    handleLogin(authInfo) {
      return this.$store
        .dispatch("login", authInfo)
        .then(() => {
          // router.pushで異なるurlに遷移できる。
          this.$router.push({ name: "tracker_list" });
        })
        .catch(err => this.throwReject(err));
    },
    throwReject(err) {
      return Promise.reject(err);
    }
  }
};
</script>
