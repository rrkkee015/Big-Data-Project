<template>
  <v-col cols="12" sm="4" md="6" class="pt-0">
    <v-row class="pt-3 detail-text">
      <v-col data-aos="fade-left" data-aos-once="true" data-aos-duration="1000" data-aos-delay="1200" cols="6" class="pb-0">
        RATING
      </v-col>
      <v-col data-aos="fade-left" data-aos-once="true" data-aos-duration="1000" data-aos-delay="1400" cols="6" class="pb-0">
        RUNTIME
      </v-col>
    </v-row>
    <v-row class="detail-text-content">
      <v-col data-aos="fade-left" data-aos-once="true" data-aos-duration="1000" data-aos-delay="1200" cols="6" class="py-0">
        <v-rating
          :value="rating"
          color="yellow darken-3"
          background-color="grey darken-1"
          half-increments
          dense
          readonly
          small
        />
      </v-col>
      <v-col data-aos="fade-left" data-aos-once="true" data-aos-duration="1000" data-aos-delay="1400" cols="6" class="py-0">
        {{ movie.runtime }}min
      </v-col>
    </v-row>
    <v-row class="detail-text">
      <v-col data-aos="fade-left" data-aos-once="true" data-aos-duration="1000" data-aos-delay="1600" class="pb-0">
        GENRE
      </v-col>
      <v-col data-aos="fade-left" data-aos-once="true" data-aos-duration="1000" data-aos-delay="1800" class="pb-0">
        RELEASE DATES
      </v-col>
    </v-row>
    <v-row class="detail-text-content">
      <v-col data-aos="fade-left" data-aos-once="true" data-aos-duration="1000" data-aos-delay="1600" class="py-0" cols="6">
        {{ movie.genres }}
      </v-col>
      <v-col data-aos="fade-left" data-aos-once="true" data-aos-duration="1000" data-aos-delay="1800" class="py-0" cols="6">
        {{ movie.released}}
      </v-col>
    </v-row>
    <v-row class="detail-text">
      <v-col data-aos="fade-left" data-aos-once="true" data-aos-duration="1000" data-aos-delay="2000" class="pb-0">
        CAST
      </v-col>
      <v-col data-aos="fade-left" data-aos-once="true" data-aos-duration="1000" data-aos-delay="2200" class="pb-0">
        DIRECTOR & WRITER
      </v-col>
    </v-row>
    <v-row class="detail-text-content">
      <v-col data-aos="fade-left" data-aos-once="true" data-aos-duration="1000" data-aos-delay="2000" class="py-0" cols="6">
        {{ movie.cast }}
      </v-col>
      <v-col data-aos="fade-left" data-aos-once="true" data-aos-duration="1000" data-aos-delay="2200" class="py-0" cols="6">
        <v-col class="pa-0" cols="12">
          {{ movie.director}}
        </v-col>
        <v-col class="pa-0" cols="12">
          {{ movie.writer }}
        </v-col>
      </v-col>
    </v-row>
    <v-row class="detail-text">
      <v-col data-aos="fade-left" data-aos-once="true" data-aos-duration="1000" data-aos-delay="2400" class="pb-0">
        view
      </v-col>
    </v-row>
    <v-row class="detail-text-content">
      <v-col data-aos="fade-left" data-aos-once="true" data-aos-duration="1000" data-aos-delay="2600" class="py-0">
        {{ movie.viewCnt }}
      </v-col>
    </v-row>
  </v-col>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters("data", {
      movie: "getMovie"
    }),
    rating() {
      return Number(this.movie.imdbRating)
    }
  },
  async created() {
    await this.searchMovie(this.$route.params.movieId)
  },
  methods: {
    ...mapActions("data", ["searchMovie"])
  },
};
</script>

<style scoped>
.detail-text {
  font-size: 1rem !important;
  color: #8e8e8e;
}

.detail-text-content {
  font-size: 1rem !important;
}
</style>