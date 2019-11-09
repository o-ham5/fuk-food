<template>
  <v-card>
    <v-container>
      <v-row>
        <v-col>
          <v-form v-model="valid">
            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="Email"
              required
            ></v-text-field>
            <v-text-field
              v-model="password"
              :append-icon="show ? 'visibility' : 'visibility_off'"
              :type="show ? 'text' : 'password'"
              :rules="passwordRules"
              label="Password"
              required
              @click:append="show = !show"
            ></v-text-field>
            <p v-if="error" style="color: #F44336">{{ this.error }}</p>
            <v-btn
              color="error"
              :disabled="!valid"
              class="mr-4"
              @click="handleClick"
              >SIGN IN</v-btn
            >
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import store from "@/store";
const required = val => !!val.trim();

export default {
  name: "SignInForm",

  components: {},

  props: {
    onlogin: {
      type: Function,
      required: true
    }
  },

  data() {
    return {
      valid: false,
      email: "",
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
          "パスワードは5文字以上30文字以内で入力してください。"
        // v =>
        //   (v &&
        //     /^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]{8,100}$/.test(v)) ||
        //   "パスワードには半角小文字大文字数字をそれぞれ１種類以上含めてください。"
      ],
      progress: false,
      error: null,
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
      this.error = null;

      this.$nextTick(() => {
        this.onlogin({ email: this.email, password: this.password })
          .catch(err => {
            this.error = err;
          })
          .then(() => {
            this.progress = false;
            if (store.state.auth.token) this.$emit("close");
          });
      });
    }
  }
};
</script>

<style scoped></style>
