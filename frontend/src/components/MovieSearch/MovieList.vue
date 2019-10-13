<template>
  <v-layout mt-5 wrap>
    <v-flex 
      v-for="(movie, idx) in movieList" 
      :key="idx" 
      pa-2 xs12 md6 lg4> 
      <MovieListCard
        :movie="movie"
        class="pa-3"
      />
    </v-flex>
    <v-flex 
      v-show="nextUrl"
      xs12 
      text-xs-center 
      round 
      my-5
    > 
      <v-btn 
        @click="loadMoreMovies" 
        tile 
        icon 
        color="white" 
        outlined
        class="button-more" 
        style="border: 0px !important" 
      >
        <i class="fas fa-angle-double-down" style="font-size:16px"/>
      </v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapState, mapGetters, mapActions } from "vuex";
import MovieListCard from "../Common/MovieListCard";

export default {
  components: {
    MovieListCard,
  },
  computed: {
    ...mapState("data",{ movieList: "movieSearchList" }),
    ...mapGetters('data', {
      nextUrl: 'getNextUrl'
    }),
    // pagination related variables 
    movieListEmpty: function() {
      return this.movieList.length === 0;
    },
  },
  methods: {
    ...mapActions("data", ["searchNextMovies"]),
    loadMoreMovies() {
      this.searchNextMovies()
    }
  },
}
</script>

<style scoped>
.button-more:hover {
  transform: translateY(10px);
}
</style>