<template>
  <v-card>
    <v-form v-model="valid">
      <v-text-field v-model="username" :rules="userNameRules" label="ユーザー名" required></v-text-field>
      <v-text-field v-model="email" :rules="emailRules" label="メールアドレス" required></v-text-field>
      <v-text-field
        v-model="password"
        :append-icon="show ? 'visibility' : 'visibility_off'"
        :type="show ? 'text' : 'password'"
        :rules="passwordRules"
        label="パスワード"
        required
        @click:append="show = !show"
      ></v-text-field>
      <v-btn color="error" :disabled="!valid" class="mr-4" @click="handleClick">SIGN UP</v-btn>
    </v-form>
  </v-card>
</template>

<script>
const REGEX_EMAIL = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
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
      valid: false,
      username: "",
      userNameRules: [v => !!v || "ユーザー名を入力してください。"],
      email: "",
      emailRules: [
        v => !!v || "メールアドレスを入力してください。",
        v =>
          /.+@.+\..+/.test(v) ||
          "メールアドレスを正しい形式で入力してください。"
      ],
      password: "",
      passwordRules: [
        v => !!v || "パスワードを入力してください。",
        v =>
          (v && v.length >= 5) ||
          "パスワードは5文字以上20文字以内で入力してください。",
        v =>
          (v && v.length <= 20) ||
          "パスワードは5文字以上20文字以内で入力してください。"
      ],
      progress: false,
      error: "",
      show: false
    };
  },

  methods: {
    resetError() {
      this.error = "";
    },

    handleClick(event) {
      if (this.disableLoginAction) {
        return;
      }

      this.progress = true;
      this.error = "";

      this.$nextTick(() => {
        this.onregister({
          username: this.username,
          email: this.email,
          password: this.password
        })
          .catch(err => {
            this.error = err.message;
          })
          .then(() => {
            this.progress = false;
            this.$emit("close");
            this.username = null;
            this.email = null;
            this.password = null;
          });
      });
    }
  }
};
</script>

<style scoped></style>
