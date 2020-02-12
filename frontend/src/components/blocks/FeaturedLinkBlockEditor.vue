<template>
  <v-row>
    <v-col cols="12">
      <v-textarea v-model="text" label="Link Text" outlined />
      <v-text-field v-model="href" label="Destination" />
      <v-checkbox v-model="target" label="Open link in new window?" />
    </v-col>
  </v-row>
</template>

<script>
import BaseBlock from "@/components/blocks/BaseBlock";

export default {
  computed: {
    href: {
      get() {
        return this.getValue("href");
      },
      set(value) {
        this.setValue("href", value);
      }
    },
    target: {
      get() {
        return this.getValue("target") == "_blank" ? true : false;
      },
      set(newWindow) {
        const value = newWindow == true ? "_blank" : "";
        return this.setValue("target", value);
      }
    },
    text: {
      get() {
        return this.getValue("text");
      },
      set(value) {
        this.setValue("text", value);
      }
    }
  },
  extends: BaseBlock
};
</script>
