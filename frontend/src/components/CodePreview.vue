<template>
  <highlight-code :code="code" :lang="language" class="codeBlock" v-if="code" />
</template>

<script>
export default {
  props: ["code", "language"]
};
</script>

<style>
.hljs {
  height: 100%;
  width: 100%;
}
</style>
