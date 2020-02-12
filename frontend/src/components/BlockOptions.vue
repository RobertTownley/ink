<template>
  <v-row>
    <v-col class="d-flex justify-end">
      <v-btn class="green ml-2" dark @click="save">Save</v-btn>
      <v-btn class="red ml-2" dark @click="removeBlock">Delete Block</v-btn>
    </v-col>
  </v-row>
</template>

<script>
export default {
  methods: {
    removeBlock() {
      this.$store.dispatch("obj/removeBlock", this.index);
      const { length } = this.$store.state.obj.blocks;
      const index = length > this.index ? this.index : length - 1;
      this.$store.dispatch("editor/setActiveBlockIndex", index);
    },
    save() {
      this.$store.dispatch("editor/save");
    }
  },
  props: ["block", "index"]
};
</script>
