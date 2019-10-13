<template>
  <v-container>
    <ScrollToTop />
		<v-btn
			v-if="ratingCnt < 7"
			disabled
      data-aos="fade-up" data-aos-once="true" data-aos-duration="1500"
			class="fixed-right-bottom"
			style="background-color: grey !important; color: white !important;"
		>
			{{ ratingCnt }} / 7
		</v-btn>
		<v-btn 
			v-else
      @click="setRating"
			class="fixed-right-bottom"
      color="success"
		>
			{{ ratingCnt }} / 7
		</v-btn>
		<v-row class="justify-center mt-12">
			<v-flex
				sm9
			>
				<div 
					data-aos="fade-in" 
					data-aos-once="true" 
					data-aos-duration="1500" 
					data-aos-delay="600"
					class="neon"
				>
					<p>P<span>lease leave</span> ratings <span>on</span> the mo<span>vi</span>e you saw.</p>
				</div>
			</v-flex>
			<v-flex	
				sm9 
				style="max-width: 936px;"
			>
				<MovieListByGenre
         data-aos="fade-up" data-aos-once="true" data-aos-duration="1500" data-aos-delay="1000"
        />
			</v-flex>
		</v-row>
  </v-container>
</template>

<script>
import { mapState, mapGetters, mapMutations, mapActions } from "vuex";
import ScrollToTop from "../components/Common/ScrollToTop"
import MovieListByGenre from "../components/Rating/MovieListByGenre"

export default {
  components: {
		ScrollToTop,
		MovieListByGenre,
  },
	computed: {
		...mapState ({
      newRatings: state => state.rating.newRatings
		}),
		...mapState ({
			ratingCnt: state => state.rating.ratingCnt
    }),
    ...mapState ("profiles", ["singleProfile"]),
    ...mapGetters("rating", {
      newRatings: "newRatings"
    }),
  },
  created() {
    this.checkNavBar(true)
    this.toggleProfileSnackBar(false)
  },
  methods: {
    ...mapActions("rating", ["setRatings"]),
    ...mapActions("profiles", ["getSingleProfile"]),
    ...mapMutations("rating", ["initRatingCnt"]),
    ...mapMutations("entrance", ["toggleProfileSnackBar"]),
    ...mapMutations("entrance", ["checkNavBar"]),
    setRating() {
      this.setRatings(this.newRatings)
    }
  },
  async beforeRouteLeave(to, from, next) {
    var nickname = await this.$store.state.auth.profile.nickname
    await this.$store.dispatch('profiles/getSingleProfile', nickname)
    var ratingsLength = await this.$store.state.profiles.ratingsLength
    if (ratingsLength < 7) {
      console.log('Please pick the seven movies')
    } else {
      this.initRatingCnt()
      next()
    }
  }
}
</script>

<style scoped>
.fixed-right-bottom {
	position: fixed;
	right: 100px;
	bottom: 25px;
	z-index: 2;
}
.disable {
	background-color: grey !important; 
	color: white !important;
}
.neon-box-main {
  width: 100%;
  box-shadow: -1px -6px 20px 20px black inset;
}

@import url(//fonts.googleapis.com/css?family=Vibur);

.neon {
	display: flex;
	align-items: center; 
	justify-content: center;
  text-align: center;
  height: 250px;
  background: #112 url(//images.weserv.nl/?url=i.imgur.com/6QJjYMe.jpg) center;
  background-size: contain;
  border-radius: 50px;
  box-shadow: 0px 0px 20px 20px black inset;
}
.neon p{
  font: 400 55px "Vibur";
  color: #fee;
  text-shadow: 
    0 -40px 100px, 
    0 0 2px, 
    0 0 1em #ff4444, 
    0 0 0.5em #ff4444, 
    0 0 0.1em #ff4444, 
    0 10px 3px #000;
}
.neon p span{
  animation: blink linear infinite 2s;
}
.neon p span:nth-of-type(2){
  animation: blink linear infinite 4s;
}
.neon p span:nth-of-type(3){
  animation: blink linear infinite 3s;
}
@keyframes blink {
  78% {
    color: inherit;
    text-shadow: inherit;
  }
  79%{
     color: #333;
  }
  80% {
    
    text-shadow: none;
  }
  81% {
    color: inherit;
    text-shadow: inherit;
  }
  82% {
    color: #333;
    text-shadow: none;
  }
  83% {
    color: inherit;
    text-shadow: inherit;
  }
  92% {
    color: #333;
    text-shadow: none;
  }
  92.5% {
    color: inherit;
    text-shadow: inherit;
  }
}
</style>