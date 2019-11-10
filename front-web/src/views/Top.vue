<template>
  <div id="top-wrapper">
    <NavBar
      :inverted-scroll="invertedScroll"
      :scroll-threshold="scrollThreshold"
      :color="color"
    />
    <PreScreen v-if="!display" @set="Setflag"></PreScreen>
    <v-container v-if="display" fluid class="mb-12">
      <BottomBar v-if="bottomBarFlag" />
      <v-row id="mainVisual">
        <MainVisual @bottom-bar="SetBottom" />
      </v-row>
      <v-row id="ramenVisual" class="my-8">
        <div style="width: 100%;">
          <img id="ramen_mask" src="../assets/ramen_path.svg" width="80%" />
          <img id="kou" class="c1-part c1-part1" src="../assets/kou.png" width="7%" />
          <img id="huku" class="c1-part c1-part3" src="../assets/huku.png" width="10%" />
          <img id="oka" class="c1-part c1-part1" src="../assets/oka.png" width="7%" />
          <p id="c1_text" class="c1-part c1-part2">
            美味い飯を求める学生達よ，集まれ！
          </p>
        </div>
      </v-row>
      <v-row id="contents" class="my-12">
        <div class='text-title'>
          <TextContents v-if="contentsFlag" />
        </div>
        <div class="contents-item">
          <v-container fluid>
            <v-row>
              <v-col cols=12 md=6>
                <h4>FUKネーターがあなたの好みを当てちゃいます！</h4>
                <p class="mt-12">
                  会員登録をする時，あなたがどんな人なのかをFUKネーターが調査します。<br>
                  質問には嘘偽りなく答えて...ね？
                </p>
              </v-col>
              <v-col cols=10 md=5>
                <img src="../assets/green.png" width=100%>
              </v-col>
              <v-col cols=2 md=1>
              </v-col>  
            </v-row>
          </v-container>
        </div>
        <div class="contents-item">
          <v-container fluid>
            <v-row>
              <v-col cols=12 md=6 order-md="3">
                <h4>自分の好みに似たユーザーのオススメ店をpick up！</h4>
                <p class="mt-12">
                  独自の分析法であなたの好みや性格と似ているユーザーを調査し，その人がよく行くお店を紹介します。<br>
                  登録ユーザー同士で美味しいお店を共有しちゃいましょう！
                </p>
              </v-col>
              <v-col cols=2 md=1 order-md="1">
              </v-col>
              <v-col cols=10 md=5 order-md="2">
                <img src="../assets/blue.png" width=100%>
              </v-col>
            </v-row>
          </v-container>
        </div>
        <div class="contents-item">
          <v-container fluid>
            <v-row>
              <v-col cols=12 md=6>
                <h4>複数人でぴったりのお店をpick up！</h4>
                <p class="mt-12">
                  複数人でご飯に行く場合
                  <ul>
                    <li>好みがバラバラ</li>
                    <li>譲り合って決められない</li>
                  </ul>
                  そんな経験はないですか...？<br>
                  このアプリでは，みなさんの「ちょうどいい」お店を紹介します。
                </p>
              </v-col>
              <v-col cols=10 md=5>
                <img src="../assets/red.png" width=100%>
              </v-col>
              <v-col cols=2 md=1>
              </v-col>  
            </v-row>
          </v-container>
        </div>
      </v-row>
      <v-row id="about-us" class="my-12">
        <div class='text-title'>
          <TextAboutUs v-if="aboutusFlag" />
        </div>
        <div style="width:100%;"></div>
        <p>
          あいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえお
        </p>
      </v-row>
      <v-row id="next-release" class="my-12">
        <div class='text-title'>
          <TextNextRelease v-if="nextreleaseFlag" />
        </div>
        <div style="width:100%;"></div>
        <p>
          行動範囲や予算から，１日の行動プランをご紹介！？ デートプランも！？
        </p>
      </v-row>
      <div style="width:100%;height:1000px;"></div>
    </v-container>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import BottomBar from "@/components/BottomBar";
