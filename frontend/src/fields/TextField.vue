<template>
  <v-text-field
    v-model="value"
    :error="error"
    :error-messages="errorMessages"
    :label="label"
    class="my-2"
    dense
  />
</template>

<script>
export default {
  computed: {
    error() {
      const { errors } = this.$store.state.editor;
      return errors && errors[this.field] && errors[this.field].length > 0;
    },
    errorMessages() {
      const { errors } = this.$store.state.editor;
      return errors && errors[this.field] ? errors[this.field] : [];
    },
    value: {
      get() {
        return this.$store.state.obj[this.field];
      },
      set(value) {
        const payload = { field: this.field, value };
        this.$store.dispatch("obj/setFieldValue", payload);
      }
    }
  },

  props: ["field", "label"]
};
</script>
