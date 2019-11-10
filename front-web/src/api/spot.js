import client from "./client";

export default {
  register: registerInfo => {
    return new Promise((resolve, reject) => {
      client
        .post("/api/spot/register/", registerInfo)
        .then(res =>
          resolve({
            spot_id: res.data.spot_id,
            spot_name: res.data.spot_name,
            area: res.data.area,
            genre: res.data.genre,
            latitude: res.data.latitude,
            longitude: res.data.longitude,
            link: res.data.link,
            evaluated_score: res.data.evaluated_score
          })
        )
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  getInfo: spot_id => {
    return new Promise((resolve, reject) => {
      const url = "/api/spot/info/" + toString(spot_id) + "/";
      client
        .get(url)
        .then(res =>
          resolve({
            spot_id: res.data.spot_id,
            spot_name: res.data.spot_name,
            area: res.data.area,
            genre: res.data.genre,
            latitude: res.data.latitude,
            longitude: res.data.longitude,
            link: res.data.link,
            evaluated_score: res.data.evaluated_score
          })
        )
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  getList: () => {
    return new Promise((resolve, reject) => {
      const url = "/api/spot/list/";
      client
        .get(url)
        .then(res => resolve(res.data))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  getTop3List: query => {
    return new Promise((resolve, reject) => {
      const url = "/api/spot/top3-list/";
      client
        .get(url, {
          params: query,
          data: {}
        })
        .then(res => resolve(res.data))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  update: (spot_id, updateInfo) => {
    return new Promise((resolve, reject) => {
      const url = "/api/spot/update/" + spot_id + "/";
      client
        .put(url, updateInfo)
        .then(res =>
          resolve({
            spot_id: res.data.spot_id,
            spot_name: res.data.spot_name,
            area: res.data.area,
            genre: res.data.genre,
            latitude: res.data.latitude,
            longitude: res.data.longitude,
            link: res.data.link,
            evaluated_score: res.data.evaluated_score
          })
        )
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  delete: spot_id => {
    return new Promise((resolve, reject) => {
      const url = "/api/spot/delete/" + spot_id + "/";
      client
        .delete(url)
        .then(res => resolve({}))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  }
};
