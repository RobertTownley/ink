<template>
  <v-row>
    <v-col class="d-flex justify-end">
      <v-img :src="image.thumbnail" />
    </v-col>
  </v-row>
</template>

<script>
export default {
  props: ["image"]
};
</script>
