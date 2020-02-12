<template>
  <v-dialog
    v-model="dialog"
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
  >
    <template v-slot:activator="{ on }">
      <v-btn class="ml-1 primary" text v-on="on">History</v-btn>
    </template>
    <v-card>
      <v-container>
        <v-card class="pa-2 my-4">
          <v-container>
            <v-layout row justify-space-between align-center>
              <h1 class="display-1">Edit History</h1>
              <v-btn class="primary" @click="closeDialog">Close</v-btn>
            </v-layout>
            <RevisionHistoryTable v-if="dialog" />
          </v-container>
        </v-card>
      </v-container>
    </v-card>
  </v-dialog>
</template>

<script>
import RevisionHistoryTable from "@/components/RevisionHistoryTable";

export default {
  components: {
    RevisionHistoryTable
  },
  computed: {
    dialog: {
      get() {
        return this.$store.state.editor.showRevisionDialog;
      },
      set(value) {
        this.$store.dispatch("editor/updateRevisionDialogStatus", value);
      }
    }
  },
  methods: {
    closeDialog() {
      this.dialog = false;
    }
  },
  name: "RevisionHistory"
};
</script>
