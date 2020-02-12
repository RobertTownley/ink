<template>
  <v-row>
    <v-col cols="12">
      <v-text-field v-model="header" label="Header" />
      <v-text-field
        v-model="anchor"
        label="Anchor Tag"
        hint="Anchor tag that will appear as a unique ID for the given section. Used to generate links to a specific part of a web page."
      />
    </v-col>
  </v-row>
</template>

<script>
import BaseBlock from "@/components/blocks/BaseBlock";

export default {
  computed: {
    header: {
      get() {
        return this.getValue("header");
      },
      set(header) {
        return this.setValue("header", header);
      }
    },
    anchor: {
      get() {
        return this.getValue("anchor");
      },
      set(anchor) {
        return this.setValue("anchor", anchor);
      }
    }
  },
  extends: BaseBlock,
  name: "SectionHeaderBlockEditor"
};
</script>
