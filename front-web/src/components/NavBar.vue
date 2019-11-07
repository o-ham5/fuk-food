<template>
  <nav id="nav-wrapper">
    <v-app-bar
      flat
      fixed
      app
      :inverted-scroll="invertedScroll"
      :scroll-threshold="scrollThreshold"
      :color="color"
    >
      <v-toolbar-title class="text-uppercase grey--text">
        <span class="font-weight-light">FUK</span>
        <span>food</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn v-if="!authorized" outlined class="mr-3" @click.stop="signup = true">Sign UP</v-btn>
      <v-btn v-if="!authorized" outlined class="mr-3" @click.stop="signin = true">Sign IN</v-btn>

      <span v-if="authorized" style="margin-right:1%">{{ this.username }}&nbsp;&nbsp;様</span>

      <v-btn v-if="authorized" icon @click.stop="accountInfo = true">
        <v-icon>mdi-account</v-icon>
      </v-btn>

      <!-- sign up dialog -->
      <v-dialog v-model="signup" max-width="700">
        <SignUpForm :onregister="handleSignUp" @close="closeSignUp" />
      </v-dialog>
      <!-- sign in dialog -->
      <v-dialog v-model="signin" max-width="500">
        <SignInForm :onlogin="handleSignIn" @close="closeSignIn" />
      </v-dialog>
      <!-- user infomaton dialog -->
      <v-dialog v-model="accountInfo" max-width="500">
        <AccountInfo
          :on-sign-out-click="handleSignOut"
          :on-update-click="handleAccountInfoUpdate"
          @close="closeAccountInfo"
        />
      </v-dialog>
    </v-app-bar>
  </nav>
</template>

<script>
import SignInForm from "@/components/SignInForm";
import SignUpForm from "@/components/SignUpForm";
import AccountInfo from "@/components/AccountInfo";
import { Auth } from "../api";
import store from "../store";

export default {
  name: "Navbar",

  components: {
    SignInForm,
    SignUpForm,
    AccountInfo
  },

  props: {
    invertedScroll: {
      type: Boolean,
      default: false
    },
    scrollThreshold: {
      type: Number,
      required: false,
      default: 0
    },
    color: {
      type: String,
      required: false,
      default: "transparent"
    }
  },

  data() {
    return {
      signup: false,
      signin: false,
      accountInfo: false
    };
  },
  computed: {
    authorized: function() {
      return (
        store.state.auth.token !== null && store.state.auth.token !== undefined
      );
    },
    username: function() {
      return store.state.user.username;
    }
  },

  methods: {
    handleSignIn(authInfo) {
      return this.$store
        .dispatch("login", authInfo)
        .then(() => {
          this.$router.push({ name: "home" });
        })
        .catch(err => this.throwReject(err));
    },
    handleSignUp(registerInfo) {
      return Auth.register(registerInfo)
        .then(({ username, email }) => {
          console.log(username);
          let authInfo = {
            email: registerInfo.email,
            password: registerInfo.password
          };
          this.handleSignIn(authInfo);
        })
        .catch(err => this.throwReject(err));
    },
    handleSignOut() {
      return this.$store
        .dispatch("logout")
        .then(() => {
          this.$router.push({ name: "top" });
        })
        .catch(err => this.throwReject(err));
    },
    handleAccountInfoUpdate(token, updateAccountInfo) {
      return Auth.update(token, updateAccountInfo)
        .then(({ result }) => {
          console.log(result);
        })
        .catch(err => this.throwReject(err));
    },

    throwReject(err) {
      return Promise.reject(err);
    },
    closeSignIn() {
      this.signin = false;
    },
    closeSignUp() {
      this.signup = false;
    },
    closeAccountInfo() {
      this.accountInfo = false;
    }
  }
};
</script>
