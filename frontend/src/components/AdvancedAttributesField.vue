<template>
  <div>
    <div class="title">Advanced Attributes</div>
    <p>
      Advanced attributes are object-specific customizations. Key/value pairings
      added here will be made available via API as-entered within the
      "advancedFields" field.
    </p>
    <v-simple-table v-if="advancedFields.length">
      <v-subheader>Advanced Entries</v-subheader>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">Key</th>
            <th class="text-left">Value</th>
            <th class="text-left">Delete</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(entry, index) in advancedFields" :key="index">
            <td>{{ entry.key }}</td>
            <td>{{ entry.value }}</td>
            <td>
              <v-btn text icon color="gray" @click="() => deleteValue(index)">
                <v-icon>mdi-delete</v-icon>
              </v-btn>
            </td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
    <v-layout class="d-flex align-baseline justify-space-between">
      <v-text-field v-model="newKey" label="Key" />
      <v-spacer />
      <v-text-field v-model="newValue" label="Value" />
      <v-spacer />
      <v-btn class="primary" @click="add">Add</v-btn>
    </v-layout>
  </div>
</template>

<script>
export default {
  computed: {
    advancedFields() {
      return this.$store.state.obj.advancedFields;
    }
  },
  data() {
    return {
      newKey: null,
      newValue: null
    };
  },
  methods: {
    add() {
      const { newKey, newValue } = this;
      if (!newKey) {
        this.keyError = "Required";
      } else if (!newValue) {
        this.valueError = "Required";
      } else {
        let value = this.$store.state.obj.advancedFields;
        value.push({ key: this.newKey, value: this.newValue });
        const payload = { field: "advancedFields", value };
        this.$store.dispatch("obj/setFieldValue", payload);
        this.clear();
      }
    },
    clear() {
      this.newKey = null;
      this.newValue = null;
    },
    deleteValue(index) {
      let value = Array.from(this.advancedFields);
      value.splice(index, 1);
      const payload = { field: "advancedFields", value };
      this.$store.dispatch("obj/setFieldValue", payload);
    }
  }
};
</script>
