<template>
  <v-row>
    <v-col cols="6">
      <v-select v-model="language" :items="languages" filled label="Language">
      </v-select>
      <v-textarea v-model="code" outlined />
    </v-col>
    <v-col cols="6" v-if="code && code.length">
      <CodePreview :code="code" :language="language" />
    </v-col>
  </v-row>
</template>

<script>
import BaseBlock from "@/components/blocks/BaseBlock";
import CodePreview from "@/components/CodePreview";

export default {
  components: {
    CodePreview
  },
  computed: {
    language: {
      get() {
        return this.getValue("language");
      },
      set(language) {
        return this.setValue("language", language);
      }
    },
    code: {
      get() {
        return this.getValue("code");
      },
      set(code) {
        this.setValue("code", code);
      }
    }
  },
  data() {
    return {
      languages: [
        "Bash",
        "C",
        "C++",
        "HTML",
        "Java",
        "Javascript",
        "Perl",
        "Python",
        "Ruby",
        "Rust",
        "XML"
      ]
    };
  },
  extends: BaseBlock
};
</script>
