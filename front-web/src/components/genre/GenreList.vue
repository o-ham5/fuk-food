<template>
  <v-data-table
    :headers="headers"
    :items="genres"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
import { Genre } from "@/api";

export default {
  name: "GenreList",
  components: {},
  data: () => ({
    headers: [
      {
        text: "ID",
        value: "genre_id"
      },
      { text: "ジャンル", value: "genre_name" }
    ],
    genres: []
  }),
  created() {
    this.fetchGenreData();
  },
  methods: {
    fetchGenreData() {
      Genre.getList().then(res => {
        this.genres = res;
      });
    }
  }
};
</script>
