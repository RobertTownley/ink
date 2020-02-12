<template>
  <v-expansion-panels :value="panel">
    <div v-if="!revisions.length">
      <p>No revision history found</p>
    </div>
    <v-expansion-panel v-for="revision in revisions" :key="revision.id">
      <RevisionHistoryPreview :revision="revision" />
      <RevisionHistoryContent :revision="revision" />
    </v-expansion-panel>
    <v-btn v-if="next" @click="loadMore" class="primary my-4">See More</v-btn>
  </v-expansion-panels>
</template>

<script>
import axios from "axios";
import RevisionHistoryContent from "@/components/RevisionHistoryContent";
import RevisionHistoryPreview from "@/components/RevisionHistoryPreview";

export default {
  components: {
    RevisionHistoryContent,
    RevisionHistoryPreview
  },
  data() {
    return {
      next: null,
      panel: null,
      revisions: []
    };
  },
  methods: {
    getRevisions(url) {
      let params = {};
      if (!url) {
        url = "/ink/api/v1/revisions/";
        const { id, modelName, appName } = this.$route.params;
        params = {
          appName,
          id,
          modelName
        };
      }

      axios({
        method: "GET",
        url,
        params
      })
        .then(response => {
          const { next, results } = response.data;
          this.revisions = this.revisions.concat(results);
          this.next = next;
        })
        .catch(error => {
          // TODO: Add error handling
          return error;
        });
    },
    loadMore() {
      this.getRevisions(this.next);
    }
  },
  mounted() {
    this.getRevisions(this.next);
  },
  name: "RevisionHistoryTable"
};
</script>
