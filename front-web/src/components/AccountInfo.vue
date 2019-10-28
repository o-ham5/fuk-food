<template>
  <!-- ユーザの性格入力のページ -->
  <v-card style="height:100%">
    <div style="margin-left:3%">
      <v-container>
        <v-row>
          <v-col cols="5">
            <v-row justify="center" style="margin-top:3%">
              <v-avatar>
                <v-icon size="60">mdi-account-circle</v-icon>
              </v-avatar>
            </v-row>
          </v-col>
          <v-col cols="7">
            <v-row>
              <p>{{ this.username }}</p>
            </v-row>
            <v-row>
              <p>{{ this.email }}</p>
            </v-row>
          </v-col>
        </v-row>
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
              </v-container>
            </div>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-btn outlined class="mr-3" @click="updateConfirm = true"
              >更新する</v-btn
            >
            <v-btn outlined class="mr-3" @click="signOutConfirm = true"
              >ログアウト</v-btn
            >
          </v-col>
        </v-row>
      </v-container>
      <v-snackbar v-model="updateConfirm" top :timeout="10000">
        アカウント情報を更新します。よろしいですか？
        <v-btn color="pink" text @click="handleUpdateClick">実行</v-btn>
        <v-btn color="pink" text @click="updateConfirm = false"
          >キャンセル</v-btn
        >
      </v-snackbar>
      <v-snackbar v-model="updateComplete" top :timeout="5000"
        >アカウント情報を更新しました。</v-snackbar
      >
      <v-snackbar v-model="signOutConfirm" top :timeout="10000">
        ログアウトします。よろしいですか？
        <v-btn color="pink" text @click="handleSignOutClick">実行</v-btn>
        <v-btn color="pink" text @click="signOutConfirm = false"
          >キャンセル</v-btn
        >
      </v-snackbar>
    </div>
  </v-card>
</template>

<script>
import store from "@/store";

export default {
  name: "AccountInfo",

  components: {},

  props: {
    onSignOutClick: {
      type: Function,
      required: true
    },
    onUpdateClick: {
      type: Function,
      required: true
    }
  },

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

      updateConfirm: false,
      updateComplete: false,
      signOutConfirm: false
    };
  },

  mounted() {
    this.init();
  },

  methods: {
    resetError() {
      this.error = "";
    },
    init() {
      this.username = store.state.user.username;
      this.email = store.state.user.email;
      this.inyou = store.state.user.inyou;
      this.oshare = store.state.user.oshare;
      this.shokuji = store.state.user.shokuji;
      this.setsuyaku = store.state.user.setsuyaku;
    },

    handleSignOutClick() {
      this.$nextTick(() => {
        this.onSignOutClick()
          .catch(err => {
            this.error = err;
          })
          .then(() => {
            this.$emit("close");
            this.inyou = 50;
            this.oshare = 50;
            this.shokuji = 50;
            this.setsuyaku = 50;
          });
      });
    },

    handleUpdateClick() {
      if (this.disableLoginAction) {
        return;
      }
      let updateAccountInfo = {
        inyou: this.inyou,
        oshare: this.oshare,
        shokuji: this.shokuji,
        setsuyaku: this.setsuyaku
      };
      this.$nextTick(() => {
        this.onUpdateClick(store.state.auth.token, updateAccountInfo)
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
