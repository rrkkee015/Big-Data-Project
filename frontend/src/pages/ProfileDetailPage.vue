<template>
  <v-container class="white--text my-12">
    <ScrollToTop />
    <v-layout row class="profile-detail-center my-12">
      <!-- UserInfo under sm -->
      <v-flex 
        xs10
        sm6
        class="ml-1 d-md-none px-3 pt-3 mb-8"
        style="border: solid 0.5px rgba(255, 255, 255, 0.2);"
      >
        <ProfileDetailUndersm/>
      </v-flex>

      <!-- RatedMovieList -->
      <v-flex 
        data-aos="fade-up" 
        data-aos-once="false"
        data-aos-duration="2000"
        xs10 
        sm6
        xl4
        class="offset-md-1 offset-lg-1 offset-xl-2"
      >
        <RatedMovieList/>
      </v-flex>

      <!-- UserInfo above md-->
      <v-flex
        md4
        lg4
        xl2
        class="d-none d-md-block ml-12 py-5"
      >
        <ProfileDetailAbovemd/>  
      </v-flex>
    </v-layout>
    <v-snackbar
      v-model="snackbar"
      color="#E50914"
    >
      Please enter information to change.
      <v-btn
        text
        @click="snackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
  </v-container>
</template>

<script>
import { mapActions } from "vuex";
import ProfileDetailUndersm from "../components/ProfileDetail/ProfileDetailUndersm";
import RatedMovieList from "../components/ProfileDetail/RatedMovieList";
import ProfileDetailAbovemd from "../components/ProfileDetail/ProfileDetailAbovemd";
import ScrollToTop from "../components/Common/ScrollToTop";

export default {
  components: {
    ProfileDetailUndersm,
    RatedMovieList,
    ProfileDetailAbovemd,
    ScrollToTop,
  },
  data() {
    return {
      snackbar: false,
      top: 0,
    }
  },
  async created() {
    await this.getSingleProfile(this.$route.params.nickname)
  },
  methods: {
    ...mapActions("profiles", ["getSingleProfile"]),
  },
  async beforeRouteUpdate (to, from, next) {
    await this.getSingleProfile(to.params.nickname)
    next()
  },
  beforeRouteLeave (to, from, next) {
    if (from.path.slice(-8) === '/setting') {
      this.snackbar = true
    }
    next()
  }
};
</script>

<style scoped>
@media (max-width: 960px) {
  .profile-detail-center {
    justify-content: center;
    display: flex;
  }
}
</style>