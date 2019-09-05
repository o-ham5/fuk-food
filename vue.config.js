module.exports = {
  devServer: {
    host: "localhost",
    port: 8081,
    disableHostCheck: true
  },

  pluginOptions: {
    express: {
      shouldServeApp: true,
      serverDir: './srv'
    }
  }
};
