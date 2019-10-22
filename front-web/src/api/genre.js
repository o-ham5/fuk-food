import client from "./client";

export default {
  register: registerInfo => {
    return new Promise((resolve, reject) => {
      client
        .post("/api/genre/register/", registerInfo)
        .then(res =>
          resolve({
            genre_id: res.data.genre_id,
            genre_name: res.data.genre_name
          })
        )
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  getInfo: genre_id => {
    return new Promise((resolve, reject) => {
      const url = "/api/genre/info/" + toString(genre_id) + "/";
      client
        .get(url)
        .then(res =>
          resolve({
            genre_id: res.data.genre_id,
            genre_name: res.data.genre_name
          })
        )
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  getList: () => {
    return new Promise((resolve, reject) => {
      const url = "/api/genre/list/";
      client
        .get(url)
        .then(res => resolve(res.data))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  }
};
