<template>
  <v-container>
    <ckeditor
      :editor="editor"
      v-model="editorData"
      :config="editorConfig"
    ></ckeditor>
  </v-container>
</template>

<script>
import BaseBlock from "@/components/blocks/BaseBlock";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";

export default {
  computed: {
    editorData: {
      get: function() {
        return this.block.value.text;
      },
      set: function(rawValue) {
        const value = { text: rawValue };
        if (this.lead) {
          this.$store.dispatch("obj/editLeadBlockValue", value);
        } else {
          const payload = { index: this.index, value };
          this.$store.dispatch("obj/editBlockValue", payload);
        }
      }
    }
  },
  data() {
    return {
      editor: ClassicEditor,
      editorConfig: {
        rect: {
          height: 600
        }
      }
    };
  },
  extends: BaseBlock,
  name: "TextBlockEditor"
};
</script>

<style>
.ck-content {
  height: 300px;
}
</style>
