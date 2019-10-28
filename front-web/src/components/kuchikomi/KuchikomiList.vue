<template>
  <v-data-table
    :headers="headers"
    :items="kuchikomis"
    :items-per-page="50"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title>口コミ</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <div class="flex-grow-1"></div>
        <v-btn color="primary" dark class="mb-2" @click="clickRegister()"
          >投稿する</v-btn
        >
        <v-dialog v-model="dialog" max-width="500px">
          <v-card>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-select
                      v-model="spot"
                      :items="spots"
                      item-text="spot_name"
                      item-value="spot_id"
                      label="スポット"
                      return-object
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-select
                      v-model="situation"
                      :items="situations"
                      item-text="situation_name"
                      item-value="situation_id"
                      label="シチュエーション"
                      return-object
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="price"
                      label="一人当たり金額(円)"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="score" label="スコア"></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12">
                    <v-text-field
                      v-model="comment"
                      label="コメント"
                    ></v-text-field>
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
import { Spot, Situation, Kuchikomi } from "@/api";
import store from "@/store";

export default {
  name: "KuchikomiList",
  components: {},
  data: () => ({
    dialog: false,
    headers: [
      { text: "スポット", value: "spot.spot_name" },
      { text: "投稿者", value: "account.username" },
      { text: "シチュエーション", value: "situation.situation_name" },
      { text: "一人当たり金額", value: "price" },
      { text: "スコア", value: "score" },
      { text: "偏差値", value: "deviation" },
      { text: "コメント", value: "comment" },
      { text: "投稿日", value: "created_at" },
      { text: "Actions", value: "action", sortable: false }
    ],
    kuchikomis: [],
    kuchikomi_id: null,
    spots: [],
    spot: null,
    spot_id: null,
    spot_name: null,
    situations: [],
    situation: null,
    situation_id: null,
    situation_name: null,
    price: null,
    score: null,
    deviation: null,
    comment: null
  }),
  created() {
    this.fetchSpotData();
    this.fetchSituationData();
    this.fetchKuchikomiData();
  },
  methods: {
    fetchSpotData() {
      Spot.getList().then(res => {
        console.log(res);
        this.spots = res;
      });
    },
    fetchSituationData() {
      Situation.getList().then(res => {
        this.situations = res;
      });
    },
    fetchKuchikomiData() {
      Kuchikomi.getList().then(res => {
        this.kuchikomis = res;
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
      console.log(item);
      this.dialog = true;
      this.mode = "update";
      this.kuchikomi_id = item.kuchikomi_id;
      this.spot = item.spot;
      this.spot_id = item.spot.spot_id;
      this.spot_name = item.spot.spot_name;
      this.situation = item.situation;
      this.situation_id = item.situation.situation_id;
      this.situation_name = item.situation.situation_name;
      this.price = item.price;
      this.score = item.score;
      this.comment = item.comment;
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
        spot_id: this.spot.spot_id,
        situation_id: this.situation.situation_id,
        account_id: store.state.user.account_id,
        price: this.price,
        score: this.score,
        comment: this.comment
      };
      if (this.mode === "register") {
        Kuchikomi.register(saveInfo)
          .then(res => {
            this.fetchKuchikomiData();
            this.clearData();
          })
          .catch(err => this.throwReject(err));
        this.dialog = false;
      } else if (this.mode === "update") {
        console.log(saveInfo);
        Kuchikomi.update(this.kuchikomi_id, saveInfo)
          .then(res => {
            this.fetchKuchikomiData().then(res => {
              this.clearData();
            });
          })
          .catch(err => this.throwReject(err));
        this.dialog = false;
      }
    },
    onCancel() {
      this.dialog = false;
    },
    clearData() {
      this.spot = null;
      this.situation = null;
      this.price = null;
      this.score = null;
      this.comment = null;
    }
  }
};
</script>
