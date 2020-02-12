<template>
  <v-row v-if="$store.state.obj.id">
    <v-col cols="8">
      <v-row v-if="!loading">
        <v-col class="d-flex justify-space-between align-center pa-0">
          <v-file-input
            v-model="imageFile"
            :label="label"
            @change="handleFileUpload"
            accept="image/*"
            dense
          />
          <v-btn
            v-if="hasImage"
            @click="clear"
            class="ml-4"
            color="primary"
            outlined
            >Clear</v-btn
          >
        </v-col>
      </v-row>
      <LoadingMessage v-else msg="Uploading image..." />
      <v-text-field v-model="alt_text" label="Alternative Text" dense />
      <v-text-field v-model="attribution" label="Attribution" dense />
      <v-text-field v-model="caption" label="Caption" dense />
    </v-col>
    <v-col cols="4">
      <ImagePreview :image="block.value.image" v-if="hasImage && !loading" />
    </v-col>
  </v-row>
  <UnsavedImageMessage v-else />
</template>

<script>
import axios from "axios";

import { getHeaders } from "@/utils/auth";
import BaseBlock from "@/components/blocks/BaseBlock";
import ImagePreview from "@/components/ImagePreview";
import LoadingMessage from "@/components/LoadingMessage";
import UnsavedImageMessage from "@/components/UnsavedImageMessage";
import { buildImageData } from "@/utils/images";

export default {
  components: {
    ImagePreview,
    LoadingMessage,
    UnsavedImageMessage
  },
  computed: {
    alt_text: {
      get() {
        return this.getValue("alt_text");
      },
      set(alt_text) {
        this.setValue("alt_text", alt_text);
      }
    },
    attribution: {
      get() {
        return this.getValue("attribution");
      },
      set(attribution) {
        this.setValue("attribution", attribution);
      }
    },
    caption: {
      get() {
        return this.getValue("caption");
      },
      set(caption) {
        this.setValue("caption", caption);
      }
    },
    hasImage() {
      const { value } = this.block;
      return value && value.image && value.image.filename ? true : false;
    },
    label() {
      return this.hasImage ? "Change Image" : "Add Image";
    }
  },
  data() {
    return {
      loading: false,
      imageFile: null
    };
  },
  methods: {
    clear() {
      let { value } = this.block;
      value.image = {};
      if (this.lead) {
        this.$store.dispatch("obj/editLeadBlockValue", value);
      } else {
        const payload = { index: this.index, value };
        this.$store.dispatch("obj/editBlockValue", payload);
      }
      this.imageFile = null;
    },
    handleFileUpload(value) {
      this.loading = true;
      let headers = getHeaders();
      headers["Content-Type"] = "multipart/form-data";
      axios({
        data: buildImageData(value),
        headers,
        method: "POST",
        url: "/ink/image_upload/"
      })
        .then(response => {
          let { value } = this.block;
          value.image = response.data;
          if (this.lead) {
            this.$store.dispatch("obj/editLeadBlockValue", value);
          } else {
            const payload = { index: this.index, value };
            this.$store.dispatch("obj/editBlockValue", payload);
          }
        })
        .catch(error => {
          return error;
        })
        .finally(() => {
          this.loading = false;
          this.imageFile = null;
        });
    }
  },
  extends: BaseBlock,

  name: "ImageBlockEditor"
};
</script>
