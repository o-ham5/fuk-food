// https://eslint.org/docs/user-guide/configuring

module.exports = {
  root: true,
  parser: "vue-eslint-parser",
  parserOptions: {
    sourceType: "module",
    parser: "babel-eslint"
  },
  env: {
    browser: true
  },
  extends: [
    "eslint:recommended",
    "plugin:prettier/recommended",
    // https://github.com/vuejs/eslint-plugin-vue#priority-a-essential-error-prevention
    // consider switching to `plugin:vue/strongly-recommended` or `plugin:vue/recommended` for stricter rules.
    //'plugin:vue/essential',
    "plugin:vue/recommended",
    // https://github.com/standard/standard/blob/master/docs/RULES-en.md
    "prettier/vue"
  ],
  // required to lint *.vue files
  plugins: ["vue"],
  // add your custom rules here
  rules: {
    // allow async-await
    "generator-star-spacing": "off",
    // allow debugger during development
    // 'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off'
    "no-debugger": process.env.NODE_ENV === "production" ? "error" : "off",
    "no-console": "off",
    "import/no-webpack-loader-syntax":
      process.env.NODE_ENV === "production" ? "error" : "off",
    "no-plusplus": "off",
    "func-names": "off",
    "vue/component-name-in-template-casing": "off"
  }
};
