<template>
  <div id="top-wrapper">
    <NavBar
      :inverted-scroll="invertedScroll"
      :scroll-threshold="scrollThreshold"
      :color="color"
    />
    <PreScreen v-if="!display" @set="Setflag"></PreScreen>
    <v-container id="main-wrapper" v-if="display" fluid class="mb-12">
      <BottomBar v-if="bottomBarFlag" />
      <v-row id="mainVisual">
        <MainVisual @bottom-bar="SetBottom" />
        <div class="dark-mask"></div>
      </v-row>
      <v-row id="ramenVisual">
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
      <v-row id="contents">
        <div class='text-title'>
          <TextContents v-if="contentsFlag" />
          <img class="meido" src="../assets/meido.png" width="20%">
        </div>
        <div>
          <p class="section-sentence contents-item" :class="{show:contents_item[0], hidden:!contents_item[0]}">
            あいうえお
          </p>
          <div class="contents-item" :class="{show:contents_item[1], hidden:!contents_item[1]}">
            <v-container fluid>
              <v-row>
                <v-col cols=12 md=6>
                  <h4>自分に似たユーザーのオススメ店をpick up！</h4>
                  <p class="mt-12">
                    独自の分析法であなたの好みや性格と似ているユーザーを調査し，その人がよく行くお店を紹介します。<br>
                    登録ユーザー同士で美味しいお店を共有しちゃいましょう！
                  </p>
                </v-col>
                <v-col cols=12 md=6>
                  <img src="../assets/gureko1.png" width=100%>
                </v-col>
              </v-row>
            </v-container>
          </div>
          <div class="contents-item" :class="{show:contents_item[2], hidden:!contents_item[2]}">
            <v-container fluid >
              <v-row>
                <v-col cols=12 md=6 order-md="2">
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
                <v-col cols=12 md=6 order-md="1">
                  <img src="../assets/gureko2.png" width=100%>
                </v-col>
              </v-row>
            </v-container>
          </div>
          <div class="contents-item" :class="{show:contents_item[3], hidden:!contents_item[3]}">
            <v-container fluid>
              <v-row>
                <v-col cols=12 md=6>
                  <h4>お店の真の魅力をランキング！</h4>
                  <p class="mt-12">
                    ユーザの評価に対する信頼度などを独自の最先端手法で分析し，ランキング形式でご紹介。<br>
                    検索対象を絞れるので，お好きな条件で１位のお店を調べてみよう！
                  </p>
                </v-col>
                <v-col cols=12 md=6>
                  <img src="../assets/gureko3.png" width=100%>
                </v-col>
              </v-row>
            </v-container>
          </div>
        </div>
      </v-row>
      <v-row id="about-us">
        <div class='text-title'>
          <TextAboutUs v-if="aboutusFlag" />
          <img class="meido" src="../assets/meido.png" width="20%">
        </div>
        <p class="section-sentence au-item" :class="{show:au_item[0], hidden:!au_item[0]}">数学を愛し・数学に愛された者たちの紹介です。</p>
        <v-container fluid class="container-w90" id="au-items">
          <v-row>
            <v-col cols=12 md=6 class="au-item" :class="{show:au_item[1], hidden:!au_item[1]}">
              <v-container>
                <v-row>
                  <v-col cols=3>
                    <div class="au-img-container">
                      <img class="au-img" src="../assets/red.png" width="100%">
                    </div>
                  </v-col>
                  <v-col cols=9>
                    <p><span class="au-nickname">ワタナベ</span><br>
                    <span class="au-position">PM & バックエンド構築</span><br>
                    <span class="au-language">language: Python, Java, Javascript, HTML, CSS</span><br>
                    <span class="au-library">library: Pytorch, Django, Flask, SpringBoot, Vue.js</span><br>
                    <span class="au-tool">tool: Docker, Kubernetes, MySQL, MongoDB</span></p>
                    <p class="au-message">研究室では深層学習を使った画像処理の研究をやっています。好きなサイトは食べログです！食べログのようなみんなに愛されるようなサイトにしたいと思い頑張りました！</p>
                  </v-col>
                </v-row>
              </v-container>
            </v-col>
            <v-col cols=12 md=6 class="au-item" :class="{show:au_item[2], hidden:!au_item[2]}">
              <v-container fluid>
                <v-row>
                  <v-col cols=3>
                    <div class="au-img-container">
                      <img class="au-img" src="../assets/ham.jpeg" width="100%">
                    </div>
                  </v-col>
                  <v-col cols=9>
                    <p><span class="au-nickname">はむ</span><br>
                    <span class="au-position">Webデザイナー & FE</span><br>
                    <span class="au-language">language: Python, HTML, CSS, Javascript</span><br>
                    <span class="au-library">library: jQuery, Vue.js, mo.js, Django, OpenCV</span><br>
                    <span class="au-tool">tool: Photoshop, GIMP, WordPress</span></p>
                    <p class="au-message">画像処理や量子コンピュータの研究を行なっています。将来の夢はフロントエンドエンジニア兼喫茶店開業することです。ウェブデザイン技能検定２級。</p>
                  </v-col>
                </v-row>
              </v-container>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols=12 md=6 class="au-item" :class="{show:au_item[3], hidden:!au_item[3]}">
              <v-container>
                <v-row>
                  <v-col cols=3>
                    <div class="au-img-container">
                      <img class="au-img" src="../assets/red.png" width="100%">
                    </div>
                  </v-col>
                  <v-col cols=9>
                    <p><span class="au-nickname">なりちゃん</span><br>
                    <span class="au-position">AD (Algorithm Designer)</span><br>
                    <span class="au-language">language: Python, C++, MATLAB</span><br>
                    <span class="au-library">library: PuLP, Pytorch, Networkx, sk-learn</span><br>
                    <span class="au-tool">tool: MATLAB, SCIP, CBC, GUROBI</span></p>
                    <p class="au-message">最適化理論の社会実装を主に研究しています。 MAPP(matching app)に感銘を受け, レイティングアルゴリズムに興味を持ちました. 最近彼女ができて, 毎日がハピハピハッピーディです。</p>
                  </v-col>
                </v-row>
              </v-container>
            </v-col>
            <v-col cols=12 md=6 class="au-item" :class="{show:au_item[4], hidden:!au_item[4]}">
              <v-container fluid>
                <v-row>
                  <v-col cols=3>
                    <div class="au-img-container">
                      <img class="au-img" src="../assets/aki.jpeg" width="100%">
                    </div>
                  </v-col>
                  <v-col cols=9>
                    <p><span class="au-nickname">あき</span><br>
                    <span class="au-position">UX Designer</span><br>
                    <span class="au-language">language: Python, C++, HTML, CSS</span><br>
                    <span class="au-library">library: PyTorch, NetworkX</span><br>
                    <span class="au-tool">tool: GUROBI</span></p>
                    <p class="au-message">バイクシェアリングサービスの最適化の研究をしています。日本ビール検定２級。</p>
                  </v-col>
                </v-row>
              </v-container>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols=12 md=6 class="au-item" :class="{show:au_item[5], hidden:!au_item[5]}">
              <v-container>
                <v-row>
                  <v-col cols=3>
                    <div class="au-img-container">
                      <img class="au-img" src="../assets/nopi.jpeg" width="100%">
                    </div>
                  </v-col>
                  <v-col cols=9>
                    <p><span class="au-nickname">のぴー</span><br>
                    <span class="au-position">Illustrator</span><br>
                    <span class="au-language">language: Python (勉強中)</span><br>
                    <span class="au-library">library: </span><br>
                    <span class="au-tool">tool: </span></p>
                    <p class="au-message">最適化か深層学習か研究内容は迷っています。特技はピ○チュウを早く描くことです。ピカ○ュウみたいな愛されキャラを生み出したいです。</p>
                  </v-col>
                </v-row>
              </v-container>
            </v-col>
          </v-row>
        </v-container>
      </v-row>
      <v-row id="next-release">
        <div class='text-title'>
          <img class="meido" src="../assets/meido.png" width="20%">
          <TextNextRelease v-if="nextreleaseFlag" />
        </div>
        <p class="section-sentence nr-item" :class="{show:nr_item[0], hidden:!nr_item[0]}">
          行動範囲や予算から，１日の行動プランをご紹介！？ デートプランも！？
        </p>
      </v-row>
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
      contents_item: [false, false, false, false],
      au_item: [false, false, false, false, false, false],
      nr_item: [false],
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
    this.NoScroll();
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
      var c2_els = document.getElementsByClassName("contents-item");
      var c3_els = document.getElementsByClassName("au-item");
      var c4_els = document.getElementsByClassName("nr-item");

      var c1_flag = window.innerHeight * (3 / 5) > ramenVisual.getBoundingClientRect().top;
      var c2_flag = window.innerHeight * (3 / 5) > contents.getBoundingClientRect().top;
      var c2_items_flag = [];
      for (let i = 0; i < c2_els.length; i++) {
        c2_items_flag[i] = window.innerHeight * (3 / 5) > c2_els[i].getBoundingClientRect().top;
      };
      var c3_items_flag = [];
      for (let i = 0; i < c3_els.length; i++) {
        c3_items_flag[i] = window.innerHeight * (3 / 5) > c3_els[i].getBoundingClientRect().top;
      };
      var c4_items_flag = [];
      for (let i = 0; i < c4_els.length; i++) {
        c4_items_flag[i] = window.innerHeight * (3 / 5) > c4_els[i].getBoundingClientRect().top;
      };

      var c3_flag = window.innerHeight * (3 / 5) > aboutUs.getBoundingClientRect().top;
      var c4_flag = window.innerHeight * (3 / 5) > nextRelease.getBoundingClientRect().top;

      if (c1_flag) {
        top_wrapper.style.backgroundColor = "black";
        top_wrapper.style.color = "#FAFAFA";
        for (let i = 0; i < c1_els.length; i++) {
          c1_els[i].classList.add("c1show");
        };
        for (let i = 0; i < nav_btns.length; i++) {
          nav_btns[i].classList.remove("black--text");
          nav_btns[i].classList.add("white--text");
        };

        if (c2_flag) {
          top_wrapper.style.backgroundColor =
            "#FAFAFA";
          top_wrapper.style.color = "black";
          for (let i = 0; i < nav_btns.length; i++) {
            nav_btns[i].classList.remove("white--text");
            nav_btns[i].classList.add("black--text");
          };
          setTimeout(() => {
              this.contentsFlag = true;
          }, 500);
          for (let i = 0; i < c2_els.length; i++) {
            if(c2_items_flag[i]){
              this.contents_item.splice(i, 1, true);
            };
          };
        };

        if (c3_flag){
          // setTimeout(() => {
              this.aboutusFlag = true;
          // }, 1000);
          for (let i = 0; i < c3_els.length; i++) {
            if(c3_items_flag[i]){
              this.au_item.splice(i, 1, true);
            };
          };

        };
        if (c4_flag){
          // setTimeout(() => {
              this.nextreleaseFlag = true;
          // }, 1000);
          for (let i = 0; i < c4_els.length; i++) {
            if(c4_items_flag[i]){
              this.nr_item.splice(i, 1, true);
            };
          };
        };
      }
    },
    handleTouchMove(e) {
      e.preventDefault();
    },
    NoScroll(){
      //PC用
      var scroll_event = 'onwheel' in document ? 'wheel' : 'onmousewheel' in document ? 'mousewheel' : 'DOMMouseScroll';
      document.addEventListener(scroll_event, this.handleTouchMove, {passive: false});
      //SP用
      document.addEventListener('touchmove.noScroll', this.handleTouchMove, {passive: false});
    },
    ReturnScroll(){
      //PC用
      var scroll_event = 'onwheel' in document ? 'wheel' : 'onmousewheel' in document ? 'mousewheel' : 'DOMMouseScroll';
      document.removeEventListener(scroll_event, this.handleTouchMove, {passive: false});
      //SP用
      document.removeEventListener('.noScroll', this.handleTouchMove, {passive: false});
    },
    Setflag(){
      this.display = true;
      this.ReturnScroll();
    },
    SetBottom(){
      this.bottomBarFlag = true;
    },
  }
};
</script>

