<!-- 영화 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs6>
        <div class="display-2 pa-10">장르 검색</div>
        <GenreSearchForm :submit="searchMovies" />
      </v-flex>
      <!-- 검색 결과 -->
      <v-flex xs7>
        <MovieList :movie-list-cards="movieList" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import GenreSearchForm from "../GenreSearchForm";
import MovieList from "../MovieList";
export default {
  components: {
    MovieList,
    GenreSearchForm
  },
  data: () => ({}),
  computed: {
    ...mapState("data", {
      movieList: 'movieSearchList'
    })
  },
  methods: mapActions("data", ["searchMovies"])
};
</script>
