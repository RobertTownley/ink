<template>
  <v-container id="messageContainer">
    <Message
      v-for="(message, index) in messages"
      :key="index"
      :index="index"
      :message="message"
      :style="() => messageStyle(index)"
    />
  </v-container>
</template>

<script>
import Message from "@/components/Message";

export default {
  components: {
    Message
  },
  computed: {
    messages() {
      return this.$store.state.editor.messages;
    },
    messageStyle(index) {
      return `top: ${index * 50}px`;
    }
  }
};
</script>

<style lang="scss" scoped>
#messageContainer {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  margin: 0 auto;
  width: 100vw;
  text-align: center;
  z-index: 50;
}
</style>