<style>

@keyframes show{
  0%{
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

.show{
  animation: show 0.8s;
  animation-fill-mode: both;
}

.hidden{
  opacity: 0;
}

#top-wrapper {
  transition: 0.5s;
}

#main-wrapper > .row{
  margin-bottom: 300px;
}

#mainVisual {
  position: relative;
  background: radial-gradient(#ccc, #000);
}

@keyframes dark_mask_op{
  0%{
    background: rgba(0, 0, 0, 0);
  }
  100%{
    background: rgba(0, 0, 0, 0.3);
  }
}
.dark-mask{
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: 5;
  /* background: rgba(0, 0, 0, 0.3); */
  animation: dark_mask_op 1s 2s;
  animation-fill-mode: both;
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
.c1-part.c1show{
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
  position: relative;
  margin-bottom: 100px;
}
.text-title:before{
  content: "";
  display: block;
  padding-top: 10%;
}

.text-title .meido{
  position: absolute;
  top: 0%;
  left: 10%;
  width: 30%;
}

#next-release .meido{
  position: absolute;
  top: 0%;
  left: 0%;
  width: 30%;
}

@media screen and (min-width: 768px){
  .text-title .meido{
  position: absolute;
  top: 40%;
  left: 24%;
  width: 20%;
}

#next-release .meido{
  position: absolute;
  top: 0%;
  left: 20%;
  width: 20%;
}
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