import store from "@/store";
import MainVisual from "@/components/MainVisual";
import PreScreen from "@/components/PreScreen";
import TextContents from "@/components/TextContents";
import TextAboutUs from "@/components/TextAboutUs";
import TextNextRelease from "@/components/TextNextRelease";

export default {
  name: "Home",

  components: {
    NavBar,
    BottomBar,
    MainVisual,
    PreScreen,
    TextContents,
    TextAboutUs,
    TextNextRelease,
  },
  data() {
    return {
      message: null,

      invertedScroll: true,
      scrollThreshold: 500,
      color: "transparent",
      display: false,
      bottomBarFlag: false,
      // textDivHeight: 0,
      contentsFlag: false,
      aboutusFlag: false,
      nextreleaseFlag: false,
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
      var ramenVisual = document.getElementById("ramenVisual");
      var contents = document.getElementById("contents");
      var aboutUs = document.getElementById("about-us");
      var nextRelease = document.getElementById("next-release");
      var top_wrapper = document.getElementById("top-wrapper");

      var nav_btns = document.querySelectorAll('#nav-wrapper .v-btn');

      var c1_els = document.getElementsByClassName("c1-part");
      var c1_flag = window.innerHeight * (3 / 5) > ramenVisual.getBoundingClientRect().top;
      var c2_flag = window.innerHeight * (3 / 5) > contents.getBoundingClientRect().top;
      var c3_flag = window.innerHeight * (3 / 5) > aboutUs.getBoundingClientRect().top;
      var c4_flag = window.innerHeight * (3 / 5) > nextRelease.getBoundingClientRect().top;

      if (c1_flag) {
        top_wrapper.style.backgroundColor = "black";
        top_wrapper.style.color = "#FAFAFA";
        for (let i = 0; i < c1_els.length; i++) {
          c1_els[i].classList.add("show");
        };
        for (let i = 0; i < nav_btns.length; i++) {
          nav_btns[i].classList.remove("black--text");
          nav_btns[i].classList.add("white--text");
        };

        if (c2_flag) {
          top_wrapper.style.backgroundColor =
            "#FAFAFA";
          top_wrapper.style.color = "black";
          for (let i = 0; i < c1_els.length; i++) {
            c1_els[i].classList.remove("show");
          };
          for (let i = 0; i < nav_btns.length; i++) {
            nav_btns[i].classList.remove("white--text");
            nav_btns[i].classList.add("black--text");
          };
          setTimeout(() => {
              this.contentsFlag = true;
          }, 1000);
        };

        if (c3_flag){
          setTimeout(() => {
              this.aboutusFlag = true;
          }, 1000);
        };
        if (c4_flag){
          setTimeout(() => {
              this.nextreleaseFlag = true;
          }, 1000);
        };
      }
    },
    Setflag(){
      this.display = true;
    },
    SetBottom(){
      this.bottomBarFlag = true;
    },
  }
};
</script>

<style scoped>
#top-wrapper {
  transition: 1s;
}



#mainVisual {
  background: linear-gradient(to top, lightskyblue, #fff);
}
#ramenVisual {
  position: relative;
}
#ramenVisual:before {
  content: "";
  display: block;
  padding-top: 100%;
}
#ramen_mask {
  position: absolute;
  width: 80%;
  left: 10%;
}
.c1-part{
  opacity: 0;
}
.c1-part1{
  transition: 1s 0.5s;
}
.c1-part2{
  transition: 1s 1s;
}
.c1-part3{
  transition: 1.5s 2s;
}
.c1-part.show{
  opacity: 1;
}
#kou{
  position: absolute;
  left: 37%;
  top: 31%;
}
#huku{
  position: absolute;
  left: 45%;
  top: 29.5%;
}
#oka{
  position: absolute;
  left: 46.5%;
  top: 40.5%;
}
#c1_text {
  position: absolute;
  left: 28%;
  top: 55%;
  font-size: 2.2vw;
  color: black;
}

.text-title{
  width: 100%;
}
.text-title:before{
  content: "";
  display: block;
  padding-top: 10%;
}

.content-title{
  margin: 30px auto;
  font-size: 2.5rem;
}

.contents-item .container{
  width: 85%;
}

.contents-item h4{
  font-size: 2rem;
}


</style>
