<template>
  <v-data-table
    :headers="headers"
    :items="areas"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
import { Area } from "@/api";

export default {
  name: "AreaList",
  components: {},
  data: () => ({
    headers: [
      {
        text: "ID",
        value: "id"
      },
      { text: "エリア名", value: "area_name" }
    ],
    areas: []
  }),
  created() {
    this.fetchAreaData();
  },
  methods: {
    fetchAreaData() {
      Area.getList().then(res => {
        console.log(res);
        this.areas = res;
      });
    }
  }
};
</script>
