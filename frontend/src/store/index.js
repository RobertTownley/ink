import Vue from "vue";
import Vuex from "vuex";

import EditorModule from "@/store/editor.js";
import FrontendModule from "@/store/frontend.js";
import ObjectModule from "@/store/obj.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    editor: EditorModule,
    frontend: FrontendModule,
    obj: ObjectModule
  }
});
