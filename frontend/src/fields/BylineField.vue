<template>
  <v-container class="pa-0">
    <v-row no-gutters>
      <v-col cols="6">
        <v-combobox
          v-model="authors"
          class="mr-2"
          :items="availableAuthors"
          item-text="display_name"
          item-value="id"
          label="Authors"
          multiple
          chips
          deletable-chips
          dense
          hide-selected
          outlined
        />
      </v-col>
      <v-col cols="6">
        <v-combobox
          v-model="contributors"
          class="ml-2"
          :items="availableAuthors"
          item-text="display_name"
          item-value="id"
          label="Contributors"
          multiple
          chips
          deletable-chips
          dense
          hide-selected
          outlined
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  computed: {
    authors: {
      get() {
        return this.$store.state.obj.authors;
      },
      set(value) {
        const payload = { field: "authors", value };
        this.$store.dispatch("obj/setFieldValue", payload);
      }
    },
    contributors: {
      get() {
        return this.$store.state.obj.contributors;
      },
      set(value) {
        const payload = { field: "contributors", value };
        this.$store.dispatch("obj/setFieldValue", payload);
      }
    }
  },
  data() {
    return {
      availableAuthors: []
    };
  },
  methods: {
    retrieveAuthors(url) {
      axios({
        method: "GET",
        url
      }).then(response => {
        this.availableAuthors = this.availableAuthors.concat(response.data);
      });
    }
  },
  mounted() {
    this.retrieveAuthors("/ink/api/v1/staff/");
  }
};
</script>
