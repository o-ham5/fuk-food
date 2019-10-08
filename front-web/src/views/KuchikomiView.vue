<template>
  <v-container>
    <KuchikomiList />
  </v-container>
</template>

<script>
import KuchikomiList from "@/components/kuchikomi/KuchikomiList";

export default {
  name: "KuchikomiView",

  components: {
    KuchikomiList
  },
  data() {
    return {};
  },

  methods: {
    throwReject(err) {
      return Promise.reject(err);
    }
  }
};
</script>
