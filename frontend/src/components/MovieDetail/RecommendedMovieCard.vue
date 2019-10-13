<template>
  <v-card :to="{
    name: 'movie-detail',
    params: { movieId : movie.id }
    }"
    class="hoizontal-scroll-card mx-auto"
  >
    <figure class="effect-julia">
      <v-img 
        :src="movie.poster" 
        class="movie-thumb" 
        style="height: 450px; width: 100%;"
      >
        <figcaption>
          <p class="subtitle-2 font-weight-bold">RELEASE DATES :</p>
          <p class="caption"> {{ movie.released }}</p>
          <p class="subtitle-2 font-weight-bold">GENRE :</p>
          <p class="caption"> {{ movie.genres }}</p>
          <p class="subtitle-2 font-weight-bold">Rating :</p>
          <p class="caption"> {{ movie.imdbRating }}</p>
          <p class="subtitle-2 font-weight-bold">VIEW :</p>
          <p class="caption"> {{ movie.viewCnt }}</p>
        </figcaption>	
      </v-img>
    </figure>
    <v-card-text class="genres-text px-0 pb-0 pt-2">
      {{ movie.genres }}
    </v-card-text>
    <v-card-text class="title-text pt-2 px-0 pb-0">
      {{ movie.title }}
    </v-card-text>
  </v-card>
</template>

<script scoped>
export default {
  props: {
    movie: {
      type: Object,
      default: {}
    }
  },
  computed: {
    imageUrl() {
      return 'http://img.omdbapi.com/?apikey=556ed6ed&i='+ this.movie.imdbId
    }
  },
};
</script>

<style scoped>
.hoizontal-scroll-card {
	background-color: rgba(0, 0, 0, 0) !important;
  width: 300px;
  height: 500px;
}
.hoizontal-scroll-card .effect-julia .movie-thumb {
  width: 300px;
  height: 450px;
	background-image: url('../../../public/assets/no_poster.png');
	background-size: cover;
}
figure.effect-julia figcaption {
  height: 450px;
  width: 100%;
  padding: 2em 1em;
	text-align: left;
  background-color: rgba(0, 0, 0, 0);
  -webkit-transition: background-color 0.5s;
	transition: background-color 0.5s;
}

figure.effect-julia p {
	margin: 0 0 0.25em;
	padding: 0.4em 1em;
	color: white;
	text-transform: none;
	font-weight: 500;
	font-size: 75%;
	-webkit-transition: opacity 0.35s, -webkit-transform 0.35s;
	transition: opacity 0.35s, transform 0.35s;
	-webkit-transform: translate3d(-360px,0,0);
	transform: translate3d(-360px,0,0);
}

figure.effect-julia p:first-child,
figure.effect-julia:hover p:first-child {
	-webkit-transition-delay: 0.05s;
	transition-delay: 0.05s;
}

figure.effect-julia p:nth-of-type(2),
figure.effect-julia:hover p:nth-of-type(2) {
	-webkit-transition-delay: 0.05s;
	transition-delay: 0.05s;
}

figure.effect-julia p:nth-of-type(3),
figure.effect-julia:hover p:nth-of-type(3) {
	-webkit-transition-delay: 0.1s;
	transition-delay: 0.1s;
}

figure.effect-julia p:nth-of-type(4),
figure.effect-julia:hover p:nth-of-type(4) {
	-webkit-transition-delay: 0.1s;
	transition-delay: 0.1s;
}

figure.effect-julia p:nth-of-type(5),
figure.effect-julia:hover p:nth-of-type(5) {
	-webkit-transition-delay: 0.15s;
	transition-delay: 0.15s;
}
figure.effect-julia p:nth-of-type(6),
figure.effect-julia:hover p:nth-of-type(6) {
	-webkit-transition-delay: 0.15s;
	transition-delay: 0.15s;
}
figure.effect-julia p:nth-of-type(7),
figure.effect-julia:hover p:nth-of-type(7) {
	-webkit-transition-delay: 0.15s;
	transition-delay: 0.2s;
}
figure.effect-julia p:nth-of-type(8),
figure.effect-julia:hover p:nth-of-type(8) {
	-webkit-transition-delay: 0.15s;
	transition-delay: 0.25s;
}

figure.effect-julia:hover figcaption {
  height: 450px;
	background-color: rgba(0, 0, 0, 1);
}

figure.effect-julia:hover img {
	opacity: 0;
	-webkit-transform: scale3d(1.1,1.1,1);
	transform: scale3d(1.1,1.1,1);
}

figure.effect-julia:hover p {
	opacity: 1;
	-webkit-transform: translate3d(0,0,0);
	transform: translate3d(0,0,0);
}

.title-text {
  font-size: 1.25rem !important;
	color: white !important;
  font-weight: 500;
  letter-spacing: 0.0125em !important;
  line-height: 2.3rem;
	max-height: 2.3rem;
	text-align: left;
  overflow: hidden;
  text-overflow: ellipsis;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}
.genres-text {
  color: #8e8e8e !important;
  line-height: 2rem;
	max-height: 2rem;
	text-align: left;
  overflow: hidden;
  text-overflow: ellipsis;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}
</style>``