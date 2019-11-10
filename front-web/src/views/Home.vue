<template>
  <div style="background-color: #B3E5FC; height: 100%">
    <NavBar
      :inverted-scroll="invertedScroll"
      :scroll-threshold="scrollThreshold"
      :color="color"
    />
    <v-container>
      <v-row>
        <!-- 総合ランキング -->
        <v-col cols="4">
          <v-card style="height: 100%">
            <v-container>
              <v-row style="margin: 3%">
                <p class="display-1">総合ランキング</p>
                <v-select
                  v-model="top3SelectedGenre"
                  :items="genres"
                  item-text="genre_name"
                  item-value="genre_id"
                  label="ジャンルで絞り込む"
                ></v-select>
                <v-select
                  v-model="top3SelectedArea"
                  :items="areas"
                  item-text="area_name"
                  item-value="area_id"
                  label="エリアで絞り込む"
                ></v-select>
              </v-row>
              <v-row style="margin: 3%">
                <v-btn small @click="searchTop3">検索する</v-btn>
                <v-btn small style="margin-left: 5%" @click="clearTop3"
                  >条件をクリアする</v-btn
                >
              </v-row>
              <div v-if="top3SearchProgressing">
                <v-progress-circular
                  indeterminate
                  color="primary"
                ></v-progress-circular>
              </div>
              <div v-if="top3NotFountdMsg">{{ top3NotFountdMsg }}</div>
              <div v-if="top3">
                <v-row
                  v-for="(item, idx) in top3.slice(0, 3)"
                  style="margin: 3%"
                >
                  <v-col cols="4">
                    <v-img v-if="idx == 0" src="@/assets/ranking01.png"></v-img>
                    <v-img v-if="idx == 1" src="@/assets/ranking02.png"></v-img>
                    <v-img v-if="idx == 2" src="@/assets/ranking03.png"></v-img>
                  </v-col>
                  <v-col cols="8">
                    <p>
                      <a :href="item.link" target="_blank">
                        {{ item.spot_name }}
                      </a>
                    </p>
                    <p>{{ item.evaluated_score.toFixed(2) }}&emsp;ポイント</p>
                  </v-col>
                </v-row>
              </div>
            </v-container>
          </v-card>
        </v-col>

        <!-- あなたに似た人が好きな店 -->
        <v-col cols="4">
          <v-card style="height: 100%">
            <v-container>
              <v-row style="margin: 3%">
                <p class="display-1">あなたに似た人が好きなお店</p>
              </v-row>
              <v-row v-for="item in neighborsKuchikomis" style="margin: 3%">
                <v-col cols="3">
                  <v-row>
                    <p>{{ item.account.username }}さん</p>
                  </v-row>
                </v-col>
                <v-col cols="9">
                  <p>{{ item.spot.spot_name }}</p>
                  <p>{{ item.score }}</p>
                  <p>{{ item.comment }}</p>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-col>

        <!-- ぴったりスポット検索 -->
        <v-col cols="4">
          <v-card style="height:100%">
            <div style="margin-left:3%">
              <v-container>
                <v-row style="margin: 3%">
                  <p class="display-1">ぴったりスポット検索</p>
                </v-row>
                <v-row>
                  <v-col cols="12">
                    <div style="margin-top:0%">
                      <v-container>
                        <v-row>
                          <p>相手の陽キャ度は？</p>
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
                          <p>相手のオシャレ度は？</p>
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
                          <p>相手が食事にかける熱意はどれくらい？</p>
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
                          <p>相手が節約にかける熱意はどれくらい？</p>
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
                          <v-slider v-model="weight" :max="max" :min="min">
                            <template v-slot:prepend>
                              <p>自分</p>
                            </template>
                            <template v-slot:append>
                              <p>相手</p>
                            </template>
                          </v-slider>
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
                  </v-col>
                  <!-- API通信が完了してsearchProgressingがfalseになるまでローディングを表示 -->
                  <v-col>
                    <v-progress-circular
                      v-show="searchProgressing"
                      indeterminate
                      color="primary"
                    ></v-progress-circular>
                  </v-col>
                </v-row>
              </v-container>
            </div>
          </v-card>
        </v-col>
      </v-row>

      <!-- 検索結果ダイアログ APIの結果が帰ってきたら表示される -->
      <v-dialog v-model="showResult" max-width="700">
        <v-card>
          <v-container>
            <v-row style="margin: 3%">
              <p class="display-1">検索結果</p>
            </v-row>
            <v-row
              v-for="item in virtualNeighborsKuchikomis"
              style="margin: 3%"
            >
              <v-col cols="3">
                <v-row>
                  <p>{{ item.account.username }}さん</p>
                </v-row>
              </v-col>
              <v-col cols="9">
                <p>{{ item.spot.spot_name }}</p>
                <p>{{ item.score }}</p>
                <p>{{ item.comment }}</p>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-dialog>

      <v-row align="center" justify="center">
        <v-col>
          <v-card @click="toKuchikomi()">
            <v-card-text>
              <v-container>
                <v-row>口コミを書く</v-row>
                <v-row>
                  <p>{{ message }}</p>
                </v-row>
              </v-container>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col>
          <v-card :to="{ name: 'spot' }">
            <v-card-text>
              <v-container>
                <v-row>新しくスポットを追加する</v-row>
              </v-container>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col>
          <v-card :to="{ name: 'meta' }">
            <v-card-text>
              <v-container>
                <v-row>メタ情報を管理する</v-row>
              </v-container>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import spot from "@/api/spot";
