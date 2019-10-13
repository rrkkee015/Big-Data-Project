<template>
  <v-layout
    wrap
  >
    <!-- <v-flex>
      {{ ratedMovies}}
    </v-flex> -->
    <v-flex 
      v-for="(ratedMovie, i) in ratedMovies" 
      :key="i" 
      data-aos="fade-up" 
      data-aos-once="true" 
      data-aos-duration="1000"
      px-4 pb-5 xs12 lg6
      class="movie-card-center"
    > 
      <RatedMovieCard 
        :ratedMovie="ratedMovie"
      />
    </v-flex>
  </v-layout>  
</template>

<script>
import RatedMovieCard from "./RatedMovieCard"
import { mapState, mapGetters } from 'vuex'

export default {
  components: {
    RatedMovieCard
  },
  computed: {
    ...mapGetters("profiles", { 
      ratedMovies: 'ratings'
    })
  }
}
</script>

<style scoped>
@media (max-width: 960px) {
  .movie-card-center {
    justify-content: center;
    display: flex;
  }
}
</style>
