<template>
  <v-col cols="12">
    <div class="title">{{ displayMsg }}</div>
  </v-col>
</template>

<script>
export default {
  data() {
    return {
      displayMsg: this.msg ? this.msg : "Loading..."
    };
  },
  props: ["msg"]
};
</script>
