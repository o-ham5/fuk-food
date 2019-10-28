import client from "./client";

export default {
  register: registerInfo => {
    return new Promise((resolve, reject) => {
      client
        .post("/api/kuchikomi/register/", registerInfo)
        .then(res => resolve(res.data))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  getInfo: kuchikomi_id => {
    return new Promise((resolve, reject) => {
      const url = "/api/kuchikomi/info/" + toString(kuchikomi_id) + "/";
      client
        .get(url)
        .then(res => resolve(res.data))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  getList: () => {
    return new Promise((resolve, reject) => {
      const url = "/api/kuchikomi/list/";
      client
        .get(url)
        .then(res => resolve(res.data))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  getNeighborsList: token => {
    return new Promise((resolve, reject) => {
      const url = "/api/kuchikomi/neighbors/";
      client
        .get(url, {
          headers: { Authorization: "JWT " + token },
          data: {}
        })
        .then(res => resolve(res.data))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  update: (kuchikomi_id, updateInfo) => {
    return new Promise((resolve, reject) => {
      const url = "/api/kuchikomi/update/" + kuchikomi_id + "/";
      client
        .put(url, updateInfo)
        .then(res => resolve(res.data))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  delete: kuchikomi_id => {
    return new Promise((resolve, reject) => {
      const url = "/api/kuchikomi/delete/" + kuchikomi_id + "/";
      client
        .delete(url)
        .then(res => resolve({}))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  }
};
