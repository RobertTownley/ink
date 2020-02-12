<template>
  <div>
    <div class="caption my-0" v-if="attribution">{{ attribution }}</div>
    <div class="caption mb-4" v-if="caption">{{ caption }}</div>
    <div class="my-4" v-for="(block, index) in content.blocks" :key="index">
      <CodeBlock :block="block" v-if="block.block_type == 'code'" />
      <EmbedBlock :block="block" v-if="block.block_type == 'embed'" />
      <FeaturedLinkBlock
        :block="block"
        v-if="block.block_type == 'featured_link'"
      />
      <ImageBlock :block="block" v-if="block.block_type == 'image'" />
      <PullQuoteBlock :block="block" v-if="block.block_type == 'pull_quote'" />
      <SectionHeaderBlock
        :block="block"
        v-if="block.block_type == 'section_header'"
      />
      <TextBlock :block="block" v-if="block.block_type == 'text'" />
    </div>
  </div>
</template>

<script>
import CodeBlock from "@/frontend/blocks/CodeBlock";
import EmbedBlock from "@/frontend/blocks/EmbedBlock";
import FeaturedLinkBlock from "@/frontend/blocks/FeaturedLinkBlock";
import ImageBlock from "@/frontend/blocks/ImageBlock";
import PullQuoteBlock from "@/frontend/blocks/PullQuoteBlock";
import SectionHeaderBlock from "@/frontend/blocks/SectionHeaderBlock";
import TextBlock from "@/frontend/blocks/TextBlock";

export default {
  components: {
    CodeBlock,
    EmbedBlock,
    FeaturedLinkBlock,
    ImageBlock,
    PullQuoteBlock,
    SectionHeaderBlock,
    TextBlock
  },
  computed: {
    content() {
      return this.obj ? this.obj.content : {};
    },
    attribution() {
      if (
        this.content.lead_block &&
        this.content.lead_block.block_type == "image" &&
        this.content.lead_block.value.attribution
      ) {
        return `Photo Credit: ${this.content.lead_block.value.attribution}`;
      }
      return null;
    },
    caption() {
      const date = new Date(this.obj.publication_date).toLocaleString();
      return `Published on ${date}`;
    },
    obj() {
      return this.$store.state.frontend.obj;
    }
  }
};
</script>
