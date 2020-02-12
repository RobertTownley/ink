<template>
  <v-select
    v-model="site_section"
    :items="site_sections"
    label="Site Section"
    v-if="site_sections.length"
    item-text="name"
    item-value="id"
    clearable
    dense
  >
  </v-select>
</template>

<script>
import axios from "axios";

export default {
  computed: {
    site_section: {
      get() {
        return this.$store.state.obj.site_section;
      },
      set(value) {
        const payload = { field: "site_section", value };
        this.$store.dispatch("obj/setFieldValue", payload);
      }
    }
  },
  data() {
    return {
      site_sections: []
    };
  },
  mounted() {
    axios({
      method: "GET",
      url: `/ink/api/v1/site_sections/`
    }).then(response => {
      this.site_sections = response.data;
    });
  }
};
</script>
