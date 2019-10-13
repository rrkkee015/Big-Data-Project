<template>
  <div 
    class="profile-sticky"
  >
  <!-- Profile img & Nickname -->
    <v-row class="d-flex">
      <span class="body-1 font-weight-medium px-5 my-5">{{ profile.nickname }}</span>
    </v-row>
    <!-- User Detail Info -->
    <v-row class="body-2 px-5">
      <table>
        <tbody>
          <tr>
            <td class="py-2 grey--text font-weight-medium">AGE</td>
            <td class="py-2 pl-6">{{ profile.age }}</td>
          </tr>
          <tr>
            <td class="py-2 grey--text font-weight-medium">GENDER</td>
            <td class="py-2 pl-6">{{ profile.gender }}</td>
          </tr>
          <tr>
            <td class="py-2 grey--text font-weight-medium">OCCUPATION</td>
            <td class="py-2 pl-6">{{ profile.occupation }}</td>
          </tr>
        </tbody>
      </table>
    </v-row>
    <v-row class="profile-detail">
      <v-spacer></v-spacer>
      <v-btn 
        v-if="profile.nickname === user.nickname"
        text 
        color="grey"
        @click="goToWithParams('profile-setting', profile.nickname)"
      >
        Settings
        <v-icon 
          color="grey" 
          class="pl-2"
        >
          mdi-settings
        </v-icon>
      </v-btn>
    </v-row>
    <hr 
      class="my-5" 
      style="border: 0.5px solid rgba(255, 255, 255, 0.7);"
    >
    <v-row class="body-2 px-6">
      <v-col 
        cols="12"
        lg="6"
        class="px-0"
      >
        <span class="grey--text font-weight-medium">RATINGS </span>
        <span class="pl-5 white--text">{{ ratingsLength }}</span>
      </v-col>
      <v-col 
        cols="12"
        lg="6"
        class="px-0"
      >
        <span class="grey--text font-weight-medium">SUBSCRIBE</span>
        <span class="pl-5 white--text">{{ expirySubscribeDate }}</span>
      </v-col>
    </v-row>
    <!-- Recommended UserList -->
    <v-row 
      class="mx-2 mt-5 pa-3"
      style="border: solid 1px rgba(255, 255, 255, 0.2);"
    >
      <p class="grey--text px-3">Recommended Users</p>
      <RecommendedUserList />
    </v-row>
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import router from "../../router";
import RecommendedUserList from "./RecommendedUserList";

export default {
  components: {
    RecommendedUserList
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
    // ...mapGetters("profiles", ["profile"]),
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
      document.getElementById('arrow1').classList.remove('bounceAlpha')
      document.getElementById('arrow2').classList.remove('bounceAlpha')
      router.push({ name: path, params:{ nickname: params }});
    },
  }
};
</script>

<style scoped>
.profile {
  object-fit: cover;
  border-radius: 50%;
  height: 70px;
  width: 70px;
}

.profile-detail button {
  font-weight: 300;
  text-transform: capitalize;
}

.profile-sticky {
  position: fixed;
  top: 130px;
  width: 25%;
}
</style>