<template>
  <nav>
    <v-app-bar
      flat
      fixed
      app
      inverted-scroll
      scroll-threshold="500"
      color="transparent"
    >
      <v-toolbar-title class="text-uppercase grey--text">
        <span class="font-weight-light">FUK</span>
        <span>food</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        v-if="!authorized"
        outlined
        class="mr-3"
        @click.stop="signup = true"
        >Sign UP</v-btn
      >
      <v-btn
        v-if="!authorized"
        outlined
        class="mr-3"
        @click.stop="signin = true"
        >Sign IN</v-btn
      >

      <span v-if="authorized" style="margin-right:1%"
        >{{ this.username }}&nbsp;&nbsp;様</span
      >

      <v-btn v-if="authorized" icon @click.stop="userinfo = true">
        <v-icon>mdi-account</v-icon>
      </v-btn>

      <!-- sign up dialog -->
      <v-dialog v-model="signup" max-width="400">
        <SignUpForm :onregister="handleSignUp" @close="closeSignUp" />
      </v-dialog>
      <!-- sign in dialog -->
      <v-dialog v-model="signin" max-width="500">
        <SignInForm :onlogin="handleSignIn" @close="closeSignIn" />
      </v-dialog>
      <!-- user infomaton dialog -->
      <v-dialog v-model="userinfo" max-width="500">
        <v-card>
          <v-container>
            <v-row>
              <v-col>
                <v-btn outlined class="mr-3" @click="handleSignOut"
                  >Sign OUT</v-btn
                >
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-dialog>
    </v-app-bar>
  </nav>
</template>

<script>
import SignInForm from "@/components/SignInForm";
import SignUpForm from "@/components/SignUpForm";
import { Auth } from "../api";
import store from "../store";

export default {
  name: "Navbar",

  components: {
    SignInForm,
    SignUpForm
  },

  data() {
    return {
      signup: false,
      signin: false,
      userinfo: false
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
          // router.pushで異なるurlに遷移できる。
          //   this.$router.push({ name: "tracker_list" });
        })
        .catch(err => this.throwReject(err));
    },
    handleSignOut() {
      return this.$store
        .dispatch("logout")
        .then(() => {
          this.userinfo = false;
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

    throwReject(err) {
      return Promise.reject(err);
    },
    closeSignIn() {
      this.signin = false;
    },
    closeSignUp() {
      this.signup = false;
    }
  }
};
</script>
