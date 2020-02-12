<template>
  <v-img :alt="alt" :src="src" class="white--text align-end">
    <div class="caption pa-2" v-if="caption">{{ caption }}</div>
  </v-img>
</template>

<script>
export default {
  computed: {
    alt() {
      return this.block.value.alt_text;
    },
    caption() {
      return this.block.value.caption;
    },
    src() {
      return this.block.value.image.optimized;
    }
  },
  name: "ImageBlock",
  props: ["block"]
};
</script>
