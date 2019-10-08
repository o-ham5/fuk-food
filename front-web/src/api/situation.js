import client from "./client";

export default {
  register: registerInfo => {
    return new Promise((resolve, reject) => {
      client
        .post("/api/situation/register/", registerInfo)
        .then(res =>
          resolve({ id: res.data.id, situation_name: res.data.situation_name })
        )
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  getInfo: id => {
    return new Promise((resolve, reject) => {
      const url = "/api/situation/info/" + toString(id) + "/";
      client
        .get(url)
        .then(res =>
          resolve({
            situation_id: res.data.id,
            situation_name: res.data.situation_name
          })
        )
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  getList: () => {
    return new Promise((resolve, reject) => {
      const url = "/api/situation/list/";
      client
        .get(url)
        .then(res => resolve(res.data))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  }
};
