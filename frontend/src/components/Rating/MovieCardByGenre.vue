<template>
	<div>
		<v-card
			class="movie-card text-left white--text mx-auto"
		>
			<figure class="effect-julia">
				<v-img 
					:src="movie.poster" 
					@click="goToWithParams('movie-detail', movie.id )"
					class="thumb pointer" 
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
			<v-card-text 
				@click="goToWithParams('movie-detail', movie.id )"
				class="title-text pointer pt-2 px-0 pb-0 white--text"
			>
				{{ movie.title }}
			</v-card-text>
		</v-card>
		<div class="mx-auto rating-center">
			<div @click="leaveRating">
				<v-rating
					v-model=userRating
					color="yellow darken-3"
					background-color="grey darken-1"
					half-increments
					hover
					dense
					class="rating-grid"
				/>
			</div>
			<v-btn 
				v-if="userRating > 0"
				@click="cancelRating"
				class="ml-5 pa-0"
				style="height: 24px; background-color: #f9a825;"
			>
				Reset
			</v-btn>
		</div>
	</div>
</template>

<script>
import { mapMutations } from "vuex";
import router from "../../router";

export default {
  props: {
    movie: {
      type: Object,
      default: {}
    }
	},
	data() {
		return {
			userRating: 0
		}
	},
  computed: {
    imageUrl() {
      return 'http://img.omdbapi.com/?apikey=556ed6ed&i='+ this.movie.imdbId
		},
	},
	methods: {
		...mapMutations("rating", ["collectRating"]),
		...mapMutations("rating", ["deleteCollectedRating"]),
		...mapMutations("rating", ["countCollectedRating"]),
		goToWithParams: function(path, params) {
			router.push({ name: path, params:{ movieId: params} });
    },
		leaveRating() {
			this.collectRating([this.movie.id, this.userRating]);
			this.countCollectedRating();
		},
		cancelRating() {
			this.deleteCollectedRating(this.movie.id);
			this.userRating = 0;
			this.countCollectedRating();
		}
	}
};
</script>

<style scoped>
.pointer {
  cursor: pointer;
}

.movie-card {
  background-color: rgba(0, 0, 0, 0) !important; 
  width: 350px !important; 
  height: 550px !important;
}
.rating-grid {
	width: auto;
	height: 100%;
}
.thumb {
  background-image: url('../../../public/assets/no_poster.png');
}
.v-rating--dense .v-icon {
  padding: 0.5px !important;
}

.rating-center {
	display: flex;
	width: 350px !important;
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
  font-weight: 500;
  line-height: 2rem;
  letter-spacing: 0.0125em !important;

  text-align: left;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-inline-box;
  line-height: 1.5rem;
  max-height: 4rem;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.genres-text {
  color: #8e8e8e !important;
}
</style>``