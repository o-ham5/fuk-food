<template>
  <v-container fluid>
    <v-row id='mainVisual'>
      <MainVisual />
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
    <v-row id='content1' class=''>
      <div style="width: 100%; height: 1000px;">ここからコンテンツ１</div>
    </v-row>
    <hr>
    <v-row id='content2'>
      <div style="width: 100%; height: 1000px;">ここからコンテンツ２</div>
    </v-row>
  </v-container>
</template>

<script>
import store from "@/store";
import MainVisual from "@/components/MainVisual";

export default {
  name: "Home",

  components: {
    MainVisual
  },
  data() {
    return {
      message: null,
      content1: null,
      content2: null,
      c1_flag: false,
      c2_flag: false,
    };
  },
  mounted() {
    window.addEventListener('scroll', this.bg_change);
  },
  methods: {
    toKuchikomi() {
      if (this.authorized) {
        this.$router.push({ name: "kuchikomi" });
      } else {
        this.message = "サインインしてください！";
      }
    },
    bg_change() {

      this.content1 = document.getElementById('content1');
      this.content2 = document.getElementById('content2');

      this.c1_flag = window.innerHeight*(3/5) > this.content1.getBoundingClientRect().top;
      this.c2_flag = window.innerHeight*(3/5) > this.content2.getBoundingClientRect().top;

      if (this.c1_flag && !this.c2_flag) {
        document.getElementById('main-wrapper').style.backgroundColor = 'black';
        document.getElementById('main-wrapper').style.color = 'white';
      }else{
        document.getElementById('main-wrapper').style.backgroundColor = '#FAFAFA'; 
        document.getElementById('main-wrapper').style.color = 'black';
      };
    },
  }
};
</script>

<style>
#mainVisual {
  background: linear-gradient(to top, lightskyblue, #fff);
}
</style>
