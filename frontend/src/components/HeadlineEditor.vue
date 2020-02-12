<template>
  <v-card class="pa-4">
    <TextField field="title" label="Title" />
    <TextField field="subtitle" label="Subtitle" />
    <SiteSectionField />
    <BylineField />
  </v-card>
</template>

<script>
import BylineField from "@/fields/BylineField";
import SiteSectionField from "@/fields/SiteSectionField";

import TextField from "@/fields/TextField";

export default {
  components: {
    BylineField,
    SiteSectionField,
    TextField
  }
};
</script>
