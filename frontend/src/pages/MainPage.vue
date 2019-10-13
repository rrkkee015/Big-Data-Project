<template>
  <v-container grid-list-md white--text> 
    <ScrollToTop />
    <v-layout justify-center align-center wrap>
      <v-flex mx-1 my-10 sm9 style="max-width: 936px;">
        <v-layout mt-5 wrap>
          <v-flex data-aos="fade-in" data-aos-once="true" data-aos-duration="2000" data-aos-delay="1200" mt-12 pa-2 xs12 md6 lg4 class="justify-self-center">
            <div class="neon neon-box-main">
              <p><span>R</span>ecomm<span>en</span>ded M<span>o</span>vie</p>
            </div>
          </v-flex>
          <v-flex 
            v-for="i in movieListCards.length" 
            :key="i" 
            pa-2 xs12 md6 lg4>
            <MovieListCard
              :movie="movieListCards[i-1]"
              class="pa-3"
            />
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import router from '@/router'
import { mapState, mapActions, mapMutations, mapGetters } from "vuex";
import { setTimeout } from 'timers';
import MovieListCard from "../components/Common/MovieListCard"
import ScrollToTop from "../components/Common/ScrollToTop"

export default {
  components: {
    MovieListCard,
    ScrollToTop,
  },
  data() {
    return {
      recTextShow: false,
      recText2Show: false
    }
  },
  computed: {
    ...mapState ({
      movieListCards: state => state.random.movieRandomList
    }),
    ...mapGetters('profiles', ['ratingsLength']),
    user() {
      if (this.$store.getters['auth/profileUser']) {
        return this.$store.getters['auth/profileUser']
      } 
    },
  },
  created() {
    this.checkNavBar(true)
  },
  async mounted() {
    this.checkProfile()
    await this.getRandomMovie()
    var self = this
    setTimeout(function() {
      self.recTextShow = true
    }, 700)
    setTimeout(function() {
      self.recText2Show = true
    }, 1200)
  },
  methods: {
    ...mapActions("random", ["getRandomMovie"]),
    ...mapMutations("entrance", ["checkNavBar"]),
    ...mapMutations("entrance", ["toggleProfileSnackBar"]),
    checkProfile() {
      if (this.user) {
        if (this.user.gender == "" || this.user.age == null || this.user.occupation == "") {
          this.toggleProfileSnackBar(true)
        } else {
          this.toggleProfileSnackBar(false)
        }
      } 
    },
    recTextFadeInLeft(el) {
      el.classList.add("animated");
      el.classList.add("fadeInLeft");
    },
    recText2FadeInLeft(el) {
      el.classList.add("animated");
      el.classList.add("fadeInLeft");
    }
  }
}
</script>

<style scoped>
.neon-box-main {
  width: 100%;
  box-shadow: -1px -6px 20px 20px black inset;
}

@import url(//fonts.googleapis.com/css?family=Vibur);

.neon {
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