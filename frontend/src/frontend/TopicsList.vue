<template>
  <div>
    <h2 class="title mb-2">Filter Posts By Topic</h2>
    <v-chip
      v-for="topic in site_sections"
      :key="topic.id"
      @click="() => filterByTopic(topic)"
      class="mb-2 mr-2 topic"
    >
      {{ topic.name }}
    </v-chip>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    site_sections: []
  }),
  methods: {
    getTopics() {
      axios({
        method: "GET",
        url: "/ink/api/v1/site_sections/"
      }).then(response => {
        this.site_sections = response.data;
      });
    },
    filterByTopic(topic) {
      const newUrl = this.$route.path + `?topic=${topic.id}`;
      this.$router.push(newUrl);
      window.location.reload();
    }
  },
  mounted() {
    this.getTopics();
  },
  name: "TopicsList"
};
</script>

<style lang="scss" scoped></style>
