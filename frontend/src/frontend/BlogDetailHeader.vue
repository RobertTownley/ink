<template>
  <v-card tile flat>
    <v-img v-if="hasImg" :src="src" height="50vh" class="white--text align-end">
      <div class="fill-height bottom-gradient">
        <v-card-title>{{ title }}</v-card-title>
        <v-card-subtitle v-if="obj.subtitle" class="white--text">{{
          subtitle
        }}</v-card-subtitle>
      </div>
    </v-img>
    <v-container v-else>
      <h1 class="display-3 mt-4 mb-1">{{ title }}</h1>
      <h2 class="title">{{ subtitle }}</h2>
    </v-container>
  </v-card>
</template>

<script>
export default {
  computed: {
    block() {
      return this.obj.lead_block;
    },
    hasImg() {
      return this.block.block_type && this.block.block_type == "image";
    },
    obj() {
      const { obj } = this.$store.state.frontend;
      return obj ? obj.content : {};
    },
    src() {
      return this.block.value.image.optimized;
    },
    subtitle() {
      return this.obj.subtitle;
    },
    title() {
      return this.obj.title;
    }
  },
  props: ["listPage"]
};
</script>

<style scoped>
.bottom-gradient {
  background-image: linear-gradient(
    to top,
    rgba(0, 0, 0, 0.4) 0%,
    transparent 128px
  );
}
</style>
