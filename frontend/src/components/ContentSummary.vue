<template>
  <v-container>
    <v-row dense v-for="(item, i) in contentItems" :key="i">
      <v-col cols="2">
        <b>{{ item.label }}: </b>
      </v-col>
      <v-col>{{ item.value }}</v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  computed: {
    contentItems() {
      const { obj } = this.$store.state;
      return [
        { label: "Title", value: obj.title },
        { label: "Subtitle", value: obj.subtitle }
      ];
    }
  }
};
</script>
