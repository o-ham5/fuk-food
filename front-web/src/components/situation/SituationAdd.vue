<template>
  <v-container>
    <v-btn outlined class="mr-3" @click.stop="add = true">追加する</v-btn>
    <!-- sign up dialog -->
    <v-dialog v-model="add" max-width="400">
      <v-card>
        <v-form v-model="authorized">
          <v-text-field
            v-model="situation_name"
            label="シチュエーション名"
            required
          ></v-text-field>
          <v-btn
            color="error"
            :disabled="!authorized"
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
import { Situation } from "@/api";
import store from "@/store";

export default {
  name: "SituationAdd",

  components: {},

  data() {
    return {
      add: false,
      situation_name: null
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
        situation_name: this.situation_name
      };
      return Situation.register(registerInfo)
        .then(({ situation_id, situation_name }) => {
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
