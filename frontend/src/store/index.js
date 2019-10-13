import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import data from './modules/data'
import profiles from './modules/profiles'
import info from './modules/info'
import random from './modules/random'
import entrance from './modules/entrance'
import rating from './modules/rating'
import userClustering from './modules/userClustering'
import movieClustering from './modules/movieClustering'
import movieRecommendation from './modules/movieRecommendation'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth,
    data,
    profiles,
    info,
    random,
    entrance,
    rating,
    userClustering,
    movieClustering,
    movieRecommendation
  },
})