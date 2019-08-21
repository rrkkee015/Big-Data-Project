import Vue from 'vue'
import VueRouter from 'vue-router'
import EmptyPage from '../components/pages/EmptyPage'
import MovieSearchPage from '../components/pages/MovieSearchPage'
import GenreSearchPage from '../components/pages/GenreSearchPage'
import AccountsPage from '../components/pages/AccountsPage'
Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: EmptyPage, name: 'home' },
    { path: '/movies/search', component: MovieSearchPage, name: 'movie-search' },
    { path: '/genres/search', component: GenreSearchPage, name: 'genre-search' },
    { path: '/accounts', component: AccountsPage, name: 'accounts' },
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router