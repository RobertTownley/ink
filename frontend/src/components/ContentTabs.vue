<template>
  <v-card class="pa-4 mt-4 ">
    <v-tabs v-model="tab" color="primary" grow>
      <v-tab v-for="item in items" :key="item">{{ item }}</v-tab>
      <v-tabs-items v-model="tab">
        <v-tab-item key="Content">
          <ContentEditor />
        </v-tab-item>
        <v-tab-item key="URLs">
          <URLEditor />
        </v-tab-item>
        <v-tab-item key="Tags">
          <TagEditor />
        </v-tab-item>
        <v-tab-item key="Advanced">
          <AdvancedEditor />
        </v-tab-item>
      </v-tabs-items>
    </v-tabs>
  </v-card>
</template>

<script>
import AdvancedEditor from "@/components/AdvancedEditor";
import ContentEditor from "@/components/ContentEditor";
import URLEditor from "@/components/URLEditor";
import TagEditor from "@/components/TagEditor";

export default {
  components: {
    AdvancedEditor,
    ContentEditor,
    TagEditor,
    URLEditor
  },
  data() {
    return {
      items: ["Content", "URLs", "Tags", "Advanced"],
      tab: null
    };
  }
};
</script>
