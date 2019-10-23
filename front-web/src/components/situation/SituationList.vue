<template>
  <v-data-table :headers="headers" :items="situations" :items-per-page="5" class="elevation-1"></v-data-table>
</template>

<script>
import { Situation } from "@/api";

export default {
  name: "SituationList",
  components: {},
  data: () => ({
    headers: [
      {
        text: "ID",
        value: "situation_id"
      },
      { text: "シチュエーション", value: "situation_name" }
    ],
    situations: []
  }),
  created() {
    this.fetchSituationData();
  },
  methods: {
    fetchSituationData() {
      Situation.getList().then(res => {
        this.situations = res;
      });
    }
  }
};
</script>
