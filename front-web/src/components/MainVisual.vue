<template>
  <div id="fukuoka">
    <img
      id="prefecture"
      class="fuk-parts"
      src="../assets/fukuoka.png"
      alt="福岡県"
    />
    <img id="logo" class src="../assets/Fuk-Food2.svg" alt="fuk-food" width="100%" />
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
      <img id="otya" class="fuk-parts" src="../assets/otya2.png" alt="お茶" />
      <img id="kaki" class="fuk-parts" src="../assets/kaki2.png" alt="牡蠣" />
      <img
        id="yakikare"
        class="fuk-parts"
        src="../assets/yakikare2.png"
        alt="焼きカレー"
      />
    </div>
  </div>
</template>

<script>
import mojs from "mo-js";

export default {
  name: "MainVisual",

  data() {
    return {
    };
  },
  mounted() {
    const OPTS = {
      scale: { 0: 1 },
      duration: 300,
      y: { 50: -20 },
      easing: "sin.inout"
    };
    const OPTS_THEN = {
      duration: 100,
      y: 0
    };
    const ramen = new mojs.Html({
      el: "#ramen",
      ...OPTS,
      delay: 700
    }).then({
      ...OPTS_THEN
    });
    const mentaiko = new mojs.Html({
      el: "#mentaiko",
      ...OPTS,
      delay: 500
    }).then({
      ...OPTS_THEN
    });
    const otya = new mojs.Html({
      el: "#otya",
      ...OPTS,
      delay: 900
    }).then({
      ...OPTS_THEN
    });
    const kaki = new mojs.Html({
      el: "#kaki",
      ...OPTS,
      delay: 1100
    }).then({
      ...OPTS_THEN
    });
    const yakikare = new mojs.Html({
      el: "#yakikare",
      ...OPTS,
      delay: 1300
    }).then({
      ...OPTS_THEN
    });
    const logo = new mojs.Html({
      el: "#logo",
      scale: { 10: 1 },
      opacity: { 0: 1 },
      duration: 1000,
      easing: "sin.inout",
      delay: 1500
    });

    var _this = this;

    const timeline = new mojs.Timeline({
      delay: 500,
      onComplete() {
        _this.$emit('bottom-bar');
      }
    });
    timeline.add(
      ramen,
      mentaiko,
      otya,
      kaki,
      yakikare,
      logo
    );
    timeline.play();
  }
};
</script>

<style>
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
  position: relative;
  top: 15%;
  z-index: 10;
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
