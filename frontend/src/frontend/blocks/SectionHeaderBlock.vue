<template>
  <div>
    <div :id="anchor" class="display-1">{{ block.value.header }}</div>
  </div>
</template>

<script>
export default {
  computed: {
    anchor() {
      const { anchor } = this.block.value;
      return anchor ? anchor.replace(/\W/g, "") : "";
    }
  },
  name: "SectionHeaderBlock",
  props: ["block"]
};
</script>
