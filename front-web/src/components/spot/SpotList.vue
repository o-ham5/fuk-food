<template>
  <v-data-table
    :headers="headers"
    :items="spots"
    :items-per-page="5"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title>スポット</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <div class="flex-grow-1"></div>
        <v-btn color="primary" dark class="mb-2" @click="clickRegister()"
          >追加する</v-btn
        >
        <v-dialog v-model="dialog" max-width="500px">
          <v-card>
            <v-card-title>
              <span class="headline">スポット追加</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <!-- <v-text-field v-model="spot_name" label="スポット名"></v-text-field> -->
                    <v-autocomplete
                      label="スポット名"
                      :items="spots"
                      item-text="spot_name"
                      :filter="activeFilter"
                      filled
                    ></v-autocomplete>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-select
                      v-model="area_id"
                      :items="areas"
                      item-text="area_name"
                      item-value="area_id"
                      label="エリア"
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-select
                      v-model="genre_id"
                      :items="genres"
                      item-text="genre_name"
                      item-value="genre_id"
                      label="ジャンル"
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="latitude"
                      label="緯度"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="longitude"
                      label="経度"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="link" label="リンク"></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <div class="flex-grow-1"></div>
              <v-btn color="blue darken-1" text @click="onCancel()"
                >Cancel</v-btn
              >
              <v-btn color="blue darken-1" text @click="onSave()">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.action="{ item }">
      <v-icon small class="mr-2" @click="clickUpdate(item)">edit</v-icon>
      <v-icon small @click="clickDelete(item)">delete</v-icon>
    </template>
  </v-data-table>
</template>

<script>
import { Spot, Genre, Area } from "@/api";

export default {
  name: "SpotList",
  components: {},
  data: () => ({
    headers: [
      { text: "スポット名", value: "spot_name" },
      { text: "エリア", value: "area.area_name" },
      { text: "ジャンル", value: "genre.genre_name" },
      { text: "計算スコア", value: "evaluated_score" },
      { text: "リンク", value: "link" },
      { text: "Actions", value: "action", sortable: false }
    ],
    spots: [],
    dialog: false,
    spot_id: null,
    spot_name: null,
    genres: null,
    genre_id: null,
    areas: null,
    area_id: null,
    latitude: null,
    longitude: null,
    link: null,
    filters: [
      {
        fn: (item, queryText) => item.spot_name.indexOf(queryText) > -1,
        text: "Exact Match"
      }
    ]
  }),
  computed: {
    activeFilter() {
      return this.filters[0].fn;
    }
  },
  created() {
    this.fetchSpotData();
    this.fetchGenreData();
    this.fetchAreaData();
  },
  methods: {
    fetchSpotData() {
      Spot.getList().then(res => {
        this.spots = res;
      });
    },
    fetchGenreData() {
      Genre.getList().then(res => {
        this.genres = res;
      });
    },
    fetchAreaData() {
      Area.getList().then(res => {
        this.areas = res;
      });
    },
    throwReject(err) {
      return Promise.reject(err);
    },
    clickRegister() {
      this.dialog = true;
      this.mode = "register";
    },
    clickUpdate(item) {
      this.dialog = true;
      this.mode = "update";
      this.spot_id = item.spot_id;
      this.spot_name = item.spot_name;
      this.area_id = item.area.area_d;
      this.genre_id = item.genre.genre_id;
    },
    clickDelete(item) {
      Spot.delete(item.spot_id)
        .then(res => {
          this.fetchSpotData();
        })
        .catch(err => this.throwReject(err));
    },
    onSave() {
      let saveInfo = {
        spot_name: this.spot_name,
        genre_id: this.genre_id,
        area_id: this.area_id,
        latitude: this.latitude,
        longitude: this.longitude,
        link: this.link
      };
      if (this.mode === "register") {
        Spot.register(saveInfo)
          .then(res => {
            this.fetchSpotData();
          })
          .catch(err => this.throwReject(err));
        this.dialog = false;
      } else if (this.mode === "update") {
        Spot.update(this.spot_id, saveInfo)
          .then(res => {
            this.fetchSpotData();
          })
          .catch(err => this.throwReject(err));
        this.dialog = false;
      }
    },
    onCancel() {
      this.dialog = false;
    }
  }
};
</script>
