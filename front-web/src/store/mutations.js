import * as types from "./mutation-types";

export default {
  [types.AUTH_LOGIN](state, payload) {
    state.auth = payload;
  },
  [types.AUTH_LOGOUT](state) {
    state.auth = {
      token: null
    };
    state.user = {
      account_id: null,
      username: null,
      email: null
    };
  },
  [types.USER_INFO](state, payload) {
    state.user = payload;
  }
};
