<template>
  <div class="pa-2">
    <div class="title font-italic mb-2">
      <v-icon>mdi-format-quote-open</v-icon>{{ quote
      }}<v-icon>mdi-format-quote-close</v-icon>
      <span v-if="attribution" class="caption pl-2">―{{ attribution }}</span>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    attribution() {
      return this.block.value.attribution;
    },
    quote() {
      return this.block.value.quote;
    }
  },
  name: "PullQuoteBlock",
  props: ["block"]
};
</script>
