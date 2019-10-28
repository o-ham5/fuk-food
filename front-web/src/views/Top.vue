<template>
  <div id="main-wrapper">
    <NavBar
      :inverted-scroll="invertedScroll"
      :scroll-threshold="scrollThreshold"
      :color="color"
    />
    <v-container fluid>
      <v-row id="mainVisual">
        <MainVisual />
      </v-row>
      <v-row id="content1" class="my-12">
        <div style="width: 100%;">
          <v-btn outlined class="mr-3" :to="{ name: 'home' }">はじめる</v-btn>
          <p>ここからコンテンツ１</p>
          <img id="ramen_mask" src="../assets/ramen_path.svg" width="80%" />
          <h3 id="c1_text1" class="c1_text">あいうえお。</h3>
          <p id="c1_text2" class="c1_text">
            テキストテキストテキストテキストテキストテキスト
          </p>
        </div>
      </v-row>
      <hr />
      <v-row id="content2">
        <div style="width: 100%; height: 1000px;">ここからコンテンツ２</div>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import store from "@/store";
import MainVisual from "@/components/MainVisual";

export default {
  name: "Home",

  components: {
    NavBar,
    MainVisual
  },
  data() {
    return {
      message: null,
      content1: null,
      content2: null,
      c1_flag: false,
      c2_flag: false,

      invertedScroll: true,
      scrollThreshold: 500,
      color: "transparent"
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
    window.addEventListener("scroll", this.bg_change);
  },
  beforeDestroy: function() {
    window.removeEventListener("scroll", this.bg_change);
  },

  methods: {
    bg_change() {
      var content1 = document.getElementById("content1");
      var content2 = document.getElementById("content2");

      var c1_els = document.getElementsByClassName("c1_text");
      var c1_flag =
        window.innerHeight * (2 / 5) > content1.getBoundingClientRect().top;
      var c2_flag =
        window.innerHeight * (3 / 5) > content2.getBoundingClientRect().top;

      if (c1_flag && !c2_flag) {
        document.getElementById("main-wrapper").style.backgroundColor = "black";
        document.getElementById("main-wrapper").style.color = "#FAFAFA";
        for (let i = 0; i < c1_els.length; i++) {
          c1_els[i].style.color = "black";
        }
      } else {
        document.getElementById("main-wrapper").style.backgroundColor =
          "#FAFAFA";
        document.getElementById("main-wrapper").style.color = "black";
        for (let i = 0; i < c1_els.length; i++) {
          c1_els[i].style.color = "#FAFAFA";
        }
      }
    }
  }
};
</script>

<style scoped>
#mainVisual {
  background: linear-gradient(to top, lightskyblue, #fff);
}
#content1 {
  position: relative;
}
#content1:before {
  content: "";
  display: block;
  padding-top: 100%;
}
#ramen_mask {
  position: absolute;
  width: 80%;
  left: 10%;
}
#c1_text1 {
  position: absolute;
  left: 33%;
  top: 40%;
  color: #fafafa;
  font-size: 5vw;
  transition: color 1s 0.5s;
}
#c1_text2 {
  position: absolute;
  left: 23%;
  top: 55%;
  color: black;
  font-size: 2vw;
  transition: color 1s 1s;
}
</style>
