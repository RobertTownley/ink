<template>
  <v-subheader class="caption ma-0 pa-0 workflowstate"
    >Current State: {{ workflowstate }}</v-subheader
  >
</template>

<script>
export default {
  computed: {
    workflowstate() {
      const { id, workflowstate } = this.$store.state.obj;
      if (!id) return "Unsaved";
      return workflowstate;
    }
  }
};
</script>
