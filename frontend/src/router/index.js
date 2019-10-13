import Vue from 'vue'
import VueRouter from 'vue-router'
import LandingPage from '../pages/LandingPage'
import MainPage from '../pages/MainPage'
import MovieSearchPage from '../pages/MovieSearchPage'
import MovieDetailPage from '../pages/MovieDetailPage'
import ProfileDetailPage from '../pages/ProfileDetailPage'
import ProfileEditPage from '../pages/ProfileEditPage'
import AboutUsPage from '../pages/AboutUsPage'
import RatingPage from '../pages/RatingPage'

import AdminHomePage from '../pages/AdminHomePage'
import AdminUserListPage from '../pages/AdminUserListPage'
import AdminAlgorithmSelectPage from '../pages/AdminAlgorithmSelectPage'
import AdminUserClusteringPage from '../pages/AdminUserClusteringPage'
import AdminMovieAlgorithmPage from '../pages/AdminMovieAlgorithmPage'
import AdminMovieClusteringPage from '../pages/AdminMovieClusteringPage'
import AdminMovieRecommendationPage from '../pages/AdminMovieRecommendationPage'

import random from '../store/modules/random'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: LandingPage, name: 'landing' },
    { path: '/main', component: MainPage, name: 'home',
      beforeEnter: (from, to ,next) => {
        random.state.movieRandomList = [] 
        next()
      } },
    { path: '/movies/search', component: MovieSearchPage, name: 'movie-search' },
    { path: '/movies/:movieId', component: MovieDetailPage, name: 'movie-detail'},

    { path: '/profiles/:nickname', component: ProfileDetailPage, name: 'profile-detail' },
    { path: '/profiles/:nickname/setting', component: ProfileEditPage, name: 'profile-setting' },

    { path: '/aboutus', component: AboutUsPage, name: 'about-us' },

    { path: '/rating', component: RatingPage, name: 'rating'},

    { path: '/admin', component: AdminHomePage, name: 'admin-home' },
    { path: '/admin/userlist', component: AdminUserListPage, name: 'admin-userlist' },
    { path: '/admin/select', component: AdminAlgorithmSelectPage, name: 'admin-algorithm-select' },
    { path: '/admin/user/clustering', component: AdminUserClusteringPage, name: 'admin-user-clustering' },
    { path: '/admin/movie/algorithm', component: AdminMovieAlgorithmPage, name: 'admin-movie-algorithm' },
    { path: '/admin/movie/clustering', component: AdminMovieClusteringPage, name: 'admin-movie-clustering' },
    { path: '/admin/movie/recommendation', component: AdminMovieRecommendationPage, name: 'admin-movie-recommendation' }
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router