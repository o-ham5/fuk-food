<template>
  <!-- ユーザの性格入力のページ -->
  <v-card style="height:100%">
    <div style="margin-left:3%">
      <v-container>
        <v-row>
          <v-col cols="12">
            <div style="margin-top:0%">
              <v-container>
                <v-row>
                  <p>陽？陰？</p>
                </v-row>
                <v-row>
                  <v-slider
                    v-model="inyou"
                    :max="max"
                    :min="min"
                    append-icon="mdi-weather-sunny"
                    prepend-icon="mdi-weather-night"
                  ></v-slider>
                </v-row>
                <v-row>
                  <p>オシャレ？ダサい？</p>
                </v-row>
                <v-row>
                  <v-slider
                    v-model="oshare"
                    :max="max"
                    :min="min"
                    append-icon="mdi-emoticon-cool-outline"
                    prepend-icon="mdi-emoticon-poop"
                  ></v-slider>
                </v-row>
                <v-row>
                  <p>食事にかける熱意はどれくらい？</p>
                </v-row>
                <v-row>
                  <v-slider
                    v-model="shokuji"
                    :max="max"
                    :min="min"
                    append-icon="mdi-fire"
                    prepend-icon="mdi-snowflake"
                  ></v-slider>
                </v-row>
                <v-row>
                  <p>節約にかける熱意はどれくらい？</p>
                </v-row>
                <v-row>
                  <v-slider
                    v-model="setsuyaku"
                    :max="max"
                    :min="min"
                    append-icon="mdi-fire"
                    prepend-icon="mdi-snowflake"
                  ></v-slider>
                </v-row>
                <v-row>
                  <p>相手と自分、どっちを重視する？</p>
                </v-row>
                <v-row>
                  <v-slider
                    v-model="weight"
                    :max="weightMax"
                    :min="weightMin"
                    append-icon="mdi-fire"
                    prepend-icon="mdi-snowflake"
                  ></v-slider>
                </v-row>
              </v-container>
            </div>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-btn outlined class="mr-3" @click="handleSearchClick"
              >検索する</v-btn
            >
            <v-btn outlined class="mr-3" @click="signOutConfirm = true"
              >ログアウト</v-btn
            >
          </v-col>
        </v-row>
      </v-container>
    </div>
  </v-card>
</template>

<script>
import store from "@/store";

export default {
  name: "KuchikomiMedian",

  components: {},

  props: {},

  data() {
    return {
      username: null,
      email: null,
      inyou: 50,
      oshare: 50,
      shokuji: 50,
      setsuyaku: 50,
      min: 0,
      max: 100,
      weightMin: 0,
      weightMax: 1,

      updateConfirm: false,
      updateComplete: false,
      signOutConfirm: false
    };
  },

  mounted() {},

  methods: {
    resetError() {
      this.error = "";
    },

    handleSearchClick() {
      let targetPersonality = {
        inyou: this.inyou,
        oshare: this.oshare,
        shokuji: this.shokuji,
        setsuyaku: this.setsuyaku,
        weight: this.weight
      };
      this.$nextTick(() => {
        this.onUpdateClick(store.state.auth.token, targetPersonality)
          .catch(err => {})
          .then(() => {
            this.updateComplete = true;
            this.updateConfirm = false;
          });
      });
    }
  }
};
</script>

<style scoped></style>
