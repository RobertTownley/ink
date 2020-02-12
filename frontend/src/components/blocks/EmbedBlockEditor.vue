<template>
  <v-row>
    <v-col cols="6">
      <v-textarea label="Embed code" v-model="embedCode" outlined />
    </v-col>
    <v-col cols="6" v-if="hasValue" v-html="embedCode"> </v-col>
  </v-row>
</template>

<script>
import BaseBlock from "@/components/blocks/BaseBlock";

export default {
  computed: {
    embedCode: {
      get() {
        return this.getValue("embedCode");
      },
      set(embedCode) {
        return this.setValue("embedCode", embedCode);
      }
    },
    hasValue() {
      return this.block.value ? true : false;
    }
  },
  extends: BaseBlock,
  name: "EmbedBlockEditor"
};
</script>
