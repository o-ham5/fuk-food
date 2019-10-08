import client from "./client";

export default {
  register: registerInfo => {
    return new Promise((resolve, reject) => {
      client
        .post("/api/area/register/", registerInfo)
        .then(res =>
          resolve({ id: res.data.id, area_name: res.data.area_name })
        )
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  getInfo: id => {
    return new Promise((resolve, reject) => {
      const url = "/api/area/info/" + toString(id) + "/";
      client
        .get(url)
        .then(res =>
          resolve({
            area_id: res.data.id,
            area_name: res.data.area_name
          })
        )
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  getList: () => {
    return new Promise((resolve, reject) => {
      const url = "/api/area/list/";
      client
        .get(url)
        .then(res => resolve(res.data))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  }
};
