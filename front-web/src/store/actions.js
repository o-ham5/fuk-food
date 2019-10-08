/* eslint-disable no-unused-vars */
import * as types from "./mutation-types";
import { Auth } from "../api";
/* eslint-enable no-unused-vars */

export default {
  login: ({ commit }, authInfo) => {
    return Auth.login(authInfo)
      .then(({ token }) => {
        commit(types.AUTH_LOGIN, { token });
        Auth.getUserInfo(token)
          .then(({ account_id, username, email }) => {
            commit(types.USER_INFO, { account_id, username, email });
          })
          .catch(err => {
            throw err;
          });
      })
      .catch(err => {
        throw err;
      });
  },
  logout: ({ commit }) => {
    commit(types.AUTH_LOGOUT);
  }
};
