const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  assetsDir: "./assets",
  publicPath:
    process.env.NODE_ENV === "production"
      ? "/static/ink_cms/dist/"
      : "http://0.0.0.0:9005",
  filenameHashing: false,
  indexPath: "/backend/ink_cms/templates/ink_cms/index.html",
  outputDir: "/backend/ink_cms/static/ink_cms/dist/",
  transpileDependencies: ["vuetify"],
  chainWebpack: config => {
    config.optimization.splitChunks(false);
    config
      .plugin("BundleTracker")
      .use(BundleTracker, [{ filename: "./webpack-stats.json" }]);
    config.resolve.alias.set("__STATIC__", "static");
    config.devServer
      .public("http://0.0.0.0:9005")
      .host("0.0.0.0")
      .port(9005)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .headers({ "Access-Control-Allow-Origin": ["*"] });
  }
};
