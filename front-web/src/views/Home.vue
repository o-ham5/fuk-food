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
                <p class="display-2">総合ランキング</p>
              </v-row>
              <v-row style="margin: 3%">
                <v-col cols="4">
                  <v-img src="@/assets/ranking01.png"></v-img>
                </v-col>
                <v-col cols="8">
                  <div v-if="!loading">
                    <p>
                      <a :href="top3[0].link" target="_blank">
                        {{ top3[0].spot_name }}
                      </a>
                    </p>
                    <p>
                      {{ top3[0].evaluated_score.toFixed(2) }}&emsp;ポイント
                    </p>
                  </div>
                </v-col>
              </v-row>
              <v-row style="margin: 3%">
                <v-col cols="4">
                  <v-img src="@/assets/ranking02.png"></v-img>
                </v-col>
                <v-col cols="8">
                  <div v-if="!loading">
                    <p>
                      <a :href="top3[1].link" target="_blank">
                        {{ top3[1].spot_name }}
                      </a>
                    </p>
                    <p>
                      {{ top3[1].evaluated_score.toFixed(2) }}&emsp;ポイント
                    </p>
                  </div>
                </v-col>
              </v-row>
              <v-row style="margin: 3%">
                <v-col cols="4">
                  <v-img src="@/assets/ranking03.png"></v-img>
                </v-col>
                <v-col cols="8">
                  <div v-if="!loading">
                    <p>
                      <a :href="top3[2].link" target="_blank">
                        {{ top3[2].spot_name }}
                      </a>
                    </p>
                    <p>
                      {{ top3[2].evaluated_score.toFixed(2) }}&emsp;ポイント
                    </p>
                  </div>
                </v-col>
              </v-row>
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
                            thumb-label="true"
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
                            thumb-label="true"
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
                            thumb-label="true"
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
                            thumb-label="true"
                          ></v-slider>
                        </v-row>
                        <v-row>
                          <p>相手と自分、どっちを重視する？</p>
                        </v-row>
                        <v-row>
                          <v-slider
                            v-model="weight"
                            :max="max"
                            :min="min"
                            thumb-label="true"
                          >
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

      loading: true,
      spots: null,
      top3: null,

      neighborsKuchikomis: [],
      virtualNeighborsKuchikomis: [],

      inyou: 50,
      oshare: 50,
      shokuji: 50,
      setsuyaku: 50,
      weight: 50,
      max: 100,
      min: 0,

      searchProgressing: false,
      showResult: false,

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
        this.loading = false;
      });
    },
    fetchSpotList() {
      spot.getList().then(res => {
        this.spots = Object.values(res);
        this.loading = false;
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
    }
  }
};
</script>

<style></style>