import genre from "@/api/genre";
import area from "@/api/area";
import kuchikomi from "@/api/kuchikomi";
import store from "@/store";

export default {
  name: "Home",

  components: {
    NavBar
  },
  data() {
    return {
      invertedScroll: false,
      scrollThreshold: 500,
      color: "#B3E5FC",

      spots: null,
      top3: null,
      rankImage: [
        "@/assets/ranking01.png",
        "@/assets/ranking02.png",
        "@/assets/ranking03.png"
      ],

      neighborsKuchikomis: [],
      virtualNeighborsKuchikomis: [],
      genres: [],
      areas: [],

      inyou: 50,
      oshare: 50,
      shokuji: 50,
      setsuyaku: 50,
      weight: 50,
      max: 100,
      min: 0,

      searchProgressing: false,
      showResult: false,

      top3SelectedGenre: null,
      top3SelectedArea: null,
      top3NotFountdMsg: null,
      top3SearchProgressing: false,

      message: null
    };
  },
  computed: {
    authorized: function() {
      return (
        store.state.auth.token !== null && store.state.auth.token !== undefined
      );
    }
  },

  created() {
    this.fetchTop3();
    this.fetchNeighborsKuchikomis();
    this.fetchGenreList();
    this.fetchAreaList();
  },
  methods: {
    toKuchikomi() {
      if (this.authorized) {
        this.$router.push({ name: "kuchikomi" });
      } else {
        this.message = "サインインしてください！";
      }
    },
    fetchTop3() {
      spot.getTop3List().then(res => {
        this.top3 = Object.values(res);
      });
    },
    fetchSpotList() {
      spot.getList().then(res => {
        this.spots = Object.values(res);
      });
    },
    fetchGenreList() {
      genre.getList().then(res => {
        this.genres = Object.values(res);
      });
    },
    fetchAreaList() {
      area.getList().then(res => {
        this.areas = Object.values(res);
      });
    },
    fetchNeighborsKuchikomis() {
      kuchikomi.getNeighborsList(store.state.auth.token).then(res => {
        this.neighborsKuchikomis = res;
      });
    },
    handleSearchClick() {
      let targetPersonality = {
        inyou: this.inyou,
        oshare: this.oshare,
        shokuji: this.shokuji,
        setsuyaku: this.setsuyaku,
        weight: this.weight
      };
      kuchikomi
        .getMedianList(store.state.auth.token, targetPersonality)
        .then(res => {
          this.virtualNeighborsKuchikomis = res;
          this.searchProgressing = false;
          this.showResult = true;
        });
      this.searchProgressing = true;
    },
    searchTop3() {
      this.top3SearchProgressing = true;
      let query = {
        area_id: this.top3SelectedArea,
        genre_id: this.top3SelectedGenre
      };
      spot.getTop3List(query).then(res => {
        if (res.length) {
          this.top3NotFountdMsg = null;
          this.top3 = Object.values(res);
          this.top3SearchProgressing = false;
        } else {
          this.top3 = [];
          this.top3NotFountdMsg = "お探しのお店は見つかりませんでした。";
          this.top3SearchProgressing = false;
        }
      });
    },
    clearTop3() {
      this.top3SearchProgressing = true;
      this.top3NotFountdMsg = null;
      this.top3SelectedGenre = null;
      this.top3SelectedArea = null;
      spot.getTop3List().then(res => {
        this.top3 = Object.values(res);
        this.top3SearchProgressing = false;
      });
    }
  }
};
</script>

<style></style>
