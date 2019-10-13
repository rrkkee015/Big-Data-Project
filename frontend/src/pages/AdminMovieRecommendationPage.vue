<template>
  <v-row class="white--text">
    <v-row class="col-12" data-aos="fade-in" data-aos-once="true" data-aos-duration="1500" data-aos-delay="400">
      <v-col>
        <div class="neon" style="display: flex; align-items: center; justify-content: center;">
          <p>Se<span>t</span>ting for <span>M</span>OVIE Recom<span>med</span>ation</p>
        </div>
      </v-col>
    </v-row>
    <MovieRecommendation data-aos="fade-in" data-aos-once="true" data-aos-duration="1500" data-aos-delay="800"/>
    <v-row v-show="cur.isKnn" class="center col-12">
      <knn/>
    </v-row>
    <v-row v-show="cur.isMf" class="center col-12">
      <mf/>
    </v-row>
  </v-row>
</template>

<script>
import { mapState } from 'vuex'
import MovieRecommendation from '../components/AdminMovieRecommendation/MovieRecommendation'
import knn from '../components/AdminMovieRecommendation/Knn'
import mf from '../components/AdminMovieRecommendation/Mf'

export default {
  computed: {
    ...mapState("movieRecommendation", ["cur"])
  },
  components: {
    MovieRecommendation,
    knn,
    mf,
  }
}
</script>

<style scoped>
@import url(//fonts.googleapis.com/css?family=Vibur);

.center {
  display: flex;
  justify-content: center;
}
.neon {
  text-align: center;
  width: 50%;
  height: 250px;
  margin: auto;
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