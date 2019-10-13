<template>
<div v-if="navBarShow">
  <!-- Navigation button & Logo -->
  <v-app-bar style="z-index: 1; background-color:black" app flat clipped-left class="py-3 d-md-none header">
    <a class="nav-icon" @click="drawer = !drawer">
      <div class="nav-one"></div>
      <div class="nav-two"></div>
      <div class="nav-three"></div>
      <div class="nav-four"></div>
    </a>
    <div class="flex-grow-1"></div>
    <v-toolbar-title class="pointer white--text font-weight-black" @click="goTo('home')">
      <v-img src="../../../public/assets/logo.png" style="width: 36px;"></v-img>
    </v-toolbar-title>
  </v-app-bar>

  <div class="d-none d-md-flex" style="z-index: 3 !important; width:64px; height:100%;">
    <v-app-bar app flat clipped-left class="side" style="width:64px; height:100%;">
      <v-content style="height: 100%" class="py-3">
        <v-row style="position: fixed; padding-left: 10px">
          <a class="white--text font-weight-black" @click="goTo('home')">
            <v-img src="../../../public/assets/logo.png" style="width: 36px;"></v-img>
          </a>
        </v-row>
      </v-content>
      <div class="arrows" @click="drawerChange()">
        <span id="arrow1"  class="arrow primera next "></span>
        <span id="arrow2" class="arrow segunda next "></span>
      </div>
    </v-app-bar>
  </div>

  <!-- Navigation drawer -->
  <v-navigation-drawer hide-overlay v-model="drawer" app color="rgba(0, 0, 0, 0)" mobile-break-point="100000" style="z-index: 2 !important; width: 100%;">
    <v-layout style="height: 100%">
      <v-col cols="12" md="3" class="drawer-background">
        <div class="px-7 pt-5 pb-3" style="display: flex; justify-content: space-between;">
          <div style="display: flex; align-items: center;">
            <v-btn icon @click="drawer=drawerChange()" style="width: 24px; height: 24px;"><v-icon>mdi-close</v-icon></v-btn>
          </div>
          <div>
            <v-btn text @click="goToWithParams('profile-detail', user.nickname)" class="lowercase">{{ user.nickname }}</v-btn>
            <v-btn text @click="signOut" class="capitalize">Logout</v-btn>
          </div>
        </div>
      <!-- Menu list -->
        <v-list class="pt-1">
          <v-list-item v-for="(choice, i) in choicesMenu" :key="i" @click="goTo(choice.path)">
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold pl-4">{{ choice.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item v-show="user.user.is_staff" @click="goTo('admin-home')">
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold pl-4" style="z-index: 2;">Admin</v-list-item-title>
            </v-list-item-content>                                      
          </v-list-item>
        </v-list>
        <!-- Bottom list -->
        <BottomList 
          @goToAboutus="goTo('about-us')"
          style="margin-top: auto;"
				/>
      </v-col>
      <v-col cols="9" class="pa-0 d-none d-md-flex" style="background-color: rgb(0, 0, 0)">
        <video autoplay loop muted class="video-cover darkness">
          <source src="assets/movie_video.mp4" type="video/mp4">
        </video>
      </v-col>
    </v-layout>
  </v-navigation-drawer>
</div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import router from "../../router";
import BottomList from "./BottomList"

export default {
  components: {
    BottomList
  },
  data() {
    return {
      isClicked: false,
      drawer: false,
      choicesMenu: [
        {
          text: "Movies",
          path: "movie-search",
        },
        {
          text: "About us",
          path: "about-us",
        },
      ],
      links: [
        {
          class: "sns__color gitlab__color",
          icon: "fab fa-gitlab",
          path: "https://lab.ssafy.com/HyehuiLee/bigdata-sub2"
        },
        {
          class: "sns__color facebook__color",
          icon: "fab fa-facebook-f",
          path: ""
        },
        {
          class: "sns__color twitter__color",
          icon: "fab fa-twitter",
          path: ""
        },
        {
          class: "sns__color instagram__color",
          icon: "fab fa-instagram",
          path: ""
        },
      ],
    }
  },
  computed: {
    ...mapState({
      navBarShow: state => state.entrance.navBarShow
    }),
    user() {
      if (this.$store.getters['auth/profileUser']) {
        return this.$store.getters['auth/profileUser']
      } else {
        return {user: {is_staff: false}}
      }
    }
  },
  methods: {
    goTo: function(path) {
      this.isClicked = false
      document.getElementById('arrow1').classList.remove('bounceAlpha')
      document.getElementById('arrow2').classList.remove('bounceAlpha')
      router.push({ name: path });
      this.drawer = false;
    },
    goToWithParams: function(path, params) {
      this.isClicked = false
      document.getElementById('arrow1').classList.remove('bounceAlpha')
      document.getElementById('arrow2').classList.remove('bounceAlpha')
      router.push({ name: path, params:{ nickname: params }});
      this.drawer = false;
    },
    changeLocation: function(path) {
      location = `/${path}`
    },
    imageFadeIn(el) {
      el.classList.add("animated");
      el.classList.add("fadeIn");
    },
    drawerChange() {
      this.isClicked = !this.isClicked
      if (this.isClicked) {
        document.getElementById('arrow1').classList.add('bounceAlpha')
        document.getElementById('arrow2').classList.add('bounceAlpha')
      } else {
        document.getElementById('arrow1').classList.remove('bounceAlpha')
        document.getElementById('arrow2').classList.remove('bounceAlpha')
      }
      this.drawer = !this.drawer
    },
    signOut() {
      this.$store.dispatch('auth/userLogout')
      // this.changeLocation('')
    }
  }
}
</script>

