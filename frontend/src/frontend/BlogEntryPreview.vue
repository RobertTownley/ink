<template>
  <v-card class="ma-2" :href="href" outlined>
    <v-img v-if="src" :src="src" class="white--text align-end" />
    <v-card-title>{{ title }}</v-card-title>
    <v-card-subtitle class="overline pb-0 pt-2">{{ byline }}</v-card-subtitle>
    <v-card-subtitle class="overline pt-0 pb-2">{{ pubDate }}</v-card-subtitle>
  </v-card>
</template>

<script>
export default {
  computed: {
    src() {
      const { lead_block } = this.entry.content;
      if (!lead_block || lead_block.block_type != "image") return null;
      const { image } = lead_block.value;
      return image.optimized;
    },
    href() {
      return `/blog/${this.entry.slug}/`;
    },
    byline() {
      const authors = this.entry.content.authors.map(
        author => author.display_name
      );
      return `Written by ${authors.join(", ")}`;
    },
    pubDate() {
      const pubDate = new Date(this.entry.publication_date).toLocaleString();
      return `Published on ${pubDate}`;
    },
    title() {
      return this.entry.content.title;
    }
  },
  props: ["entry"]
};
</script>
