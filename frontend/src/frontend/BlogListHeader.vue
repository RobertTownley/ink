<template>
  <v-card tile flat class="mb-4">
    <v-img v-if="hasImg" :src="src" height="35vh">
      <div class="bottom-gradient"></div>
    </v-img>
    <v-container class="pa-0">
      <v-card-title class="display-3 py-0">{{ title }}</v-card-title>
      <v-card-subtitle class="title mt-2 py-0" v-if="subtitle">{{
        subtitle
      }}</v-card-subtitle>
    </v-container>
  </v-card>
</template>

<script>
export default {
  computed: {
    config() {
      return this.$store.state.frontend.config;
    },
    hasImg() {
      return true;
    },
    src() {
      return this.config.blogAvatar;
    },
    subtitle() {
      return this.config.blogSubtitle;
    },
    title() {
      return this.config.blogTitle;
    }
  }
};
</script>

<style scoped>
.bottom-gradient {
  background-image: linear-gradient(
    to top,
    rgba(256, 256, 256, 1) 0%,
    transparent 15vh
  );
  height: 35vh;
}
</style>
