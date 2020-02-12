<template>
  <v-checkbox v-model="value" />
</template>

<script>
export default {
  computed: {
    value: {
      get() {
        return this.url.final;
      },
      set() {
        let currentUrls = this.$store.state.obj.urls.map((url, i) => {
          url.final = i == this.index;
          return url;
        });
        const payload = { field: "urls", value: currentUrls };
        this.$store.dispatch("obj/setFieldValue", payload);
      }
    }
  },
  props: ["index", "url"]
};
</script>
