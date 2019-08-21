<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout justify-end>
      <v-btn v-model="rating_order" text color="primary" v-show="this.movieListCards.length" @click="order_by_rating()">평점 순</v-btn>
      <v-btn v-model="view_order" text color="primary" v-show="this.movieListCards.length" @click="order_by_view()">조회 순</v-btn>
    </v-layout>
    <v-layout column>
      <v-flex v-for="card in movieListCardsSliced" :key="card.id" pa-2>
        <MovieListCard
          :id="card.id"
          :img="card.img"
          :title="card.title"
          :genres="card.genres"
          :rating="card.rating"
          :view-cnt="card.viewCnt"
        />
      </v-flex>
      <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
    </v-layout>
  </v-container>
</template>

<script>
import MovieListCard from "./MovieListCard"
export default {
  components: {
    MovieListCard
  },
  props: {
    movieListCards: {
      type: Array,
      default: () => new Array(),
    },
  },
  data: () => ({
    cardsPerPage: 10,
    page: 1,
    rating_order: false,
    view_order: false
  }),
  methods: {
    order_by_view () {
      this.view_order = !this.view_order
      this.rating_order = false
    },
    order_by_rating () {
      this.rating_order = !this.rating_order
      this.view_order = false
    }
  },
  computed: {
    // pagination related variables
    movieListEmpty: function() {
      return this.movieListCards.length === 0;
    },
    maxPages: function() {
      return Math.floor((this.movieListCards.length + this.cardsPerPage - 1) / this.cardsPerPage)
    },
    movieListCardsSliced: function() {
      if (this.rating_order == true) {
        return this.movieListCards.sort((a, b) => a.rating > b.rating ? -1 : a.rating < b.rating ? 1 : 0).slice(this.cardsPerPage * (this.page - 1), this.cardsPerPage * this.page)
      }
      else if (this.view_order) {
        return this.movieListCards.sort((a, b) => a.title < b.title ? -1 : a.title > b.title ? 1 : 0).slice(this.cardsPerPage * (this.page - 1), this.cardsPerPage * this.page)
      }
      else {
        return this.movieListCards.slice(this.cardsPerPage * (this.page - 1), this.cardsPerPage * this.page)
      }
    },
  },
};
</script>