<template>
  <v-container style="padding-top: 175px; max-width: 100%;" class="white--text container-padding-top">
    <v-row style="border-bottom: solid 1px;" data-aos="fade-up" data-aos-once="true" data-aos-duration="1500">
      <v-col cols="12" md="4" style="display:flex; justify-content:center;">
        <div class="title-text title-detail-text">{{ movie.title }}</div>
      </v-col>
      <v-col class="detail-text detail-media-text" cols="12" md="8">
        <div class="title-detail-text detail-main-text">Detail</div>
      </v-col>
    </v-row>
    <v-row class="pt-12">
      <v-col data-aos="fade-up" data-aos-once="true" data-aos-duration="1500" data-aos-delay="400" cols="12" md="4" class="detail-poster" style="justify-content: center; display: grid;">
        <v-img :src="movie.poster" lazy-src class="thum" style="height: 450px; width: 300px" />
      </v-col>
      <v-col cols="12" md="8">
        <v-row class="detail-text-responsive" style="justify-content: center">
          <v-col data-aos="fade-left" data-aos-once="true" data-aos-duration="1500" data-aos-delay="800" cols="12" sm="5" md="5" class="pt-0">
            <span class="detail-text">{{ movie.fullPlot }}</span>
          </v-col>
          <v-col cols="1"></v-col>
          <MovieDetail></MovieDetail>
        </v-row>
      </v-col>
    </v-row>
    <v-row data-aos="fade-up" data-aos-once="true" data-aos-duration="1500">
      <v-col cols="4">
      </v-col>
      <v-col style="padding-top: 250px; border-bottom: solid 1px;" class="responsive-pt" cols="12" md="8">
        <div class="title-detail-text detail-media-text">Media</div>
      </v-col>
    </v-row>
    <v-row data-aos="fade-up" data-aos-once="true" data-aos-duration="2000" >
      <v-col cols="4" class="display"></v-col>
      <v-col cols="12" md="8" class="px-0">
        <div class="video">
          <iframe
            :src="youtubeUrl"
            frameborder="0"
            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
          >
          </iframe>
        </div>
      </v-col>
    </v-row>
    <v-row data-aos="fade-up" data-aos-once="true" data-aos-duration="2000" >
      <v-col cols="4">
      </v-col>
      <v-col style="padding-top: 250px; border-bottom: solid 1px;" class="responsive-pt" cols="12" md="8">
        <div class="title-detail-text detail-media-text">User Lists</div>
      </v-col>
    </v-row>
    <div v-if="movieTags">
      <v-row data-aos="fade-up" data-aos-once="true" data-aos-duration="2000">
        <v-col cols="4" class="display"></v-col>
        <v-col style="padding-top: 250px; border-bottom: solid 1px;" class="responsive-pt" cols="12" md="8">
          <div class="title-detail-text detail-media-text">Tags</div>
        </v-col>
      </v-row>

      <v-row data-aos="fade-up" data-aos-once="true" data-aos-duration="2000">
        <v-col cols="4" class="display"></v-col>
        <v-col cols="12" md="8" class="px-0">
          <h2 style="line-height: 26px"><marquee scrollamount = "17">{{ movie.tags[0] }}</marquee></h2>
          <h3 style="line-height: 22px"><marquee scrollamount = "15">{{ movie.tags[1] }}</marquee></h3>
          <h1 style="line-height: 36px"><marquee scrollamount = "11">{{ movie.tags[2] }}</marquee></h1>
          <h4 style="line-height: 18px"><marquee scrollamount = "20">{{ movie.tags[3] }}</marquee></h4>
          <h1 style="line-height: 36px"><marquee scrollamount = "14">{{ movie.tags[4] }}</marquee></h1>
          <h3 style="line-height: 22px"><marquee scrollamount = "18">{{ movie.tags[5] }}</marquee></h3>
          <h2 style="line-height: 26px"><marquee scrollamount = "12">{{ movie.tags[6] }}</marquee></h2>
          <h4 style="line-height: 18px"><marquee scrollamount = "13">{{ movie.tags[8] }}</marquee></h4>
          <h2 style="line-height: 26px"><marquee scrollamount = "19">{{ movie.tags[9] }}</marquee></h2>
        </v-col>
      </v-row>
    </div>

    <div>
      <v-row data-aos="fade-up" data-aos-once="true" data-aos-duration="2000">
        <v-col cols="4" class="display"></v-col>
        <v-col style="padding-top: 250px; border-bottom: solid 1px;" class="responsive-pt" cols="12" md="8">
          <div class="title-detail-text detail-media-text">How about these movies?</div>
        </v-col>
      </v-row>

      <v-row data-aos="fade-up" data-aos-once="true" data-aos-duration="2000">
        <v-col cols="4" class="display"></v-col>
        <v-col cols="12" md="8" class="px-0 mb-12" style="height: 600px;">
          <RecommendedMovieList />
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import axios from 'axios'
import MovieDetail from "@/components/MovieDetail/MovieDetail";
import RecommendedMovieList from "@/components/MovieDetail/RecommendedMovieList"

export default {
  components: {
    MovieDetail,
    RecommendedMovieList,
  },
  computed: {
    ...mapGetters("data", {
      movie: "getMovie"
    }),
    movieTags() {
      if (this.movie.tags) {
        return true
      } else {
        return false
      }
    },
    youtubeUrl() {
      return 'https://www.youtube.com/embed/' + this.movie.youtubeId
    }
  },
  async created() {
    await this.searchMovie(this.$route.params.movieId)
  },
  methods: {
    ...mapActions("data", ["searchMovie"])
  },
  async beforeRouteUpdate (to, from, next) {
    await this.searchMovie(to.params.movieId)
    next()
  },
};
</script>

<style scoped>
.video {
  position: relative;
  width: 100%;
  padding-bottom:56.25%;
  overflow: hidden;
}
.video iframe {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
}

.title-detail-text {
  font-size: 1.75rem !important;
  line-height: 2rem;
  letter-spacing: 0.0125em !important;
}

.detail-text {
  font-size: 1rem !important;
}
.detail-poster{
  background-size: cover;
}

@media (max-width: 959px) {
  .detail-media-text {
    display: flex;
    justify-content: center;
  }
  .detail-text-responsive {
    padding-top: 25px;
  }
  .title-text {
    font-size: 2rem !important;
  }
  .detail-main-text {
    padding-top: 35px;
  }
  .container-padding-top {
    padding-top: 130px !important;
  }
  .responsive-pt {
    padding-top:35px !important;
  }
  .display {
    display: none;
  }
}
</style>