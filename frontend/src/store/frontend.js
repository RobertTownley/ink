// Vuex module for interacting with the object being edited through Ink

import axios from "axios";

export default {
  actions: {
    clearObjectData({ commit }) {
      commit("saveObjectDataToStore", {});
    },
    retrieveEntries({ commit, state }, payload) {
      axios({
        method: "GET",
        url: payload.url,
        params: payload.params
      }).then(response => {
        const { next, results } = response.data;
        commit("saveBlogSearchUrlToStore", next);
        commit("saveEntriesToStore", state.entries.concat(results));
      });
    },
    setEntries({ commit }, entries) {
      commit("saveEntriesToStore", entries);
    },
    setFrontendContext({ commit }, payload) {
      commit("saveFrontendContextToStore", payload);
    },
    setInitialObjectData({ commit }, obj) {
      commit("saveObjectDataToStore", obj);
    }
  },
  mutations: {
    saveBlogSearchUrlToStore(state, url) {
      state.blogSearchUrl = url;
    },
    saveEntriesToStore(state, entries) {
      state.entries = entries;
    },
    saveFrontendContextToStore(state, payload) {
      state.config = payload;
    },
    saveObjectDataToStore(state, obj) {
      state.obj = obj;
    }
  },
  namespaced: true,
  state: {
    blogSearchUrl: "/ink/api/v1/blogentries/",
    config: {},
    entries: [],
    obj: {}
  }
};
