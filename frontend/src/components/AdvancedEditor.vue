<template>
  <v-container>
    <TextField field="slug" label="Slug" />
    <PublicationDateField />
    <AdvancedAttributesField />
  </v-container>
</template>

<script>
import AdvancedAttributesField from "@/components/AdvancedAttributesField";
import PublicationDateField from "@/fields/PublicationDateField";
import TextField from "@/fields/TextField";

export default {
  components: {
    AdvancedAttributesField,
    PublicationDateField,
    TextField
  }
};
</script>
