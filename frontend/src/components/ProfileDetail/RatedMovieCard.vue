<template>
<div class="pa-0">
  <v-card 
    class="rated-movie-card white--text"
    style="background-color: rgba(0, 0, 0, 0);"
  >
    <v-card-title class="cut-text pl-0">
      {{ ratedMovie.movie.title }}
    </v-card-title>
    <v-img
      :src="ratedMovie.movie.poster"
      @click="goToWithParams('movie-detail', ratedMovie.movie.id )"
      class="rated-movie-img thumb"
    >
    </v-img>
    <v-card-text>
      <div
        v-if="host === user.nickname"
        @click="dialog = true"
        class="mb-0">
        <v-rating
          v-model=modifiedRating
          color="yellow darken-3"
          background-color="grey darken-1"
          half-increments
          hover
          dense
          small
          class="d-inline"
        />
        <span class="white--text"> {{ modifiedRating }}</span>
      </div>
      <div
        v-else
        class="mb-0">
        <v-rating
          v-model=modifiedRating
          color="yellow darken-3"
          background-color="grey darken-1"
          readonly
          dense
          small
          class="d-inline"
        />
        <span class="white--text"> {{ modifiedRating }}</span>
      </div>
      <span class="title white--text">4.2 </span>
      <span class="mr-3 grey--text">/ 5</span>
      <span class="white--text">based on <strong>{{ voteCnt }}</strong> user ratings</span>
    </v-card-text>
  </v-card>
  <v-dialog
    v-model="dialog"
    persistent
    max-width="290"
  >
    <v-card
      style="background-color: rgba(0, 0, 0, 0.7);"  
    >
      <v-card-actions>
        <div class="flex-grow-1"></div>
        <v-btn 
          @click="cancelModifyRating"
          icon
          color="white"
          style="height: 40px; width: 40px;"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-card-actions>
      <v-card-text class="body-1 white--text text-center">
        Would you like to modify <br>
        your rating?
      </v-card-text>

      <v-card-actions>
        <div class="flex-grow-1"></div>
        <v-btn
          @click="modifyRating"
          text
          color="red darken-3"
        >
          Submit
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import router from "../../router";

export default {
  props: {
    ratedMovie: {
      type: Object,
      default: {
        id: '',
        movie: Array,
        rating: ''
      }
    }
  },
  data() {
    return {
      dialog: false,
      modifiedRating: Number(this.ratedMovie.rating)
    }
  },
  computed: {
    ...mapGetters('auth', {
      user: 'profileUser'
    }),
    rating() {
      return Number(this.ratedMovie.rating)
    },
    voteCnt() {
      return this.ratedMovie.movie.imdb_vote
    },
    host() {
      return this.$route.params.nickname
    }
  },
  methods: {
    ...mapActions("rating", ["patchRating"]),
		goToWithParams: function(path, params) {
			router.push({ name: path, params:{ movieId: params} });
    },
    modifyRating: function() {
      this.patchRating({ratingId: this.ratedMovie.id, params: {rating: this.modifiedRating}})
      // this.$store.dispatch("rating/patchRating",{rating: this.modifiedRating})
      this.dialog = false
    },
    cancelModifyRating: function() {
      this.modifiedRating = this.rating
      this.dialog = false
    }
	}
}
</script>

<style scoped>
.cut-text {
  text-align: left;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-inline-box;
  line-height: 88px;
  max-height: 88px;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}

.rated-movie-card {
  background-color: rgba(0, 0, 0, 0) !important; 
  width: 300px !important; 
  height: 600px !important;
}
.rated-movie-img {
  height: 400px; 
  width: 100%; 
  background-image: url('../../../public/assets/no_poster.png');
  cursor: pointer;
}
</style>