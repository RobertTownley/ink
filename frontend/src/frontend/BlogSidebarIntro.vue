<template>
  <div>
    <h1 class="title mb-2">{{ label }}</h1>
    <v-img v-if="src" :src="src" class="mb-2" />
    <div v-html="text" />
  </div>
</template>

<script>
export default {
  computed: {
    settings() {
      return this.$store.state.frontend.config;
    },
    label() {
      return this.settings.blogSidebarLabel;
    },
    src() {
      return this.settings.blogSidebarAvatar;
    },
    text() {
      return this.settings.blogSidebarText;
    }
  }
};
</script>
