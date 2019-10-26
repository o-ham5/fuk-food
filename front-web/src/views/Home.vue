<template>
  <div style="background-color: #B3E5FC; height: 100%">
    <NavBar :inverted-scroll="invertedScroll" :scroll-threshold="scrollThreshold" :color="color" />
    <v-container>
      <v-row>
        <v-col cols="6">
          <v-card style="height: 100%">
            <v-container>
              <v-row style="margin: 3%">
                <p class="display-2">総合ランキング</p>
              </v-row>
              <v-row>
                <v-col cols="4">
                  <v-img src="@/assets/ranking01.png"></v-img>
                </v-col>
                <v-col cols="8">
                  <div v-if="!loading">
                    <p>{{ top3[0].spot_name }}</p>
                    <p>{{ top3[0].evaluated_score.toFixed(2) }}&emsp;ポイント</p>
                  </div>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="4">
                  <v-img src="@/assets/ranking02.png"></v-img>
                </v-col>
                <v-col cols="8">
                  <div v-if="!loading">
                    <p>{{ top3[1].spot_name }}</p>
                    <p>{{ top3[1].evaluated_score.toFixed(2) }}&emsp;ポイント</p>
                  </div>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="4">
                  <v-img src="@/assets/ranking03.png"></v-img>
                </v-col>
                <v-col cols="8">
                  <div v-if="!loading">
                    <p>{{ top3[2].spot_name }}</p>
                    <p>{{ top3[2].evaluated_score.toFixed(2) }}&emsp;ポイント</p>
                  </div>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-col>

        <v-col cols="6">
          <v-card style="height: 100%">
            <v-container>
              <v-row style="margin: 3%">
                <p class="display-1">あなたと似た人が好きなお店</p>
              </v-row>
              <v-row>
                <v-col cols="4">
                  <v-img src="@/assets/ranking01.png"></v-img>
                </v-col>
                <v-col cols="8">
                  <div v-if="!loading">
                    <p>{{ top3[0].spot_name }}</p>
                    <p>{{ top3[0].evaluated_score.toFixed(2) }}&emsp;ポイント</p>
                  </div>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="4">
                  <v-img src="@/assets/ranking02.png"></v-img>
                </v-col>
                <v-col cols="8">
                  <div v-if="!loading">
                    <p>{{ top3[1].spot_name }}</p>
                    <p>{{ top3[1].evaluated_score.toFixed(2) }}&emsp;ポイント</p>
                  </div>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="4">
                  <v-img src="@/assets/ranking03.png"></v-img>
                </v-col>
                <v-col cols="8">
                  <div v-if="!loading">
                    <p>{{ top3[2].spot_name }}</p>
                    <p>{{ top3[2].evaluated_score.toFixed(2) }}&emsp;ポイント</p>
                  </div>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-col>
      </v-row>
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
      top3: null
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
    }
  }
};
</script>

<style></style>
