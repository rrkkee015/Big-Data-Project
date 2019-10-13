<!-- 영화 검색 페이지 -->
<template>
  <v-container grid-list-md text-center white--text>
    <ScrollToTop />
    <div data-aos="fade-in" data-aos-once="true" data-aos-duration="1500" data-aos-delay="400" class="neon" style="display: flex; align-items: center; justify-content: center;">
      <p>w<span>hat</span> movie do you <span>w</span>ant to fin<span>d</span>?</p>
    </div>
    <!-- 검색 폼 --> 
    <v-layout justify-center align-center wrap>
      <v-flex mx-3 my-10 xs9 style="max-width: 936px;">
        <MovieSearchForm/>
      </v-flex>
    </v-layout>
    <!-- 검색 결과 -->
    <v-layout justify-center align-center wrap>
      <v-flex mx-1 my-10 sm9 style="max-width: 936px;">
        <v-btn class="rating-icon" v-if="movieList.length" right text @click="sortByRating" color="white"><v-icon small>mdi-star</v-icon>&nbsp;Rating</v-btn>
        <v-btn class="view-icon" v-if="movieList.length" right text @click="sortByViewCount" color="white"><v-icon small>mdi-eye</v-icon>&nbsp;View</v-btn>
        <MovieList :movie-list-cards="movieList" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import MovieSearchForm from "../components/MovieSearch/MovieSearchForm";
import MovieList from "../components/MovieSearch/MovieList";
import ScrollToTop from "../components/Common/ScrollToTop"

export default {
  components: {
    MovieList,
    MovieSearchForm,
    ScrollToTop,
  },
  data: () => ({}),
  computed: {
    ...mapState("data",{ movieList: "movieSearchList" })
  },
  methods: {
    sortByRating () {
      return this.movieList.sort((a, b) => a.imdbRating > b.imdbRating ? -1 : a.imdbRating < b.imdbRating ? 1 : 0)
    },
    sortByViewCount () {
      return this.movieList.sort((a, b) => a.viewCnt > b.viewCnt ? -1 : a.viewCnt < b.viewCnt ? 1 : 0)
    },
  }
};
</script>

<style scoped>
.neon {
  text-align: center;
  width: 65%;
  height: 250px;
  margin: auto;
  background: #112 url(//images.weserv.nl/?url=i.imgur.com/6QJjYMe.jpg) center;
  background-size: contain;
  border-radius: 50px;
  box-shadow: 0px 0px 20px 20px black inset;
}
.rating-icon:hover .mdi-star {
  color: yellow;
}
.view-icon:hover .mdi-eye {
  color: #0080ff;
}

@import url(//fonts.googleapis.com/css?family=Vibur);
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