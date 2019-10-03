import axiosBase from "axios";

const axios = axiosBase.create({
  baseURL: process.env.VUE_APP_API_ORIGIN, // バックエンドB のURL:port を指定する
  headers: {
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest"
  },
  responseType: "json"
});

export default axios;
