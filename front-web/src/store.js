import Vue from "vue";
import Vuex from "vuex";
import actions from "@/store/actions";
import getters from "@/store/getters";
import mutations from "@/store/mutations";

Vue.use(Vuex);

const state = {
  auth: {
    token: null
  },
  user: {
    username: null,
    email: null
  }
};
export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations,
  strict: process.env.NODE_ENV !== "production"
});
