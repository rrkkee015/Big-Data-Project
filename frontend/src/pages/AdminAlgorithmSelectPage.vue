<template>
  <v-row class="mx-0" style="height: 100%">
    <v-col class="admin-area col-12 pa-0">
      <router-link :to="{ name: 'admin-user-clustering' }">
        <a class="admin-href">
          <transition
            @before-enter="userFadeInUp"
            @enter="enter"
            @after-enter="movieCall"
          >
            <div v-show="userShow" class="admin-text font-weight-bold" data-text="USER">
              USER
            </div>
          </transition>
          <div class="admin-image-user" :style="{ 'background-image' :peopleImage }"></div>
        </a>
      </router-link>
    </v-col>
    <v-col class="admin-area col-12 pa-0">
      <router-link :to="{ name: 'admin-movie-algorithm' }">
        <a class="admin-href">
          <transition
            @before-enter="movieFadeInUp"
            @enter="enter"
            @after-enter="algorithmCall"
          >
            <div v-show="movieShow" class="admin-text font-weight-bold" data-text="MOVIE">
              MOVIE
            </div>
          </transition>
          <div class="admin-image" :style="{ 'background-image' :avengersImage }"></div>
        </a>
      </router-link>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      userShow: false,
      movieShow: false,
      algorithmShow: false,
    }
  },
  methods: {
    enter(el, done) {
      setTimeout(function() {
        done()
      }, 500)
    },
    userFadeInUp(el) {
      el.classList.add("animated");
      el.classList.add("fadeInUp");
    },
    movieCall(el) {
      this.movieShow = true;
    },
    movieFadeInUp(el) {
      el.classList.add("animated");
      el.classList.add("fadeInUp");
    },
    algorithmCall(el) {
      this.algorithmShow = true;
    },
    algorithmFadeInUp(el) {
      el.classList.add("animated");
      el.classList.add("fadeInUp");
    },
  },
  mounted() {
    var self = this
    setTimeout(function() {
      self.userShow = true;
    }, 500)
  },
  computed: {
    peopleImage() {
      return `url('assets/background-images/Admin/people.jpg')`
    },
    avengersImage() {
      return `url('assets/background-images/Admin/avengers.jpg')`
    }
  }
}
</script>

<style scoped>
.admin-area {
  width: 100%;
  cursor: pointer;
  position: relative;
  text-align: center;
  white-space: normal;
}

.admin-href {
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  cursor: pointer;
  position: absolute;
  justify-content: center;
  display: flex;
  align-items: center;
  overflow: hidden;
}

.admin-href:hover .admin-image {
  transform: scale(1.1);
}

.admin-href:hover .admin-text:before {
  width: 0%;
}

.admin-text {
  z-index: 1;
  position: absolute;
  will-change: opacity;
  font-size: 50px;
  font-weight: 500;
  transform: translate(-50%, -50%);
  backface-visibility: hidden;
  color: white;
  -webkit-text-stroke-width: 1px;
  -webkit-text-fill-color: rgba(0, 0, 0, 0); 
  -webkit-text-stroke-color: white;
}

.admin-text:before {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  overflow: hidden;
  color: red;
  transition: 0.5s;
  -webkit-text-fill-color: white; 
}

.admin-image {
  background-size: cover;
  background-position: 70% 15%;
  opacity: 0.3;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  position: absolute;
  transition: transform 0.8s ease-in-out;
}

.admin-image-user {
  background-size: cover;
  background-position: 70% 50%;
  opacity: 0.3;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  position: absolute;
  transition: transform 0.8s ease-in-out;
}

.admin-href:hover .admin-image-user {
  transform: scale(1.1);
}

.admin-href:hover .admin-text:before {
  width: 0%;
}
</style>