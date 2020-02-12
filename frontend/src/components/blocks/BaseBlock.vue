<script>
// Parent class of other blocks. Used for store-interactive utility methods
export default {
  methods: {
    getValue(fieldName) {
      return this.block.value[fieldName];
    },
    setValue(fieldName, fieldValue) {
      let value = this.block.value;
      value[fieldName] = fieldValue;
      if (this.lead) {
        this.$store.dispatch("obj/editLeadBlockValue", value);
      } else {
        const payload = { index: this.index, value };
        this.$store.dispatch("obj/editBlockValue", payload);
      }
    }
  },
  props: ["block", "index", "lead"]
};
</script>
