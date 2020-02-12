<template>
  <v-row>
    <v-col cols="12">
      <v-textarea v-model="quote" label="Quote" outlined />
      <v-text-field v-model="attribution" label="Attribution" />
    </v-col>
  </v-row>
</template>

<script>
import BaseBlock from "@/components/blocks/BaseBlock";

export default {
  computed: {
    attribution: {
      get() {
        return this.getValue("attribution");
      },
      set(attribution) {
        return this.setValue("attribution", attribution);
      }
    },
    quote: {
      get() {
        return this.getValue("quote");
      },
      set(quote) {
        return this.setValue("quote", quote);
      }
    }
  },
  extends: BaseBlock,
  name: "PullQuoteBlockEditor"
};
</script>
