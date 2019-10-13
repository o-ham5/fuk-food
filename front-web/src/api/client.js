import axiosBase from "axios";
import store from "@/store";

// const token = store !== undefined ? store.state.auth.token : null;
const axios = axiosBase.create({
  baseURL: process.env.VUE_APP_API_ORIGIN, // バックエンドB のURL:port を指定する
  headers: {
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest"
    // Authorization: "JWT " + token
  },
  responseType: "json"
});

export default axios;
