import Vue from "vue";
import Vuex from "vuex";
import actions from "@/store/actions";
import getters from "@/store/getters";
import mutations from "@/store/mutations";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

const state = {
  auth: {
    token: null
  },
  user: {
    account_id: null,
    username: null,
    email: null,
    bias: null,
    variance: null,
    inyou: null,
    oshare: null,
    shokuji: null,
    setsuyaku: null
  }
};
export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations,
  strict: process.env.NODE_ENV !== "production",
  // ブラウザのlocalStrageにセッション情報を保存する
  plugins: [
    createPersistedState({
      key: "fuk-food"
    })
  ]
});
