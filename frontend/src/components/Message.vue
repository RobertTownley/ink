<template>
  <v-alert :type="message.type" dismissible>{{ message.content }} </v-alert>
</template>

<script>
export default {
  mounted() {
    if (!this.message.persist) {
      const { dispatch } = this.$store;
      setTimeout(function() {
        dispatch("editor/updateFormMessages", []);
      }, 4000);
    }
  },
  name: "Message",
  props: ["message"]
};
</script>
