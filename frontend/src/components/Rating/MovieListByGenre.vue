<template>
  <v-layout 
    mt-5 
    wrap
  >
    <v-flex
      v-for="idx in movieListCards.length > limits ? limits : movieListCards.length"
      :key="idx"
      pa-2 
      xs12 md6 lg4
    >
      <MovieCardByGenre
        :movie="movieListCards[idx-1]"
        class="pa-3 mb-12"
      />
    </v-flex>
    <v-flex 
      v-show="this.limits < movieListCards.length"
      xs12
      class="text-center py-12"  
    >
      <v-btn class="button-more" tile icon style="border: 0px !important"  @click="loadMoreMovies" color="white" outlined><i class="fas fa-angle-double-down" style="font-size:16px"/></v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
/* eslint-disable */
import { mapState, mapActions } from "vuex";
import MovieCardByGenre from "./MovieCardByGenre"

export default {
  components: {
    MovieCardByGenre
  },
  data() {
    return {
      limits: 9,
      loadMore: false
    }
  },
  computed: {
		...mapState ({
      movieListCards: state => state.random.movieRandomList
    })
	},
	mounted() {
    this.getRandomMovie()
  },
	methods: {
    ...mapActions("random", ['getRandomMovie']),
    loadMoreMovies() {
      this.limits += 9;
    }
  }
}
</script>

<style scoped>
.button-more:hover {
  transform: translateY(10px);
}
</style>