<template>
  <v-container v-if="!$store.state.editor.loading">
    <FormMessages v-if="messages" />
    <ErrorDetails />
    <ObjectActions />

    <HeadlineEditor />
    <LeadContentEditor />
    <ContentTabs />
  </v-container>
  <v-container v-else>
    <div style="text-align: center;">
      CMS Loaded. Retrieving latest content version...
    </div>
  </v-container>
</template>

<script>
import { getBlockTypes } from "@/utils/blockTypes";

import ContentTabs from "@/components/ContentTabs";
import ErrorDetails from "@/components/ErrorDetails";
import FormMessages from "@/components/FormMessages";
import HeadlineEditor from "@/components/HeadlineEditor";
import LeadContentEditor from "@/components/LeadContentEditor";
import ObjectActions from "@/components/ObjectActions";

export default {
  components: {
    ContentTabs,
    ErrorDetails,
    FormMessages,
    HeadlineEditor,
    LeadContentEditor,
    ObjectActions
  },
  computed: {
    messages() {
      return this.$store.state.editor.messages.length >= 0;
    }
  },
  methods: {
    loadNewContent() {
      this.$store.dispatch("editor/setEditorLoadingState", false);

      // Add initial block to content area
      this.$store.dispatch("obj/addNewBlock", getBlockTypes()[0]);
      this.$store.dispatch("editor/setActiveBlockIndex", 0);
    }
  },
  mounted() {
    if (this.$route.params.id) {
      this.$store.dispatch("editor/loadLatestContent");
    } else {
      this.loadNewContent();
    }
  },
  name: "InkEditor"
};
</script>
