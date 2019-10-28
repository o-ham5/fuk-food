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
      <v-row id="content1" class>
        <v-btn outlined class="mr-3" :to="{ name: 'home' }">はじめる</v-btn>

        <div style="width: 100%; height: 1000px;">ここからコンテンツ１</div>
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
      this.content1 = document.getElementById("content1");
      this.content2 = document.getElementById("content2");

      this.c1_flag =
        window.innerHeight * (3 / 5) >
        this.content1.getBoundingClientRect().top;
      this.c2_flag =
        window.innerHeight * (3 / 5) >
        this.content2.getBoundingClientRect().top;

      if (this.c1_flag && !this.c2_flag) {
        document.getElementById("main-wrapper").style.backgroundColor = "black";
        document.getElementById("main-wrapper").style.color = "white";
      } else {
        document.getElementById("main-wrapper").style.backgroundColor =
          "#FAFAFA";
        document.getElementById("main-wrapper").style.color = "black";
      }
    }
  }
};
</script>

<style scoped>
#mainVisual {
  background: linear-gradient(to top, lightskyblue, #fff);
}
</style>
