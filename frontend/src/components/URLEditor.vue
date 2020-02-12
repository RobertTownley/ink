<template>
  <v-container>
    <v-simple-table v-if="urls.length">
      <v-subheader>Current URLs</v-subheader>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">Alternative URL Value</th>
            <th class="text-left">Is Final</th>
            <th class="text-left">Delete</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(url, index) in urls" :key="url.value">
            <td>{{ url.value }}</td>
            <td><FinalURLCheckbox :url="url" :index="index" /></td>
            <td>
              <v-btn text icon color="gray" @click="() => deleteUrl(index)">
                <v-icon>mdi-delete</v-icon>
              </v-btn>
            </td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
    <v-layout class="d-flex align-baseline justify-space-between">
      <v-text-field
        v-model="newUrl"
        :errors="errors"
        :error="errors.length > 0"
        label="Add Alternative URL"
        clearable
        :messages="messages"
      />
      <v-btn class="ml-4 primary" @click="addUrl">Add</v-btn>
    </v-layout>
  </v-container>
</template>

<script>
import FinalURLCheckbox from "@/fields/FinalURLCheckbox";

export default {
  components: {
    FinalURLCheckbox
  },
  computed: {
    messages() {
      if (this.errors.length == 0) {
        const msg =
          'Articles are accessible at any alternative URL associated with that article. All alternative URLs eventually resolve to whichever URL is marked "final".';
        return [msg];
      } else {
        return this.errors[0];
      }
    },
    urls() {
      return this.$store.state.obj.urls;
    }
  },
  data() {
    return {
      errors: [],
      newUrl: null
    };
  },
  methods: {
    addUrl() {
      this.clearErrors();
      const errors = this.validationErrors(this.newUrl);
      if (errors.length) {
        this.errors = errors;
      } else {
        let currentUrls = this.$store.state.obj.urls;
        currentUrls.push({
          final: false,
          value: this.newUrl
        });
        const payload = { field: "urls", value: currentUrls };
        this.$store.dispatch("obj/setFieldValue", payload);
        this.newUrl = null;
      }
    },
    clearErrors() {
      this.errors = [];
    },
    deleteUrl(index) {
      let urls = this.$store.state.obj.urls.filter((url, i) => i != index);
      const payload = { field: "urls", value: urls };
      this.$store.dispatch("obj/setFieldValue", payload);
    },
    validationErrors(url) {
      if (!url || url.length < 1) {
        return ["URL cannot be empty"];
      } else if (!url.startsWith("/") || !url.endsWith("/")) {
        return ['URL must start and end with a slash (eg "/my-article-url/")'];
      }
      return [];
    }
  }
};
</script>
