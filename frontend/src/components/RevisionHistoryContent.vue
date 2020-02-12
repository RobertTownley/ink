<template>
  <v-expansion-panel-content>
    <v-treeview :items="tree" />
    <div v-if="showConfirmation">
      <p class="warning pa-4 d-flex">
        Are you sure you want to revert to this previous version? This will
        create a new reversion, and can be undone at any time. The content
        object will need to be republished before the reversion will take
        effect.
        <v-btn @click="revert" class="primary ma-2">Confirm Reversion</v-btn>
      </p>
    </div>
    <v-btn v-else @click="confirmRevert" class="primary ma-4">Revert</v-btn>
  </v-expansion-panel-content>
</template>

<script>
function getNameForEntry(entry) {
  const [name, value] = entry;
  if (!value) {
    return `${name}: None`;
  } else if (typeof value == "object") {
    return `${name}: `;
  } else {
    return `${name}: ${value}`;
  }
}

function getChildrenForEntry(entry) {
  const value = entry[1];
  if (!value || typeof value != "object") return [];
  if (value.length > -1) {
    // Array
    return value.map((subValue, index) => {
      const name = `${index.toString()}:`;
      const children = getChildrenForEntry([index, subValue]);
      return { name, children };
    });
  } else {
    // Object
    return Object.entries(value).map(subEntry => {
      const children = getChildrenForEntry(subEntry);
      const name = getNameForEntry(subEntry);
      return { name, children };
    });
  }
}
export default {
  computed: {
    tree() {
      return Object.entries(this.revision.data).map(entry => {
        const children = getChildrenForEntry(entry);
        const name = getNameForEntry(entry);
        return { name, children };
      });
    }
  },
  data() {
    return {
      showConfirmation: false
    };
  },
  methods: {
    confirmRevert() {
      this.showConfirmation = true;
    },
    revert() {
      this.showConfirmation = false;
      this.$store.dispatch("editor/revertToPriorVersion", this.revision.id);
    }
  },
  props: ["revision"]
};
</script>
