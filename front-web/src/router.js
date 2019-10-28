import Vue from "vue";
import Router from "vue-router";
import Top from "@/views/Top.vue";
import Home from "@/views/Home.vue";
import MetaView from "@/views/MetaView.vue";
import SpotView from "@/views/SpotView.vue";
import KuchikomiView from "@/views/KuchikomiView.vue";
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
      name: "top",
      component: Top,
      meta: { requiresAuth: false }
    },
    {
      path: "/home",
      name: "home",
      component: Home,
      meta: { requiresAuth: false }
    },
    {
      path: "/spot",
      name: "spot",
      component: SpotView,
      meta: { requiresAuth: false }
    },
    {
      path: "/kuchikomi",
      name: "kuchikomi",
      component: KuchikomiView,
      meta: { requiresAuth: true }
    },
    {
      path: "/meta",
      name: "meta",
      component: MetaView,
      meta: { requiresAuth: false }
    }
  ]
});

router.beforeEach(authorizeToken);

export default router;