.section-sentence{
  width: 100%;
  text-align: center;
  font-size: 1.2rem
}

#au-items > .row > .col-12{
  height: 350px;
}

#au-items > .row:nth-child(odd) .col-12:nth-child(even),
#au-items > .row:nth-child(even) .col-12:nth-child(odd){
  background-color: #ffffea;
  border-radius: 240px 100px 100px 100px / 75px 150px 50px 200px;
}

#au-items > .row:nth-child(odd) .col-12:nth-child(odd),
#au-items > .row:nth-child(even) .col-12:nth-child(even){
  background-color: #f5f5f5;
  border-radius: 240px 100px 100px 100px / 75px 150px 50px 200px;
}

.container-w90{
  width: 95%;
}

.au-img-container{
  display: inline-block;
  position: relative;
}

#au-items > .row:nth-child(odd) .col-12:nth-child(even) .au-img-container:after,
#au-items > .row:nth-child(even) .col-12:nth-child(odd) .au-img-container:after{
  position: absolute;
  display: block;
  content: "";
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  /* background: #fff; */
  box-shadow:
  inset 0 0 20px #ffffea,
  inset 0 0 20px #ffffea,
  inset 0 0 20px #ffffea,
  inset 0 0 20px #ffffea,
  inset 0 0 20px #ffffea;
}

#au-items > .row:nth-child(odd) .col-12:nth-child(odd) .au-img-container:after,
#au-items > .row:nth-child(even) .col-12:nth-child(even) .au-img-container:after{
  position: absolute;
  display: block;
  content: "";
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  /* background: #fff; */
  box-shadow:
  inset 0 0 20px #f5f5f5,
  inset 0 0 20px #f5f5f5,
  inset 0 0 20px #f5f5f5,
  inset 0 0 20px #ffffea,
  inset 0 0 20px #f5f5f5;
}

.au-img-container{
  margin-top: 30px;
}

.au-nickname{
  font-weight: bold;
  font-size: 1.2rem;
}

.au-nickname, .au-position{
  display: inline-block;
  width: 100%;
  text-align: center;
}

.au-language, .au-library, .au-tool{
  font-size: 0.8rem;
  color: #555;
}


</style>
