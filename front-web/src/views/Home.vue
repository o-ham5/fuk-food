<template>
  <v-container fluid>
    <v-row id="mainVisual">
      <div id="fukuoka">
        <img
          id="prefecture"
          class="fuk-parts"
          src="../assets/fukuoka.png"
          alt="福岡県"
        />
        <img id="logo" class src="../assets/fukfood-logo.png" alt="fuk-food" />
        <div id="parts">
          <img
            id="ramen"
            class="fuk-parts"
            src="../assets/ramen2.png"
            alt="ラーメン"
          />
          <img
            id="mentaiko"
            class="fuk-parts"
            src="../assets/mentaiko2.png"
            alt="明太子"
          />
          <img
            id="otya"
            class="fuk-parts"
            src="../assets/otya2.png"
            alt="お茶"
          />
          <img
            id="kaki"
            class="fuk-parts"
            src="../assets/kaki2.png"
            alt="牡蠣"
          />
          <img
            id="yakikare"
            class="fuk-parts"
            src="../assets/yakikare2.png"
            alt="焼きカレー"
          />
        </div>
      </div>
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
    <v-row>
      <div style="width: 100%; height: 1000px;"></div>
    </v-row>
  </v-container>
</template>

<script>
import store from "@/store";
import mojs from "mo-js";

export default {
  name: "Home",

  components: {},
  data() {
    return {
      message: null,
      OPTS: {
        scale: { 0: 1 },
        duration: 300,
        y: { 50: -20 },
        easing: "sin.inout"
      },
      OPTS_THEN: {
        duration: 100,
        y: 0
      },
      ramen: undefined,
      mentaiko: undefined,
      otya: undefined,
      kaki: undefined,
      yakikare: undefined,
      logo: undefined,
      timeline: undefined
    };
  },
  computed: {
    authorized: function() {
      return (
        store.state.auth.token !== null && store.state.auth.token !== undefined
      );
    }
  },
  mounted() {
    this.ramen = new mojs.Html({
      el: "#ramen",
      ...this.OPTS,
      delay: 700
    }).then({
      ...this.OPTS_THEN
    });
    this.mentaiko = new mojs.Html({
      el: "#mentaiko",
      ...this.OPTS,
      delay: 500
    }).then({
      ...this.OPTS_THEN
    });
    this.otya = new mojs.Html({
      el: "#otya",
      ...this.OPTS,
      delay: 900
    }).then({
      ...this.OPTS_THEN
    });
    this.kaki = new mojs.Html({
      el: "#kaki",
      ...this.OPTS,
      delay: 1100
    }).then({
      ...this.OPTS_THEN
    });
    this.yakikare = new mojs.Html({
      el: "#yakikare",
      ...this.OPTS,
      delay: 1300
    }).then({
      ...this.OPTS_THEN
    });
    this.logo = new mojs.Html({
      el: "#logo",
      scale: { 10: 1 },
      opacity: { 0: 1 },
      duration: 1000,
      easing: "sin.inout",
      delay: 1500
    });
    this.timeline = new mojs.Timeline({
      delay: 500,
      onComplete() {
        // this.replay();
      }
    });
    this.timeline.add(
      this.ramen,
      this.mentaiko,
      this.otya,
      this.kaki,
      this.yakikare,
      this.logo
    );
    this.timeline.play();
  },
  methods: {
    toKuchikomi() {
      if (this.authorized) {
        this.$router.push({ name: "kuchikomi" });
      } else {
        this.message = "サインインしてください！";
      }
    }
  }
};
</script>

<style>
#mainVisual {
  background: linear-gradient(to top, lightskyblue, #fff);
}
#fukuoka {
  position: relative;
  width: 640px;
  height: 640px;
  margin: 0 auto;
}
.fuk-parts {
  position: absolute;
}
#prefecture {
  width: 100%;
  height: 100%;
}

#logo {
  display: block;
  margin: auto;
  padding-top: 5%;
}

#ramen {
  top: 60%;
  left: 40%;
  z-index: 2;
}

#mentaiko {
  top: 53%;
  left: 46%;
  z-index: 1;
}

#otya {
  top: 65%;
  left: 55%;
}

#kaki {
  top: 52%;
  left: 15%;
}

#yakikare {
  top: 45%;
  left: 60%;
}
</style>
