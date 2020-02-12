<template>
  <v-layout class="my-4 d-flex justify-space-between align-center">
    <div>
      <div class="title">{{ title }}</div>
      <WorkflowStateHeader />
    </div>
    <div class="d-flex flex-wrap justify-end">
      <RevisionHistory />
      <PreviewDialog v-if="previewFeatureHasBeenBuilt" />
      <v-btn @click="save" class="ml-1 primary" text>Save</v-btn>
      <PublishButton />
      <UnpublishButton v-if="workflowstate == 'Published'" />
    </div>
  </v-layout>
</template>

<script>
import PreviewDialog from "@/components/PreviewDialog";
import PublishButton from "@/components/PublishButton";
import RevisionHistory from "@/components/RevisionHistory";
import UnpublishButton from "@/components/UnpublishButton";
import WorkflowStateHeader from "@/components/WorkflowStateHeader";

export default {
  components: {
    PreviewDialog,
    PublishButton,
    RevisionHistory,
    UnpublishButton,
    WorkflowStateHeader
  },
  computed: {
    modelName() {
      const names = {
        article: "Article",
        blogentry: "Blog Entry",
        page: "Page"
      };
      return names[this.$route.params.modelName];
    },
    title() {
      if (this.$store.state.obj.id) {
        const { id, title } = this.$store.state.obj;
        const max = 40;
        const shortTitle =
          title.length > max ? title.slice(0, max) + "..." : title;
        return `Editing ${this.modelName} #${id}: ${shortTitle}`;
      } else {
        return `Add ${this.modelName}`;
      }
    },
    workflowstate() {
      return this.$store.state.obj.workflowstate;
    }
  },
  data() {
    return {
      previewFeatureHasBeenBuilt: false // TODO: Build preview
    };
  },
  methods: {
    save() {
      this.$store.dispatch("editor/save");
    },
    preview() {
      this.$store.dispatch("editor/preview");
    }
  }
};
</script>

<style lang="scss" scoped>
.workflowstate {
  height: auto;
  text-transform: capitalize;
}
</style>
