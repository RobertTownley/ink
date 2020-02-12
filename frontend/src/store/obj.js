// Vuex module for interacting with the object being edited through Ink

export default {
  actions: {
    addNewBlock({ commit }, model) {
      const block = {
        block_type: model.block_type,
        value: JSON.parse(JSON.stringify(model.default_value))
      };
      commit("addNewBlockToStore", block);
    },
    editBlockValue(context, payload) {
      context.commit("updateBlockValue", payload);
    },
    editLeadBlockValue({ commit }, value) {
      commit("updateLeadBlockValue", value);
    },
    removeBlock({ commit, state }, index) {
      const newBlocks = state.blocks.filter((block, i) => i != index);
      commit("saveFieldValueToStore", {
        field: "blocks",
        value: newBlocks
      });
    },
    setFieldValue({ commit }, payload) {
      commit("saveFieldValueToStore", payload);
    },
    setInitialFormValues({ commit }, data) {
      for (let [field, value] of Object.entries(data)) {
        commit("saveFieldValueToStore", { field, value });
      }
    }
  },
  getters: {
    objectData(state) {
      return JSON.parse(JSON.stringify(state));
    }
  },
  mutations: {
    addNewBlockToStore(state, newBlock) {
      let blocks = JSON.parse(JSON.stringify(state.blocks));
      blocks.push(newBlock);
      state.blocks = blocks;
    },
    saveFieldValueToStore(state, payload) {
      state[payload.field] = payload.value;
    },
    updateBlockValue(state, payload) {
      let blocks = JSON.parse(JSON.stringify(state.blocks));
      blocks[payload.index].value = payload.value;
      state.blocks = blocks;
    },
    updateLeadBlockValue(state, value) {
      state.lead_block.value = value;
    }
  },
  namespaced: true,
  state: {
    advancedFields: [],
    authors: [],
    blocks: [],
    contributors: [],
    first_publication_date: null,
    id: null,
    lead_block: {},
    publication_date: null,
    pub_date_str: null,
    pub_time_str: null,
    site_section: null,
    slug: null,
    subtitle: null,
    tags: [],
    title: null,
    urls: [],
    workflowstate: "Draft"
  }
};
