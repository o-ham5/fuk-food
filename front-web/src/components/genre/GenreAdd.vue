<template>
  <v-container>
    <v-btn outlined class="mr-3" @click.stop="add = true">追加する</v-btn>
    <!-- sign up dialog -->
    <v-dialog v-model="add" max-width="400">
      <v-card>
        <v-form v-model="valid">
          <v-text-field
            v-model="genre_name"
            label="ジャンル名"
            required
          ></v-text-field>
          <v-btn
            color="error"
            :disabled="!valid"
            class="mr-4"
            @click="handleClick"
            >追加する</v-btn
          >
        </v-form>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { Genre } from "@/api";
import store from "@/store";

export default {
  name: "GenreAdd",

  components: {},

  data() {
    return {
      add: false,
      genre_name: null
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
    handleClick() {
      let registerInfo = {
        genre_name: this.genre_name
      };
      return Genre.register(registerInfo)
        .then(({ id, genre_name }) => {
          console.log(genre_name);
          this.closeAdd();
        })
        .catch(err => this.throwReject(err));
    },

    throwReject(err) {
      return Promise.reject(err);
    },
    closeAdd() {
      this.add = false;
    }
  }
};
</script>
