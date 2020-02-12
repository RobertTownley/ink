<template>
  <v-card class="pa-4 mt-4">
    <v-layout class="d-flex justify-space-between align-center">
      <div class="title">Lead Content</div>
      <v-chip-group active-class="primary--text" v-model="activeChip" mandatory>
        <v-chip v-for="blockModel in blockModels" :key="blockModel.block_type">
          {{ blockModel.label }}</v-chip
        >
      </v-chip-group>
    </v-layout>
    <LeadBlock />
  </v-card>
</template>

<script>
import { getBlockTypes } from "@/utils/blockTypes";
import LeadBlock from "@/components/LeadBlock";

export default {
  components: {
    LeadBlock
  },
  computed: {
    blockModels() {
      return [{ label: "None", block_type: "none" }].concat(
        getBlockTypes()
          .filter(b => b.can_lead === true)
          .sort((a, b) => a.lead_order > b.lead_order)
      );
    },
    activeChip: {
      get() {
        const { block_type } = this.$store.state.obj.lead_block;
        return this.blockModels.findIndex(b => b.block_type == block_type);
      },
      set(index) {
        let block = {};
        if (index != 0) {
          const blockModel = this.blockModels[index];
          block = JSON.parse(
            JSON.stringify({
              block_type: blockModel.block_type,
              value: blockModel.default_value
            })
          );
        }
        const payload = { field: "lead_block", value: block };
        this.$store.dispatch("obj/setFieldValue", payload);
      }
    }
  }
};
</script>
