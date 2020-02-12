<template>
  <div v-html="text" />
</template>

<script>
export default {
  computed: {
    text() {
      return this.block.value.text;
    }
  },
  name: "TextBlock",
  props: ["block"]
};
</script>
