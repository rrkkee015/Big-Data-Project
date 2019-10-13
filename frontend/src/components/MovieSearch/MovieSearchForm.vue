<template>
  <div>
    <v-row data-aos="fade-up" data-aos-once="true" data-aos-duration="1500">
      <v-text-field dark v-model="title" label="Movie Title" @keyup.enter="onSubmit" autocomplete="off"/>
    </v-row>
    <v-row class="pt-5" style="display: flex; justify-content: center;">
      <v-btn color="#5e5e5e" data-aos="fade-up" data-aos-once="true" data-aos-duration="1500" data-aos-delay="400" style="color:white" text @click="onSubmit">SEARCH</v-btn>
    </v-row>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data() {
    return {
      title: "",
    }
  },
  methods: {
    ...mapActions("data", ["searchMovies"]),
    onSubmit: function() {
      if (this.title.trim()) {
        const params = {
          search: this.title,
        };
        this.searchMovies(params);
      }
    }
  }
};
</script>

<style scoped>
</style>