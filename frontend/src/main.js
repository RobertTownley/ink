import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import CKEditor from "@ckeditor/ckeditor5-vue";
import VueHighlightJS from "vue-highlight.js";

import "highlight.js/styles/default.css";
import "roboto-fontface/css/roboto/roboto-fontface.css";
import "@mdi/font/css/materialdesignicons.css";
import "vue-highlight.js/lib/allLanguages";

Vue.config.productionTip = false;
Vue.use(CKEditor);
Vue.use(VueHighlightJS);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
