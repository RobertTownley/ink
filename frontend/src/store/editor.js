// Vuex module for interacting with the object being edited through Ink
import editorActions from "@/store/editorActions";

export default {
  actions: editorActions,
  mutations: {
    saveActiveBlockIndexToStore(state, index) {
      state.activeBlockIndex = index;
    },
    saveMessagesToStore(state, messages) {
      state.messages = messages;
    },
    saveFormErrorsToStore(state, errors) {
      state.errors = errors;
    },
    saveEditorLoadingStateToStore(state, isLoading) {
      state.loading = isLoading;
    },
    setShowPreviewDialog(state, status) {
      state.showPreviewDialog = status;
    },
    setShowPublishDialog(state, status) {
      state.showPublishDialog = status;
    },
    setShowRevisionDialog(state, status) {
      state.showRevisionDialog = status;
    }
  },
  namespaced: true,
  getters: {
    objectId(state, getters, rootState) {
      // Retrieve the ID of the object from the `obj` store.
      // Used to determine if the object already exists, and if so
      // which save action to call.
      return rootState.obj.id;
    },
    objectData(state, getters, rootState, rootGetters) {
      return rootGetters["obj/objectData"];
    }
  },
  state: {
    activeBlockIndex: 0,
    config: {},
    errors: [],
    loading: true,
    messages: [],
    showPreviewDialog: false,
    showPublishDialog: false,
    showRevisionDialog: false
  }
};
