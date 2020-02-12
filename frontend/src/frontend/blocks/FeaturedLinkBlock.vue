<template>
  <v-card
    class="pa-4 font-italic title text-center"
    :href="block.value.href"
    :target="block.value.target"
    v-html="block.value.text"
    outlined
    tile
  />
</template>

<script>
export default {
  name: "FeaturedLinkBlock",
  props: ["block"]
};
</script>
