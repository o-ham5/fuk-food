import client from "./client";

export default {
  login: authInfo => {
    return new Promise((resolve, reject) => {
      client
        .post("/api/login/", authInfo)
        .then(res => resolve({ token: res.data.token }))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  register: registerInfo => {
    return new Promise((resolve, reject) => {
      client
        .post("/api/register/", registerInfo)
        .then(res =>
          resolve({ username: res.data.username, email: res.data.email })
        )
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  getUserInfo: token => {
    return new Promise((resolve, reject) => {
      client
        .get("/api/user-info/", {
          headers: { Authorization: "JWT " + token },
          data: {}
        })
        .then(res =>
          resolve({ username: res.data.username, email: res.data.email })
        )
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  }
};
