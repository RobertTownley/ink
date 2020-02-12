<template>
  <v-btn @click="publish" class="ml-1 primary" text>{{ label }}</v-btn>
</template>

<script>
export default {
  computed: {
    label() {
      const publishMsg =
        this.$store.state.obj.workflowstate == "Published"
          ? "Republish"
          : "Publish";
      return `Save and ${publishMsg}`;
    }
  },
  methods: {
    publish() {
      this.$store.dispatch("editor/publish");
    }
  }
};
</script>
