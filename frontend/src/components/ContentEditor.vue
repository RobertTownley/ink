<template>
  <v-container>
    <v-expansion-panels :value="panel" v-if="hasBlocks">
      <v-expansion-panel v-for="(block, index) in blocks" :key="index">
        <v-expansion-panel-header>{{
          previewText(block)
        }}</v-expansion-panel-header>
        <v-expansion-panel-content>
          <CodeBlockEditor
            v-if="block.block_type == 'code'"
            :block="block"
            :index="index"
          />
          <EmbedBlockEditor
            v-if="block.block_type == 'embed'"
            :block="block"
            :index="index"
          />
          <FeaturedLinkBlockEditor
            v-if="block.block_type == 'featured_link'"
            :block="block"
            :index="index"
          />
          <ImageBlockEditor
            v-if="block.block_type == 'image'"
            :block="block"
            :index="index"
          />
          <PullQuoteBlockEditor
            v-if="block.block_type == 'pull_quote'"
            :block="block"
            :index="index"
          />
          <SectionHeaderBlockEditor
            v-if="block.block_type == 'section_header'"
            :block="block"
            :index="index"
          />
          <TextBlockEditor
            v-if="block.block_type == 'text'"
            :block="block"
            :index="index"
          />
          <BlockOptions :block="block" :index="index" class="mt-4" />
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
    <h1 class="mt-4 mt-2 title">Add New Block</h1>
    <NewBlockField />
  </v-container>
</template>

<script>
import BlockOptions from "@/components/BlockOptions";

import CodeBlockEditor from "@/components/blocks/CodeBlockEditor";
import FeaturedLinkBlockEditor from "@/components/blocks/FeaturedLinkBlockEditor";
import EmbedBlockEditor from "@/components/blocks/EmbedBlockEditor";
import ImageBlockEditor from "@/components/blocks/ImageBlockEditor";
import NewBlockField from "@/fields/NewBlockField";
import PullQuoteBlockEditor from "@/components/blocks/PullQuoteBlockEditor";
import SectionHeaderBlockEditor from "@/components/blocks/SectionHeaderBlockEditor";
import TextBlockEditor from "@/components/blocks/TextBlockEditor";

import { getPreview } from "@/utils/preview";

export default {
  components: {
    BlockOptions,
    CodeBlockEditor,
    EmbedBlockEditor,
    FeaturedLinkBlockEditor,
    ImageBlockEditor,
    NewBlockField,
    PullQuoteBlockEditor,
    SectionHeaderBlockEditor,
    TextBlockEditor
  },
  computed: {
    blocks() {
      return this.$store.state.obj.blocks;
    },
    hasBlocks() {
      return this.blocks && this.blocks.length && this.blocks.length > 0;
    },
    panel() {
      return this.$store.state.editor.activeBlockIndex;
    }
  },
  methods: {
    previewText(block) {
      return getPreview(block);
    }
  }
};
</script>
