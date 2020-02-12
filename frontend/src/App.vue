<template>
  <v-app>
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
export default {
  mounted() {
    const elem = document.getElementById("frontend_context");
    if (elem) {
      const rawData = JSON.parse(elem.textContent);
      this.$store.dispatch("frontend/setFrontendContext", JSON.parse(rawData));
    }
  },
  name: "App"
};
</script>

<style lang="scss">
.v-card__text,
.v-card__title {
  word-break: normal !important;
}
</style>
