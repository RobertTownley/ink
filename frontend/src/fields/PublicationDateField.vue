<template>
  <v-container class="py-0">
    <v-row align="center">
      <v-col cols="3" class="pl-0 pt-0">
        <v-menu
          ref="dateMenu"
          v-model="dateMenu"
          :close-on-content-click="false"
          :return-value.sync="date"
          transition="scale-transition"
          offset-y
        >
          <template v-slot:activator="{ on }">
            <v-text-field
              v-model="date"
              label="Publication Date"
              readonly
              v-on="on"
              dense
            ></v-text-field>
            <v-spacer />
          </template>
          <v-date-picker v-model="date" no-title scrollable>
            <v-btn text color="primary" @click="dateMenu = false">Cancel</v-btn>
            <v-btn text color="primary" @click="$refs.dateMenu.save(date)"
              >OK</v-btn
            >
          </v-date-picker>
        </v-menu>
      </v-col>
      <v-col cols="3" class="pl-0 pt-0">
        <v-menu
          ref="timeMenu"
          v-model="timeMenu"
          :close-on-content-click="false"
          :nudge-right="40"
          :return-value.sync="time"
          transition="scale-transition"
          offset-y
        >
          <template v-slot:activator="{ on }">
            <v-text-field
              v-model="time"
              label="Publication Time"
              readonly
              v-on="on"
              dense
            ></v-text-field>
          </template>
          <v-time-picker
            v-if="timeMenu"
            v-model="time"
            full-width
            @click:minute="$refs.timeMenu.save(time)"
          ></v-time-picker>
        </v-menu>
      </v-col>
      <v-col cols="6">
        <p class="caption">
          If no publication date or time are selected, the publication date will
          default to the date at which the content was first published.
          Publishing again will not automatically change the value.
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  computed: {
    datetime() {
      return this.$store.state.obj.publication_date;
    },
    date: {
      get() {
        return this.$store.state.obj.pub_date_str;
      },
      set(value) {
        const payload = { field: "pub_date_str", value };
        this.$store.dispatch("obj/setFieldValue", payload);
        this.setDateTime(value, this.time);
      }
    },
    time: {
      get() {
        return this.$store.state.obj.pub_time_str;
      },
      set(value) {
        const payload = { field: "pub_time_str", value };
        this.$store.dispatch("obj/setFieldValue", payload);
        this.setDateTime(this.date, value);
      }
    }
  },
  data: () => ({
    dateMenu: false,
    timeMenu: false
  }),
  methods: {
    setDateTime(date, time) {
      if (!date || !time) return;
    }
  }
};
</script>
