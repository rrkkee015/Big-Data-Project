<template>
  <div>
    <hr>
    <v-row>
      <v-col
      v-for="(link, i) in links"
      :key="i"
      class="py-4 text-center"
      >
        <a target="_blank" rel="noopener noreferrer" :href="link.path">
          <v-icon :class="link.class">{{ link.icon }}</v-icon>
        </a>
      </v-col>
    </v-row>
    <hr>
    <v-row class="hide-info font-weight-light px-7 pt-5">
      <v-col @click="$emit('goToAboutus')" cols="12" sm="6" md="12" lg="6" class="pointer">
        <v-img class="logo" src="../../../public/assets/favicon.png" style="width: 30px; margin-bottom: 16px;"></v-img>
        <p class="body-2">The Hey <span style="color: red;">&</span>Nerd is a movie recommendation site build movie database.</p>
      </v-col>
      <v-col cols="12" sm="6" md="12" lg="6">
        <p class="subtitle-1 font-weight-medium">Get in touch<p>
        <p class="body-2">Phone: +82 10-0000-0000</p>
        <a class="body-2" href="mailto:ssafy@ssafy.com">Email: ssafy@ssafy.com</a>
      </v-col>
      <v-col cols="12">
        <p class="subtitle-1 font-weight-medium">Total Datas</p>
        <p v-for="(choice, i) in choices" :key="i" @click="goTo(choice.path)" class="body-2">{{ choice.text }} : {{ choice.cnt }}</p>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import router from "../../router";
import NavigationDrawerVue from './NavigationDrawer.vue';

export default {
  data() {
    return {
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
    ...mapState ({
      infoList: state => state.info.infoList
    }),
    choices() {
      return [
        {
          text: "Movies",
          cnt: this.addComma(this.infoList.movie_cnt),
        },
        {
          text: "Rating",
          cnt: this.addComma(this.infoList.rating_cnt),
        },
        {
          text: "Users",
          cnt: this.addComma(this.infoList.user_cnt),
        },
      ]
    }
  },
  mounted() {
    this.getAllInfo()
  },
  methods: {
    goTo: function(path) {
      router.push({ name: path });
    },
    ...mapActions("info", ['getAllInfo']),
    addComma(num) {
      var num = "" + num
      return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }
  },
}
</script>

<style scoped>
.pointer {
  cursor: pointer;
}

a {
  color: rgba(0, 0, 0, 0.87) !important;
  text-decoration: none;
}

.gitlab__color:hover {
    background: linear-gradient(
    to right,
    #fea227,
    #fa7e1e,
    #e34329,
    #fa7e1e,
    #fea227
  );
}
.facebook__color:hover {
  background: linear-gradient(#3c5893);
}
.twitter__color:hover {
  background: linear-gradient(#1da1f2);
}
.instagram__color:hover {
  background: linear-gradient(
    to top right,
    #feda75,
    #fa7e1e,
    #d62976,
    #962fbf,
    #4f5bd5
  );
}
.sns__color {
  -webkit-transition: none;
  transition: none;
}
.sns__color:hover,
.sns__color:active {
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  transition: none;
}
</style>
