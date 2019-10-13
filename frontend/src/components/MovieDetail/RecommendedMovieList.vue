<template>
	<div class="horizontal-scroll-wrapper1">
		<div class="horizontal-scroll-wrapper2">
      <v-flex
        v-for="i in movieListCards.length" 
        :key="i"
        class="hoizontal-scroll-flex"
      >
        <RecommendedMovieCard 
          :movie="movieListCards[i-1]"  
        />
      </v-flex>
		</div>
	</div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import RecommendedMovieCard from "./RecommendedMovieCard";

export default {
  components: {
    RecommendedMovieCard
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
    ...mapActions("random", ["getRandomMovie"]),
  },
}
</script>

<style scoped>
.horizontal-scroll-wrapper1 {
  width: 65vh;
  height: 100vw;
  position: absolute;
  overflow-y: scroll;
  overflow-x: hidden;
  transform: rotate(270deg) translateX(-100%);
  transform-origin: top left;
}
.horizontal-scroll-wrapper2 {
  position: absolute;
  transform: rotate(90deg) translateY(-100%);
  transform-origin: top left;
  white-space: nowrap;
}
.hoizontal-scroll-flex {
  display: inline-block;
  width: 300px;
  height: 600px;
	margin: 0 10px 0 10px;
}

@media (min-width: 960px) {
  .horizontal-scroll-wrapper1 {
    height: 65vw;
  }
} 
</style>