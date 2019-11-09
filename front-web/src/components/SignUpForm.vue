<template>
  <v-card>
    <v-carousel
      v-model="model"
      :show-arrows="false"
      :hide-delimiters="false"
      :cycle="false"
    >
      <v-carousel-item v-for="(page, i) in pages" :key="page">
        <!-- ようこそのページ -->
        <v-card v-if="model == 0" style="height:100%">
          <div style="margin-left:3%">
            <v-container>
              <v-row>
                <p>{{ page }}</p>
                <v-spacer></v-spacer>
                <v-btn color="error" class="mr-4" @click="changePage0to1"
                  >次へ</v-btn
                >
              </v-row>
              <v-row>
                <v-col cols="5">
                  <v-img
                    src="@/assets/mimi_sumasu_man.png"
                    style="margin-top: 10%"
                  />
                </v-col>
                <v-col cols="7">
                  <div style="margin-top:20%">
                    <p>ユーザ情報を登録します。</p>
                    <p>FUKネーターの質問に答えてね！</p>
                  </div>
                </v-col>
              </v-row>
            </v-container>
          </div>
        </v-card>

        <!-- アカウント情報入力のページ -->
        <v-card v-if="model == 1" style="height:100%">
          <div style="margin-left:3%">
            <v-container>
              <v-row>
                {{ page }}
                <v-spacer></v-spacer>
                <v-btn
                  color="error"
                  :disabled="
                    !valid || showEmailExistError || showUsernameExistError
                  "
                  class="mr-4"
                  @click="changePage1to2"
                  >次へ</v-btn
                >
              </v-row>
              <v-row>
                <v-col cols="4">
                  <v-img
                    src="@/assets/mimi_sumasu_man.png"
                    style="margin-top: 20%"
                  />
                </v-col>
                <v-col cols="8">
                  <v-form v-model="valid">
                    <v-text-field
                      v-model="username"
                      :rules="userNameRules"
                      label="ユーザー名"
                      required
                      @change="checkUserName"
                    >
                      <template v-slot:append>
                        <v-fade-transition leave-absolute>
                          <v-progress-circular
                            v-if="checkingUsername"
                            size="24"
                            color="info"
                            indeterminate
                          ></v-progress-circular>
                          <v-icon v-if="usernameOk" color="#00E676"
                            >mdi-check-circle</v-icon
                          >
                        </v-fade-transition>
                      </template>
                    </v-text-field>
                    <p
                      v-if="showUsernameExistError"
                      style="font-size: 50%; color: #EF5350"
                    >
                      {{ usernameExistError }}
                    </p>
                    <v-text-field
                      v-model="email"
                      :rules="emailRules"
                      label="メールアドレス"
                      required
                      @change="checkEmail"
                    >
                      <template v-slot:append>
                        <v-fade-transition leave-absolute>
                          <v-progress-circular
                            v-if="checkingEmail"
                            size="24"
                            color="info"
                            indeterminate
                          ></v-progress-circular>
                          <v-icon v-if="emailOk" color="#00E676"
                            >mdi-check-circle</v-icon
                          >
                        </v-fade-transition>
                      </template>
                    </v-text-field>
                    <p
                      v-if="showEmailExistError"
                      style="font-size: 50%; color: #EF5350"
                    >
                      {{ emailExistError }}
                    </p>
                    <v-text-field
                      v-model="password"
                      :append-icon="show ? 'visibility' : 'visibility_off'"
                      :type="show ? 'text' : 'password'"
                      :rules="passwordRules"
                      label="パスワード"
                      required
                      @click:append="show = !show"
                    ></v-text-field>
                    <v-text-field
                      v-model="password_re"
                      :append-icon="show ? 'visibility' : 'visibility_off'"
                      :type="show ? 'text' : 'password'"
                      :rules="passwordReRules"
                      label="パスワード（確認）"
                      required
                      @click:append="show = !show"
                    ></v-text-field>
                  </v-form>
                </v-col>
              </v-row>
            </v-container>
          </div>
        </v-card>

        <!-- ユーザの性格入力のページ -->
        <v-card v-if="model == 2" style="height:100%">
          <div style="margin-left:3%">
            <v-container>
              <v-row>
                <p>{{ page }}</p>
                <v-spacer></v-spacer>
                <v-btn color="error" class="mr-4" @click="changePage2to3"
                  >次へ</v-btn
                >
              </v-row>

              <v-row>
                <v-col cols="4">
                  <v-img
                    src="@/assets/mimi_sumasu_man.png"
                    style="margin-top: 10%"
                  />
                </v-col>
                <v-col cols="8">
                  <div style="margin-top:0%">
                    <v-container>
                      <v-row>
                        <p>陽キャ度は？</p>
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
                        <p>オシャレ度は？</p>
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
            </v-container>
          </div>
        </v-card>

        <!-- サインアップのページ -->
        <v-card v-if="model == 3" style="height:100%">
          <div style="margin-left:3%; margin-right:3%">
            <v-container>
              <v-row>{{ page }}</v-row>
              <v-row>
                <v-col cols="5">
                  <v-img
                    src="@/assets/mimi_sumasu_man.png"
                    style="margin-top: 10%"
                  />
                </v-col>
                <v-col cols="7">
                  <div style="margin-top:20%">
                    <p>入力したメールアドレスに仮登録のメールを送ります。</p>
                    <p>メールのリンクをクリックして登録を完了してください。</p>
                    <v-btn
                      color="error"
                      :disabled="!valid"
                      class="mr-4"
                      @click="handleClick"
                      >メールを送る</v-btn
                    >
                  </div>
                </v-col>
              </v-row>
            </v-container>
          </div>
        </v-card>
      </v-carousel-item>
    </v-carousel>
  </v-card>
