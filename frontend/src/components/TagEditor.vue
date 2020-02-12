<template>
  <v-container>
    <v-combobox
      v-model="value"
      :hint="hint"
      :items="availableTags"
      item-text="name"
      item-value="id"
      :label="label"
      multiple
      clearable
      chips
      deletable-chips
      persistent-hint
    />
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  computed: {
    hint() {
      return 'Topics related to this content. Examples: "Cooking", "Programming", etc.';
    },
    label() {
      if (!this.value || !this.value.length) return "Add Tags";
      const { length } = this.value;
      return `${length} tag${length > 1 ? "s" : ""}`;
    },
    value: {
      get() {
        return this.$store.state.obj.tags;
      },
      set(value) {
        const payload = { field: "tags", value };
        this.$store.dispatch("obj/setFieldValue", payload);
      }
    }
  },
  data() {
    return {
      availableTags: []
    };
  },
  methods: {
    retrieveTags(url) {
      axios({
        method: "GET",
        url
      }).then(response => {
        const { results, next } = response.data;
        if (!results) return;
        this.availableTags = this.availableTags.concat(results);
        if (next) {
          this.retrieveTags(next);
        }
      });
    }
  },
  mounted() {
    this.retrieveTags("/ink/api/v1/tags/");
  }
};
</script>
