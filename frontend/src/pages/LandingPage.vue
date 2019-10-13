<template>
  <v-container style="position: fixed;" fluid fill-height class="pl-0">
    <div class="img-cover" :style="{ 'background-image' : backgroundImage }"></div>
    <transition
      @before-enter="logoFadeInUp"
      @enter="enterSignIn"
      @after-enter="signInCall"
    >
      <v-img class="logo" v-show="logoShow" src="../../public/assets/logo.png" style="width: 36px;"></v-img>
    </transition>
    <v-layout class="align-center justify-center">
      <v-flex>
        <transition
          @before-enter="heyFadeInUp"
          @enter="enter"
          @after-enter="nCall"
          @before-leave="heyFadeOutUp"
        >
          <div v-show="heyShow" style="position: absolute; height: 20vh; left: 10%; top: 35%; color: white;">
            <div class="hey">
              <h1>HEY</h1>
            </div>
          </div>
        </transition>
        <transition
          @before-enter="nFadeInUp"
          @enter="enter"
          @after-enter="nerdCall"
          @before-leave="nFadeOutUp"
        >
          <div v-show="nShow" style="position: absolute; height: 20vh; left: 10%; top: 35%; color: red;">
            <div class="n">
              <h1>&</h1>
            </div>
          </div>
        </transition>
        <transition
          @before-enter="nerdFadeInUp"
          @enter="enter"
          @after-enter="logoCall"
          @before-leave="nerdFadeOutUp"
        >
          <div v-show="nerdShow" style="position: absolute; height: 20vh; left: 10%; top: 35%; color: white;">
            <div class="nerd">
              <h1>NERD</h1>
            </div>
          </div>
        </transition>
      </v-flex>
      <!-- SignIn or SignUp-->
      <transition
        @before-enter="signInFadeInUp"
      >
        <Signin
          :toggle="toggle"
          @turnToggle="toggle=false"
          @turnErrSnackbar="errSnackbar=true"
          v-show="signInShow"
          style="position:absolute;"
        />
      </transition>
      <transition
        @before-enter="signUpFadeInRight"  
        @before-leave="signUpFadeOutRight"
      >
        <Signup
          v-if="!toggle"
          :toggle="toggle"
          @turnToggle="toggle=true"
          @turnsignUpSnackbar="signUpSnackbar=true"
          @turnexistSnackbar="existSnackbar=true"
          style="position:absolute;"
        />
      </transition>
    </v-layout>
    <!-- snackbars -->
    <v-snackbar
      v-model="signUpSnackbar"
      color="success"
    >
      You can use our services now.
      <v-btn
        text
        @click="signUpSnackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
    <v-snackbar
      v-model="existSnackbar"
      color="#E50914"
    >
      This E-mail already exists.
      <v-btn
        text
        @click="existSnackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
    <v-snackbar
      v-model="errSnackbar"
      color="#E50914"
    >
      Password is incorrect or ID does not exist.
      <v-btn
        text
        @click="errSnackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
  </v-container>
</template>

<script>
import router from "@/router"
import Signin from "../components/Landing/Signin";
import Signup from "../components/Landing/Signup";
import { setTimeout } from 'timers';
import { mapState, mapGetters, mapMutations, mapActions } from "vuex";

export default {
  components: {
    Signin,
    Signup,
  },
  data() {
    return {
      signUpSnackbar : false,
      existSnackbar : false,
      errSnackbar: false,
      toggle : true,
      heyShow : false,
      nShow : false,
      nerdShow : false,
      logoShow : false,
      signInShow : false,
      backgroundImageList : ['DeadPool.jpg', 'disney.jpg', 'aboutTime.jpg', 'beginAgain.jpg','500DaysOfSummer.jpg', 'interStellar.jpg', 'inception.jpg', 'avengers.jpg', 'guardiansOfTheGalaxy.jpg', 'joker.jpg', 'sherLock.jpg', 'spiderMan.jpg', 'starWars.jpg', 'tangled.jpg', 'aladdin.jpg', 'lalaland.jpg'],
    }
  },
  computed: {
    backgroundImage() {
      return `url('assets/background-images/Landing/${this.backgroundImageList[Math.floor(Math.random() * this.backgroundImageList.length)]}')`
    },
    ...mapGetters('auth', {
      user: 'profileUser'
    }),
    ...mapState('profiles', {
      profile: 'singleProfile'
    })
  },
  methods: {
    ...mapActions("profiles", ["getSingleProfile"]),
    ...mapMutations("entrance", ["checkNavBar", "toggleProfileSnackBar"]),
    ...mapMutations("auth", ["initError"]),
    enter(el, done) {
      setTimeout(function() {
        done()
      }, 1000)
    },
    enterSignIn(el, done) {
      setTimeout(function() {
        done()
      }, 500)
    },
    heyFadeInUp(el) {
      el.classList.add("animated");
      el.classList.add("fadeInUp");
    },
    nCall(el) {
      this.heyShow = false
      this.nShow = true
    },
    heyFadeOutUp(el) {
      el.classList.add("animated");
      el.classList.add("fadeOutUp");
    },
    nFadeInUp(el) {
      el.classList.add("animated");
      el.classList.add("fadeInUp");
    },
    nerdCall(el) {
      this.nShow = false
      this.nerdShow = true
    },
    nFadeOutUp(el) {
      el.classList.add("animated");
      el.classList.add("fadeOutUp");
    },
    nerdFadeInUp(el) {
      el.classList.add("animated");
      el.classList.add("fadeInUp");
    },
    logoCall(el) {
      this.nerdShow = false
    },
    nerdFadeOutUp(el) {
      el.classList.add("animated");
      el.classList.add("fadeOutUp");
      var self = this;
      setTimeout(function() {
        self.logoShow = true
      }, 500)
    },
    logoFadeInUp(el) {
      el.classList.add("animated");
      el.classList.add("fadeInUp");
    },
    signInCall(el) {
      this.signInShow = true
    },
    signInFadeInUp(el) {
      el.classList.add("animated");
      el.classList.add("fadeInUp");
    },
    signUpFadeInRight(el) {
      el.classList.add("animated");
      el.classList.add("slideInRight");
    },
    signUpFadeOutRight(el) {
      el.classList.add("animated");
      el.classList.add("slideOutRight");
    }
  },
  mounted() {
    this.heyShow = true
    this.checkNavBar(false)
    this.toggleProfileSnackBar(false)
  },
  async beforeRouteLeave(to, from, next) {
    await this.initError()
    next()
  },
}
</script>

<style scoped>  
.logo {
  position: absolute;
  top: 16px;
  left: 14px;
  color: white;
}

@media (max-width: 575px) {
  .hey {
    font-size :60px;
    left: 0px;
  }
  .n {
    font-size :60px;
    left: 0px;
  }
  .nerd {
    font-size :60px;
    left: 0px;
  }
}

@media (min-width: 576px) {
  .hey {
    font-size :100px;
  }
  .n {
    font-size :100px;
  }
  .nerd {
    font-size :100px;
  }
}

.img-cover{
  background-size: cover;
  background-position: 50% 50%;
  background-attachment: fixed;
  height: 100%;
  width: 100%;
  opacity: 0.3;
  position: absolute;
  z-index: 0;
}

.container::-webkit-scrollbar { 
  display: none;
}
</style>