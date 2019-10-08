import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import store from "./store";

Vue.use(Router);

const authorizeToken = (to, from, next) => {
  // 引数のto, fromはそれぞれ遷移先ルートと遷移元ルート
  if (to.meta.requiresAuth) {
    if (!store.state.auth || !store.state.auth.token) {
      next({ path: "/" });
    } else {
      // 引数なしのnext()を呼んだ場合は、通常の遷移が行われる。
      next();
    }
  } else {
    next();
  }
};

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
      meta: { requiresAuth: false }
    }
  ]
});

router.beforeEach(authorizeToken);

export default router;
