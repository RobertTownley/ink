<template>
  <v-dialog
    v-model="dialog"
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
  >
    <template v-slot:activator="{ on }">
      <v-btn v-on="on" outlined>Preview</v-btn>
    </template>
    <v-card>
      <v-container>
        <v-layout row justify-space-between align-center>
          <h1 class="display-1">Preview</h1>
          <v-btn @click="closeDialog" outlined>Close</v-btn>
        </v-layout>
      </v-container>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  computed: {
    dialog: {
      get() {
        return this.$store.state.editor.showPreviewDialog;
      },
      set(value) {
        this.$store.dispatch("editor/updatePreviewDialogStatus", value);
      }
    }
  },
  methods: {
    closeDialog() {
      this.dialog = false;
    }
  },
  name: "PreviewDialog"
};
</script>
