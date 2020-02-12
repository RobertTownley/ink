<template>
  <div v-html="block.value.embedCode" />
</template>

<script>
export default {
  name: "EmbedBlock",
  props: ["block"]
};
</script>
