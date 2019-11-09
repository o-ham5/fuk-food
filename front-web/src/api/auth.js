import client from "./client";

export default {
  login: authInfo => {
    return new Promise((resolve, reject) => {
      client
        .post("/api/login/", authInfo)
        .then(res => resolve({ token: res.data.token }))
        .catch(err => {
          reject(err.response.data.detail[0]);
        });
    });
  },
  register: registerInfo => {
    return new Promise((resolve, reject) => {
      client
        .post("/api/account/register/", registerInfo)
        .then(res =>
          resolve({ username: res.data.username, email: res.data.email })
        )
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  checkUserName: usernameInfo => {
    return new Promise((resolve, reject) => {
      client
        .post("/api/account/check-username/", usernameInfo)
        .then(res => resolve({ res: res.data }))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  checkEmail: emailInfo => {
    return new Promise((resolve, reject) => {
      client
        .post("/api/account/check-email/", emailInfo)
        .then(res => resolve({ res: res.data }))
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  getUserInfo: token => {
    return new Promise((resolve, reject) => {
      client
        .get("/api/account/info/", {
          headers: { Authorization: "JWT " + token },
          data: {}
        })
        .then(res =>
          resolve({
            account_id: res.data.account_id,
            username: res.data.username,
            email: res.data.email,
            bias: res.data.bias,
            variance: res.data.variance,
            inyou: res.data.inyou,
            oshare: res.data.oshare,
            shokuji: res.data.shokuji,
            setsuyaku: res.data.setsuyaku
          })
        )
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  },
  update: (token, updateInfo) => {
    return new Promise((resolve, reject) => {
      client
        .patch("/api/account/update/", updateInfo, {
          headers: { Authorization: "JWT " + token },
          data: {}
        })
        .then(res =>
          resolve({
            result: res.data
          })
        )
        .catch(err => {
          reject(new Error(err.response.data.message || err.message));
        });
    });
  }
};
