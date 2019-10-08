<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <AreaList />
        <AreaAdd />
        <SituationList />
        <SituationAdd />
        <GenreList class="mt-3" />
        <GenreAdd />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import AreaList from "@/components/area/AreaList";
import AreaAdd from "@/components/area/AreaAdd";
import SituationList from "@/components/situation/SituationList";
import SituationAdd from "@/components/situation/SituationAdd";
import GenreList from "@/components/genre/GenreList";
import GenreAdd from "@/components/genre/GenreAdd";
import SpotList from "@/components/spot/SpotList";

export default {
  name: "Home",
  components: {
    AreaList,
    AreaAdd,
    SituationList,
    SituationAdd,
    GenreList,
    GenreAdd,
    SpotList
  }
};
</script>
