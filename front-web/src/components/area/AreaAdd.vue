<template>
  <v-container>
    <v-btn outlined class="mr-3" @click.stop="add = true">追加する</v-btn>
    <!-- sign up dialog -->
    <v-dialog v-model="add" max-width="400">
      <v-card>
        <v-form v-model="authorized">
          <v-text-field
            v-model="area_name"
            label="エリア名"
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
import { Area } from "@/api";
import store from "@/store";

export default {
  name: "AreaAdd",

  components: {},

  data() {
    return {
      add: false,
      area_name: null
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
        area_name: this.area_name
      };
      return Area.register(registerInfo)
        .then(({ area_id, area_name }) => {
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
