import axios from "axios";

import router from "@/router";
import { getHeaders } from "@/utils/auth";

export default {
  clearFormErrors({ commit }) {
    commit("saveFormErrorsToStore", []);
  },
  loadLatestContent({ dispatch }) {
    axios({
      method: "GET",
      url: window.location.pathname + "?format=json"
    })
      .then(response => {
        dispatch("obj/setInitialFormValues", response.data, { root: true });
      })
      .catch(error => {
        const { messages } = error.response.data;
        dispatch("updateFormMessages", messages);
      })
      .finally(() => {
        dispatch("setEditorLoadingState", false);
      });
  },
  publish({ dispatch, getters }) {
    dispatch("clearFormErrors");
    let formData = getters.objectData;
    formData._cms_action = "publish";
    axios({
      headers: getHeaders(),
      method: "POST",
      url: window.location.pathname,
      data: formData
    })
      .then(response => {
        const { data, id, messages } = response.data;
        dispatch("updateFormMessages", messages);
        dispatch("obj/setInitialFormValues", data, { root: true });
        if (!formData.id) {
          // Saved for the first time; redirect to the change form
          const url = window.location.pathname;
          router.push(url.replace("/add/", `/${id}/change/`));
          dispatch(
            "obj/setFieldValue",
            { field: "id", value: id },
            { root: true }
          );
        }
      })
      .catch(error => {
        dispatch("updateFormErrors", error.response.data.errors);
      });
  },
  revertToPriorVersion({ dispatch }, revisionId) {
    const data = { _cms_action: "revert", revision_id: revisionId };
    axios({
      headers: getHeaders(),
      method: "POST",
      url: window.location.pathname,
      data
    }).then(response => {
      const { data } = response.data;
      dispatch("obj/setInitialFormValues", data, { root: true });
      dispatch("updateRevisionDialogStatus", null);
    });
  },
  save({ dispatch, getters, rootState }) {
    dispatch("clearFormErrors");
    let data = getters.objectData;
    data._cms_action = "save";
    axios({
      headers: getHeaders(),
      method: "POST",
      url: window.location.pathname,
      data
    })
      .then(response => {
        const { id, messages } = response.data;
        if (!rootState.obj.id) {
          dispatch(
            "obj/setFieldValue",
            { field: "id", value: id },
            { root: true }
          );
        }
        if (response.status == 201) {
          const url = window.location.pathname;
          router.push(url.replace("/add/", `/${id}/change/`));
        } else {
          dispatch("updateFormMessages", messages);
        }
      })
      .catch(error => {
        dispatch("updateFormErrors", error.response.data);
      });
  },
  setActiveBlockIndex({ commit }, index) {
    commit("saveActiveBlockIndexToStore", index);
  },
  setEditorLoadingState({ commit }, isLoading) {
    commit("saveEditorLoadingStateToStore", isLoading);
  },
  unpublish({ dispatch }) {
    axios({
      headers: getHeaders(),
      method: "POST",
      url: window.location.pathname,
      data: {
        _cms_action: "unpublish"
      }
    }).then(response => {
      const { messages } = response.data;
      dispatch("loadLatestContent");
      dispatch("updateFormMessages", messages);
    });
  },
  updatePreviewDialogStatus({ commit }, status) {
    commit("setShowPreviewDialog", status);
  },
  updatePublishDialogStatus({ commit }, status) {
    commit("setShowPublishDialog", status);
  },
  updateRevisionDialogStatus({ commit }, status) {
    commit("setShowRevisionDialog", status);
  },
  updateFormErrors({ commit }, errors) {
    commit("saveFormErrorsToStore", errors);
  },
  updateFormMessages({ commit }, messages) {
    commit("saveMessagesToStore", messages);
  }
};
