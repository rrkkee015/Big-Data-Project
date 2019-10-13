<template>
  <div>
    <v-row class="px-3">
      <v-col
      cols="10"
        class="align-self-center"
      >
        <span class="body-1 font-weight-medium">{{ profile.nickname }}</span>
      </v-col>
      <v-col 
        cols="2"
        class="align-self-center"
      >
        <v-btn 
          v-if="profile.nickname === user.nickname"
          text 
          color="grey"
          @click="goToWithParams('profile-setting', profile.nickname)"
        >
          <v-icon 
            color="grey" 
          >
            mdi-settings
          </v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <hr 
      class="my-3" 
      style="border: 0.5px solid rgba(255, 255, 255, 0.7);"
    >
    <v-row class="body-2 px-6">
      <v-col 
        cols="5"
        class="px-0"
      >
        <p class="grey--text font-weight-medium">RATINGS 
          <span class="white--text pl-1">{{ ratingsLength }}</span>
        </p>
      </v-col>
      <v-col 
        cols="6"
        class="px-0"
      >
        <p class="grey--text font-weight-medium">SUBSCRIBE
          <span class="white--text pl-1">{{ expirySubscribeDate }}</span>
        </p>
      </v-col>
      <v-col
        cols="1" 
        class="px-0 py-2"
      >
        <v-btn
          icon
          @click="show = !show"
          style="height: 20px;"
        >
          <v-icon
            color="white"
          >{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
        </v-btn>
      </v-col>

      <v-expand-transition>
        <div v-show="show">
          <p class="grey--text">Recommended Users</p>
          <RecommendedUserList />
        </div>
      </v-expand-transition>
    </v-row>
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import router from "../../router"
import RecommendedUserList from "./RecommendedUserList";

export default {
  components: {
    RecommendedUserList
  },
  data() {
    return {
      show: false,
    }
  },
  computed: {
    user() {
      if (this.$store.getters['auth/profileUser']) {
        return this.$store.getters['auth/profileUser']
      } else {
        return {}
      }
    },
    profile() {
      if (this.$store.getters['profiles/profile']) {
        return this.$store.getters['profiles/profile']
      } else {
        return {}
      }
    },
    ...mapGetters('profiles', {
      ratingsLength: 'ratingsLength'
    }),
    expirySubscribeDate() {
      if (this.profile.expiry_subscribe_date) {
        return this.profile.expiry_subscribe_date.split('T')[0]
      } else {
        return this.profile.expiry_subscribe_date
      }
    },
  },
  methods: {
    goToWithParams: function(path, params) {
      this.isClicked = false
      document.getElementById('arrow1').classList.remove('bounceAlpha')
      document.getElementById('arrow2').classList.remove('bounceAlpha')
      router.push({ name: path, params:{ nickname: params }});
      this.drawer = false;
    },
  }
};
</script>

<style scoped>

</style>