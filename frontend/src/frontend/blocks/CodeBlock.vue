<template>
  <highlight-code :code="code" :lang="language" v-if="code" />
</template>

<script>
export default {
  computed: {
    code() {
      return this.block.value.code;
    },
    language() {
      return this.block.value.language;
    }
  },
  name: "CodeBlock",
  props: ["block"]
};
</script>
