<template>
  <div class="d-flex flex-wrap" v-if="blockTypes.length">
    <v-card
      class="pa-2 mr-2 align-center d-flex flex-wrap justify-center align-center blockCard"
      v-for="blockType in blockTypes"
      :key="blockType.block_type"
      @click="() => addBlock(blockType)"
      outlined
      tile
    >
      <v-icon color="primary" large>{{ blockType.icon }}</v-icon>
      <div class="blockLabel">{{ blockType.label }}</div>
    </v-card>
  </div>
</template>

<script>
import { getBlockTypes } from "@/utils/blockTypes";

export default {
  computed: {
    blockTypes() {
      return getBlockTypes();
    }
  },
  methods: {
    addBlock(blockType) {
      this.$store.dispatch("obj/addNewBlock", blockType);
      const index = this.$store.state.obj.blocks.length - 1;
      this.$store.dispatch("editor/setActiveBlockIndex", index);
    }
  }
};
</script>

<style lang="scss" scoped>
.blockCard {
  width: 140px;
}
.blockLabel {
  width: 100%;
  text-align: center;
}
</style>