<style scoped>
.drawer-background {
  display: flex;
  flex-direction: column;
  height: 100%; 
  background-color: #f3f2f0;
  padding: 0;
}
.capitalize {
  font-weight: 300;
  text-transform: capitalize;
}
.lowercase {
  font-weight: 300;
  text-transform: lowercase;
}
.arrows{
  cursor: pointer; position: absolute; padding-left: 1.5rem;
}

.pointer {
  cursor: pointer;
}

.arrows .arrow{left: 30%;}
.arrow {position: absolute; bottom: 0;  margin-left:0px; width: 15px; height: 15px; background-size: contain; top:15px;}
.segunda{margin-left: 8px;}
.next {
	background-image: url(data:image/svg+xml;base64,PHN2ZyBpZD0iTGF5ZXJfMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiI+PHN0eWxlPi5zdDB7ZmlsbDojZmZmfTwvc3R5bGU+PHBhdGggY2xhc3M9InN0MCIgZD0iTTMxOS4xIDIxN2MyMC4yIDIwLjIgMTkuOSA1My4yLS42IDczLjdzLTUzLjUgMjAuOC03My43LjZsLTE5MC0xOTBjLTIwLjEtMjAuMi0xOS44LTUzLjIuNy03My43UzEwOSA2LjggMTI5LjEgMjdsMTkwIDE5MHoiLz48cGF0aCBjbGFzcz0ic3QwIiBkPSJNMzE5LjEgMjkwLjVjMjAuMi0yMC4yIDE5LjktNTMuMi0uNi03My43cy01My41LTIwLjgtNzMuNy0uNmwtMTkwIDE5MGMtMjAuMiAyMC4yLTE5LjkgNTMuMi42IDczLjdzNTMuNSAyMC44IDczLjcuNmwxOTAtMTkweiIvPjwvc3ZnPg==);
}

@keyframes bounceAlpha {
  0% {opacity: 1; transform: translateX(0px) scale(1);}
  25%{opacity: 0; transform:translateX(10px) scale(0.9);}
  26%{opacity: 0; transform:translateX(-10px) scale(0.9);}
  55% {opacity: 1; transform: translateX(0px) scale(1);}
}

.bounceAlpha {
    animation-name: bounceAlpha;
    animation-duration:1.7s;
    animation-iteration-count:infinite;
    animation-timing-function:linear;
}

.arrow.primera.bounceAlpha {
    animation-name: bounceAlpha;
    animation-duration:1.7s;
    animation-delay:0.2s;
    animation-iteration-count:infinite;
    animation-timing-function:linear;
}

.arrows:hover .arrow{
    animation-name: bounceAlpha;
    animation-duration:1.7s;
    animation-iteration-count:infinite;
    animation-timing-function:linear;
}
.arrows:hover .arrow.primera{
    animation-name: bounceAlpha;
    animation-duration:1.7s;
    animation-delay:0.2s;
    animation-iteration-count:infinite;
    animation-timing-function:linear;
}

>>> #keep .v-navigation-drawer__border {
  display: none;
}

>>> .header {
  background-color: rgba(0, 0, 0, 0);
}

>>> .side {
  background-color: rgba(0, 0, 0);
}

>>> a {
  color: rgba(0, 0, 0, 0.87) !important;
  text-decoration: none;
}

