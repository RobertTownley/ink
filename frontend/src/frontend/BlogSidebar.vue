<template>
  <div class="sidebar">
    <BlogSidebarIntro />
    <BlogSidebarTags v-if="pageType == 'detail'" />
    <ReturnToBlogButton v-if="pageType == 'detail'" />
    <TopicsList v-if="pageType == 'list'" />
  </div>
</template>

<script>
import BlogSidebarIntro from "@/frontend/BlogSidebarIntro";
import BlogSidebarTags from "@/frontend/BlogSidebarTags";
import ReturnToBlogButton from "@/frontend/ReturnToBlogButton";
import TopicsList from "@/frontend/TopicsList";

export default {
  components: {
    BlogSidebarIntro,
    BlogSidebarTags,
    ReturnToBlogButton,
    TopicsList
  },
  computed: {
    pageType() {
      return this.$route.path == "/blog/" ? "list" : "detail";
    }
  },
  name: "BlogSidebar"
};
</script>

<style lang="scss" scoped>
.sidebar {
  position: sticky;
  top: 16px;
}
</style>
