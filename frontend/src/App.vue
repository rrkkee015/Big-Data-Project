<template>
  <v-app id="app">
    <v-container fluid fill-height class="black fira-sans pa-0">
      <NavigationDrawer />
      <v-snackbar
        v-model="infoSnackbarShow"
        :timeout=timeout
        color="#E50914"
      >
        If you want to be recommended, <br>
        please fill in your profile.
        <v-btn
          text
          @click="goToWithParams('profile-setting', user.nickname)"
        >
          Go
        </v-btn>
      </v-snackbar>
      <v-layout justify-center align-center style="overflow: hidden;">
        <transition
          name="fade"
          mode="out-in"
        >
          <router-view/>
        </transition>
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
import { mapState } from "vuex";
import router from "./router"
import NavigationDrawer from "./components/Common/NavigationDrawer";

export default {
  components: {
    NavigationDrawer,
  },
  data() {
    return {
      timeout: 0
    }
  },
  computed: {
    ...mapState({
      infoSnackbarShow: state => state.entrance.infoSnackbarShow
    }),
    user() {
      if (this.$store.getters['auth/profileUser']) {
        return this.$store.getters['auth/profileUser']
      } else {
        return {}
      }
    }
  },
  methods: {
    goToWithParams: function(path, params) {
			router.push({ name: path, params:{ nickname: params} });
    },
  }
};
</script>

<style>
  .fade-enter-active,
  .fade-leave-active {
    transition-duration: 0.3s;
    transition-property: opacity;
    transition-timing-function: ease;
  }

  .fade-enter,
  .fade-leave-active {
    opacity: 0
  }

  .fira-sans {
    font-family: 'Fira Sans', sans-serif;
  }
</style>