<template>
  <v-btn @click="publish" class="ml-1 primary" text>Unpublish</v-btn>
</template>

<script>
export default {
  methods: {
    publish() {
      this.$store.dispatch("editor/unpublish");
    }
  }
};
</script>
