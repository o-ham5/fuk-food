// const path = require("path");
// const PrerenderSPAPlugin = require("prerender-spa-plugin");

module.exports = {
  devServer: {
    host: "localhost",
    port: 8081,
    disableHostCheck: true
  }

  // pluginOptions: {
  //   express: {
  //     shouldServeApp: true,
  //     serverDir: "./srv"
  //   }
  // },

  // configureWebpack: () => {
  //   return {
  //     plugins: [
  //       new PrerenderSPAPlugin({
  //         staticDir: path.join(__dirname, "dist"),
  //         routes: ["/", "/home", "/kuchikomi", "/spot", "/meta"]
  //       })
  //     ]
  //   };
  // }
};
