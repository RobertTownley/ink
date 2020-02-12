<template>
  <div v-if="tags.length" class="d-flex text-center align-baseline flex-wrap">
    <span v-for="(tag, index) in tags" :key="index" class="mr-2 mb-2">
      <v-chip @click="() => navigateToSearch(tag)">{{ tag.name }}</v-chip>
    </span>
  </div>
</template>

<script>
export default {
  computed: {
    obj() {
      return this.$store.state.frontend.obj;
    },
    tags() {
      if (!this.obj.tags || !this.obj.tags.length) return [];
      return this.obj.tags.map(tag => {
        return typeof tag == "object" ? tag : { name: tag };
      });
    }
  },
  methods: {
    navigateToSearch(tag) {
      this.$router.push(`/blog/?tag=${tag.name}`);
    }
  }
};
</script>
