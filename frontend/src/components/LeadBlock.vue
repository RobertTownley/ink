<template>
  <div>
    <CodeBlockEditor v-if="blockType == 'code'" :block="block" :lead="true" />
    <EmbedBlockEditor v-if="blockType == 'embed'" :block="block" :lead="true" />
    <ImageBlockEditor v-if="blockType == 'image'" :block="block" :lead="true" />
    <TextBlockEditor v-if="blockType == 'text'" :block="block" :lead="true" />
  </div>
</template>

<script>
import CodeBlockEditor from "@/components/blocks/CodeBlockEditor";
import EmbedBlockEditor from "@/components/blocks/EmbedBlockEditor";
import ImageBlockEditor from "@/components/blocks/ImageBlockEditor";
import TextBlockEditor from "@/components/blocks/TextBlockEditor";

export default {
  components: {
    CodeBlockEditor,
    EmbedBlockEditor,
    ImageBlockEditor,
    TextBlockEditor
  },
  computed: {
    blockType() {
      const { lead_block } = this.$store.state.obj;
      return lead_block ? lead_block.block_type : null;
    },
    block() {
      return this.$store.state.obj.lead_block;
    }
  }
};
</script>
