<template>
  <v-container>
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
  </v-container>
</template>

<script>
import store from "@/store";

export default {
  name: "Home",

  components: {},
  data() {
    return {
      message: null
    };
  },
  computed: {
    authorized: function() {
      return (
        store.state.auth.token !== null && store.state.auth.token !== undefined
      );
    }
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
