<template>
  <v-data-table
    :headers="headers"
    :items="situations"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table>
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
        value: "id"
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
        console.log(res);
        this.situations = res;
      });
    }
  }
};
</script>
