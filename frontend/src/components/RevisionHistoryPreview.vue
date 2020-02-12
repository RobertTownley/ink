<template>
  <v-expansion-panel-header>
    {{ revision.action }} by {{ revision.user.display_name }} on {{ date }}
  </v-expansion-panel-header>
</template>

<script>
export default {
  computed: {
    date() {
      const date = new Date(this.revision.date_created);
      return date.toLocaleString();
    }
  },
  props: ["revision"]
};
</script>