</template>

<script>
import auth from "../api/auth";
const required = val => !!val.trim();

export default {
  name: "SignUpForm",

  components: {},

  props: {
    onregister: {
      type: Function,
      required: true
    }
  },

  data() {
    return {
      model: 0,
      pages: [
        "ようこそ！",
        "基本情報を教えてね！",
        "あなたの性格を調べるよ！",
        "FUK FOODを楽しんでね！"
      ],
      valid: false,
      username: "",
      checkingUsername: false,
      usernameOk: false,
      userNameRules: [
        v => !!v || "ユーザー名を入力してください。",
        v =>
          /^[a-zA-Z0-9_\-.]{3,15}$/.test(v) ||
          "ユーザ名は３文字以上15文字以内の英数字で入力してください。"
      ],
      email: "",
      checkingEmail: false,
      emailOk: false,
      emailRules: [
        v => !!v || "メールアドレスを入力してください。",
        v =>
          /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(
            v
          ) || "メールアドレスを正しい形式で入力してください。"
      ],
      password: "",
      passwordRules: [
        v => !!v || "パスワードを入力してください。",
        v =>
          (v && v.length >= 5) ||
          "パスワードは5文字以上20文字以内で入力してください。",
        v =>
          (v && v.length <= 30) ||
          "パスワードは5文字以上30文字以内で入力してください。",
        v =>
          (v &&
            /^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]{8,100}$/.test(v)) ||
          "パスワードには半角小文字大文字数字をそれぞれ１種類以上含めてください。"
      ],
      password_re: "",
      passwordReRules: [
        v => !!v || "パスワードを入力してください。",
        v => this.password == v || "パスワードが一致しません"
      ],
      progress: false,
      showError: false,
      error: null,
      show: false,

      inyou: 50,
      oshare: 50,
      shokuji: 50,
      setsuyaku: 50,
      min: 0,
      max: 100,

      usernameExistError: null,
      showUsernameExistError: false,
      emailExistError: null,
      showEmailExistError: false
    };
  },

  mounted() {
    this.model = 0;
  },

  methods: {
    resetError() {
      this.error = "";
    },

    handleClick() {
      if (this.disableLoginAction) {
        return;
      }

      this.progress = true;
      this.error = null;

      this.$nextTick(() => {
        this.onregister({
          username: this.username,
          email: this.email,
          password: this.password,
          inyou: this.inyou,
          oshare: this.oshare,
          shokuji: this.shokuji,
          setsuyaku: this.setsuyaku
        })
          .catch(err => {
            this.error = "入力されたユーザ情報で登録できませんでした。";
          })
          .then(() => {
            this.progress = false;
            this.$emit("close");
            this.username = null;
            this.email = null;
            this.password = null;
            this.inyou = 50;
            this.oshare = 50;
            this.shokuji = 50;
            this.setsuyaku = 50;
            this.model = 0;
          });
      });
    },
    changePage0to1() {
      this.model = 1;
    },
    changePage1to2() {
      this.model = 2;
    },
    changePage2to3() {
      this.model = 3;
    },
    checkUserName() {
      this.checkingUsername = true;
      if (this.username != null) {
        return auth
          .checkUserName({
            username: this.username
          })
          .then(({ res }) => {
            this.checkingUsername = false;
            if (!res.exist) {
              this.showUsernameExistError = false;
              this.usernameOk = true;
            } else {
              this.usernameOk = false;
              this.usernameExistError =
                "入力されたユーザー名はすでに登録されています。";
              this.showUsernameExistError = true;
            }
          })
          .catch(err => this.throwReject(err));
      }
    },
    checkEmail() {
      this.checkingEmail = true;
      if (this.email != null) {
        return auth
          .checkEmail({
            email: this.email
          })
          .then(({ res }) => {
            this.checkingEmail = false;
            if (!res.exist) {
              this.emailOk = true;
              this.showEmailExistError = false;
            } else {
              this.emailOk = false;
              this.emailExistError =
                "入力されたメールアドレスはすでに登録されています。";
              this.showEmailExistError = true;
            }
          })
          .catch(err => this.throwReject(err));
      }
    }
  }
};
</script>

<style scoped></style>
