<template>
  <div id="blogEntry" v-if="$store.state.frontend.obj.slug">
    <BlogDetailHeader />
    <v-container>
      <v-row>
        <v-col md="9" xs="12">
          <BlogContent />
        </v-col>
        <v-col md="3" xs="12">
          <BlogSidebar />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import BlogContent from "@/frontend/BlogContent";
import BlogDetailHeader from "@/frontend/BlogDetailHeader";
import BlogSidebar from "@/frontend/BlogSidebar";

export default {
  components: {
    BlogContent,
    BlogDetailHeader,
    BlogSidebar
  },
  mounted() {
    // Parsed twice to turn the string to a stringifed dict, and again into an obj
    const rawData = document.getElementById("object_data").textContent;
    this.$store.dispatch("frontend/setInitialObjectData", JSON.parse(rawData));
  }
};
</script>
