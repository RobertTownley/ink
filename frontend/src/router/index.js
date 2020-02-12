import Vue from "vue";
import VueRouter from "vue-router";

import BlogListView from "@/views/BlogListView";
import BlogDetailView from "@/views/BlogDetailView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/admin/:appName/:modelName/add/",
    name: "AddForm",
    component: () =>
      import(/* webpackChunkName: "editor" */ "../views/InkEditor.vue")
  },
  {
    path: "/admin/:appName/:modelName/:id/change/",
    name: "ChangeForm",
    component: () =>
      import(/* webpackChunkName: "editor" */ "../views/InkEditor.vue")
  },
  {
    path: "/blog/",
    name: "BlogListView",
    component: BlogListView
  },
  {
    path: "/blog/:slug/",
    name: "BlogDetailView",
    component: BlogDetailView
  }
];

const router = new VueRouter({
  mode: "history",
  base: "/",
  routes
});

export default router;
