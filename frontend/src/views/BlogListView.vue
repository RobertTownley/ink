<template>
  <div>
    <BlogListHeader />
    <v-container>
      <v-row no-gutters>
        <v-col md="9" xs="12">
          <v-row no-gutters v-if="entries.length">
            <v-col
              cols="12"
              xs="6"
              md="4"
              v-for="entry in entries"
              :key="entry.slug"
            >
              <BlogEntryPreview :entry="entry" />
            </v-col>
          </v-row>
          <v-row v-else>
            <p>No blog entries to show</p>
          </v-row>
          <v-btn @click="loadMore" v-if="next" class="ml-2 mt-4" outlined text
            >Load More</v-btn
          >
        </v-col>
        <v-col md="3" xs="12">
          <BlogSidebar :class="sidebarClass" />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import BlogEntryPreview from "@/frontend/BlogEntryPreview";
import BlogSidebar from "@/frontend/BlogSidebar";
import BlogListHeader from "@/frontend/BlogListHeader";

export default {
  components: {
    BlogEntryPreview,
    BlogListHeader,
    BlogSidebar
  },
  computed: {
    entries() {
      return this.$store.state.frontend.entries;
    },
    sidebarClass() {
      return this.$vuetify.breakpoint.smAndDown ? "my-4" : "ml-2";
    }
  },
  data: () => ({
    next: null
  }),
  methods: {
    loadMore() {
      this.retrieveBlogEntries(this.next);
    }
  },
  mounted() {
    this.$store.dispatch("frontend/clearObjectData");
    this.$store.dispatch("frontend/setEntries", []);
    const payload = {
      params: this.$route.query,
      url: "/ink/api/v1/blogentries/"
    };
    this.$store.dispatch("frontend/retrieveEntries", payload);
  },
  name: "BlogListView"
};
</script>
