<template>
  <div v-if="errors.length">
    <v-alert
      v-for="(error, index) in errors"
      :key="index"
      type="error"
      dense
      dismissible
      outlined
      ><span class="errorField">{{ error.field }}</span
      >: {{ error.message }}
    </v-alert>
  </div>
</template>

<script>
export default {
  computed: {
    errors() {
      return Object.entries(this.$store.state.editor.errors).map(error => {
        const message = error[1].length ? error[1][0] : error[1];
        return { field: error[0], message };
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.errorField {
  font-weight: bold;
  text-transform: capitalize;
}
</style>
