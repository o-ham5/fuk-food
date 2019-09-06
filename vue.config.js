module.exports = {
  devServer: {
    host: "localhost",
    port: 8081,
    disableHostCheck: true
  },

  pluginOptions: {
    express: {
      shouldServeApp: true,
      serverDir: "./srv"
    }
  }
};

// const webpack = require("webpack");

// module.exports = {
//   configureWebpack: {
//     plugins: [
//       new webpack.ProvidePlugin({
//         mapboxgl: "mapbox-gl"
//       })
//     ]
//   }
// };
