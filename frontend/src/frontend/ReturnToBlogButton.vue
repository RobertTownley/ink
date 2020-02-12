<template>
  <v-btn @click="returnToBlog" class="mx-0 my-2" outlined>
    <v-icon class="pr-1">mdi-arrow-left</v-icon>Return to blog</v-btn
  >
</template>
<script>
export default {
  methods: {
    returnToBlog() {
      this.$router.push("/blog/");
    }
  }
};
</script>