>>> .gitlab__color:hover {
    background: linear-gradient(
    to right,
    #fea227,
    #fa7e1e,
    #e34329,
    #fa7e1e,
    #fea227
  );
}
>>> .facebook__color:hover {
  background: linear-gradient(#3c5893);
}
>>> .twitter__color:hover {
  background: linear-gradient(#1da1f2);
}
>>> .instagram__color:hover {
  background: linear-gradient(
    to top right,
    #feda75,
    #fa7e1e,
    #d62976,
    #962fbf,
    #4f5bd5
  );
}
>>> .sns__color {
  -webkit-transition: none;
  transition: none;
}
>>> .sns__color:hover,
>>> .sns__color:active {
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  transition: none;
}

>>> .v-list-item:after {
  content: '';
  position:absolute;
  width:100%;
  transform:skew(-40deg);
  border-bottom:48px solid rgba(0, 0, 0);
  bottom:0%;
  left:-120%;
  transition-delay: all 0.5s;
  transition: all 0.5s;
  transition-timing-function: ease;
  transition-duration: 1s;
}
>>> .v-list-item:hover:after,
>>> .v-list-item.hover:after {
  left:-30%;
}

>>> .v-list-item .v-list-item__title {
  text-shadow:0px -40px 0px rgba(255, 255, 255, 1);
  transition:all 0.75s;
  transition-delay:all 0.25s;
  z-index: 2;
}

>>> .v-list-item .v-list-item-router {
  text-shadow:0px -40px 0px rgba(255, 255, 255, 1);
  transition:all 0.75s;
  transition-delay:all 0.25s;
  z-index: 2;
}

>>> .v-list-item:hover .v-list-item__title,
>>> .v-list-item.hover .v-list-item__title {
  text-shadow:0px -40px 0px rgba(255, 255, 255, 0);
  font-weight:600;
  color: white;
}

>>> .v-list-item:hover .v-list-item-router .v-list-item__title{
  text-shadow:0px -40px 0px rgba(255, 255, 255, 0);
  font-weight:600;
  color: white;
}

>>> .v-navigation-drawer {
  transition-duration: 0.7s !important;
  left: 64px;
}

@media (max-width: 960px) {
  .v-navigation-drawer {
    left: 0px !important;
  }
}

>>> .nav-icon div {
  height: 2px;
  background: white;
  margin: 5px 0;
  transition: .3s;
}

>>> .nav-icon {
  display: block;
  width: 30px;
}

>>> .nav-one {
  width: 30px;
}

>>> .nav-two {
  width: 10px;
}

>>> .nav-three {
  width: 10px;
}

>>> .nav-four {
  width: 30px;
}

>>> .nav-icon:hover div {
  width: 30px;
}

>>> .v-toolbar__content {
  height: 100% !important;
}

>>> .v-navigation-drawer--is-mobile:not(.v-navigation-drawer--close) {
  -webkit-box-shadow: none !important;
          box-shadow: none !important;
}

>>> .theme--light.v-navigation-drawer:not(.v-navigation-drawer--floating) .v-navigation-drawer__border {
  background-color: rgba(0, 0, 0, 0) !important;
}

>>> .theme--light.v-navigation-drawer .v-divider {
  border-color: rgba(0, 0, 0, 0) !important;
}

.video-cover{
  width: 100%;
}

>>> @media (max-width: 700px) {
  .hide-info {
    display: none;
  }
  .v-list-item:after {
    content: '';
    position:absolute;
    width:100%;
    transform:skew(-40deg);
    border-bottom:48px solid rgba(0, 0, 0);
    bottom:0%;
    left:-120%;
    transition-delay: all 0.5s;
    transition: all 0.5s;
    transition-timing-function: ease;
    transition-duration: 0.2s;
  }
  .v-list-item:hover:after,
  .v-list-item.hover:after {
    left:-30%;
  }

  .v-list-item .v-list-item__title {
    text-shadow:0px -40px 0px rgba(255, 255, 255, 1);
    transition:all 0.2s;
    transition-delay:all 0.2s;
    z-index: 2;
  }
  .v-list-item .v-list-item-router .v-list-item__title {
    text-shadow:0px -40px 0px rgba(255, 255, 255, 1);
    transition:all 0.2s;
    transition-delay:all 0.2s;
    z-index: 2;
  }

  .v-list-item:hover .v-list-item__title,
  .v-list-item.hover .v-list-item__title {
    text-shadow:0px -40px 0px rgba(255, 255, 255, 0);
    font-weight:600;
    color: white;
  }
  .v-list-item:hover .v-list-item-router .v-list-item__title {
    text-shadow:0px -40px 0px rgba(255, 255, 255, 0);
    font-weight:600;
    color: white;
  }
}
</style>
