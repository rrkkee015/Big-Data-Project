<template>
  <v-container>
    <v-layout class="justify-sm-center justify-lg-end iphone-ml-0">
      <video autoplay loop muted class="darkness">
        <source src="assets/aboutus_video.mp4" type="video/mp4">
      </video>
    </v-layout>
    <v-layout class="white--text">
      <v-flex>
        <v-row class="skew">
          <div class="skew-y30">
            <transition
              @before-enter="skillFadeInUp"
              @enter="enter"
              @after-enter="clusteringCall"
            >
              <p v-show="skillShow"><span class="display-1 font-weight-bold">SKILL STACK</span> <br>
                Python 3.6.3 <br>
                Django 2.1.7 <br>
                Django REST Framwork <br>
                Vue, VueX, Vue-router <br>
                Vue, VueX, Vue-router <br>
                Vue, VueX, Vue-router <br>
                Vue, VueX, Vue-router <br>
              </p>
            </transition>
          </div>
          <div class="skew-y-30">
            <transition
              @before-enter="clusteringFadeInUp"
              @enter="enter"
              @after-enter="teamCall"
            >
              <div v-show="clusteringShow" class="font-weight-medium">
                <p class="mb-0 font-weight-black">Clustering</p>
                <a
                  href="https://lab.ssafy.com/HyehuiLee/bigdata-sub3/blob/algorithm-ksj/algorithm/dd.md" 
                  target="_blank"
                  class="mb-0 d-block stroke"
                >
                  K-means
                </a>
                <a
                  href="https://lab.ssafy.com/HyehuiLee/bigdata-sub3/blob/algorithm-ksj/algorithm/dd.md" 
                  target="_blank"
                  class="mb-0 d-block stroke"
                >
                  expectation- <br>
                  maximization
                </a>
                <a
                  href="https://lab.ssafy.com/HyehuiLee/bigdata-sub3/blob/algorithm-ksj/algorithm/dd.md" 
                  target="_blank"
                  class="mb-0 d-block stroke"
                >
                  hierarchical
                </a>
              </div>
            </transition>
          </div>
          <div class="skew-x61-y-30">
            <transition
              @before-enter="teamFadeInUp"
            >
              <p v-show="teamShow"  class="caption">Hey &Nerd <br>
                The Hey <span style="color: red;">&</span>Nerd is a recommendation site build movie database.
                We added the film from 1894 to the database.
                We help you jog your memory about a movie, find the best movie to watch next.
                For users deciding what to watch, we offer the trailer, story, information of movie.
                Just enjoy hey <span style="color: red;">&</span>Nerd's service.
              </p>
            </transition>
          </div>
        </v-row>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      skillShow: false,
      clusteringShow: false,
      teamShow: false
    }
  },
  methods: {
    enter(el, done) {
      setTimeout(function() {
        done()
      }, 500)
    },
    skillFadeInUp(el) {
      el.classList.add("animated");
      el.classList.add("fadeInLeft");
    },
    clusteringCall(el) {
      this.clusteringShow = true
    },
    clusteringFadeInUp(el) {
      el.classList.add("animated");
      el.classList.add("fadeInRight");
    },
    teamCall(el) {
      this.teamShow = true
    },
    teamFadeInUp(el) {
      el.classList.add("animated");
      el.classList.add("fadeInUp");
    }
  },
  mounted() {
    this.skillShow = true;
  }
}
</script>

<style scoped>
  >>> a {
    color: rgb(255, 255, 255) !important;
    text-decoration: none;
  }
  .darkness {
    filter: brightness(.3);
  }
  /* iPhone 5/SE ~ */
  @media (max-width: 320px) {
    .iphone-ml-0 {
      margin: 0px -80px;
      width: 100%;
    }
    .skew {
      padding: 0px 4px;
    }
    .skew .skew-y-30 {
      font-size: 44px;
      line-height: 3rem;
      text-transform: uppercase;
      }
    .stroke {
    color: white;
    -webkit-text-fill-color: rgba(0, 0, 0, 0); 
    -webkit-text-stroke-width: 1px;
    -webkit-text-stroke-color: white;
    }
  }
  /* iPhone X ~ */
  @media (min-width: 321px) and (max-width: 375px) {
    .iphone-ml-0 {
      margin: 0px -55px;
      width: 100%;
    }
    .skew {
      padding: 7px;
    }
    .skew .skew-y-30 {
      font-size: 50px;
      line-height: 3.5rem;
      text-transform: uppercase;
      }
    .stroke {
    color: white;
    -webkit-text-fill-color: rgba(0, 0, 0, 0);
    -webkit-text-stroke-width: 1px;
    -webkit-text-stroke-color: white;
    }
  }
  /* iPhone 6/7/8 plus ~ */
  @media (min-width: 376px) and (max-width: 414px) {
    .iphone-ml-0 {
      margin: 0px -40px;
    }
    .skew {
      padding: 10px;
    }
    .skew .skew-y-30 {
      font-size: 55px;
      line-height: 3.55rem;
      text-transform: uppercase;
      }
    .stroke {
      color: white;
      -webkit-text-fill-color: rgba(0, 0, 0, 0); 
      -webkit-text-stroke-width: 1px;
      -webkit-text-stroke-color: white;
    }
  } 
  /* iPad ~ */
  @media (min-width: 415px) and (max-width: 1024px) {
    .skew {
      padding: 10px 50px;
    }
    .skew .skew-y30 {
      margin-right: 50px;
      }
    .skew .skew-y-30 {
      font-size: 60px;
      line-height: 3.75rem;
      text-transform: uppercase;
      }
    .stroke {
      color: white;
      -webkit-text-fill-color: rgba(0, 0, 0, 0);
      -webkit-text-stroke-width: 2px;
      -webkit-text-stroke-color: white;
    }
  }
  @media (min-width: 1025px) {
    .skew .skew-y30 {
      position:fixed;
      top: 360px;
      left: 210px;
      text-align: right;
      transform: skew(0deg, 30deg);
      }
    .skew .skew-y-30 {
      font-size: 60px;
      line-height: 3.75rem;
      position:fixed;
      left: 470px;
      top: 228px;
      text-transform: uppercase;
      transform: skew(0deg, -30deg);
      }
    .skew .skew-x61-y-30 {
      position: fixed;
      left: 580px;
      top: 510px;
      min-width: 400px;
      max-width: 500px;
      transform: skew(61deg, -30deg);
      }
    .stroke {
      color: white;
      -webkit-text-fill-color: rgba(0, 0, 0, 0);
      -webkit-text-stroke-width: 2px;
      -webkit-text-stroke-color: white;
      }
    .stroke:hover {
      color: white;
      -webkit-text-fill-color: white; 
      -webkit-text-stroke-width: 2px;
      -webkit-text-stroke-color: white;
      }
    }
  /* vuetify xl에서 container margin 없어지는 문제  해결하기 위해 ....*/
  @media (min-width: 1904px) {
   .container {
      max-width: 1264px;
    }
  }
</style>