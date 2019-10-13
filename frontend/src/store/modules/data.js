import api from '../../services/api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  previous: '',
  next: '',
  movie : {}
}

// getters
const getters = {
  getNextUrl(state) {
    return state.next
  },
  getMovie(state) {
    return state.movie
  }
}

// actions
const actions = {
  async searchMovies({ commit }, params) {
    const resp = await api.searchMovies(params)
    commit('setNextMovieListUrl', resp.data.next)
    const movies = resp.data.results.map(movie => ({
      id: movie.id,
      title: movie.title,
      genres: movie.genres_array.join(' / '),
      released: movie.released,
      runtime: movie.runtime,
      viewCnt: movie.view_count,
      poster: movie.poster,
      imdbRating: movie.imdb_rating,
      imdbVote: movie.imdb_vote,
      imdbId: movie.imdbId,
    }))
    // for (var i = 0; i < movies.length; i++) {
    //   if (movies[i].tags != '') {
    //     movies[i].tags = '#' + movies[i].tags
    //   }
    // }
    commit('setMovieSearchList', movies)
  },
  sortByRating({ commit }) {
    commit('sortByRating')
  },
  async getAllMovies({state, commit}) {
    const resp = await api.getAllMovies()
    console.log(resp)
  },
  async searchNextMovies({ state, commit }) {
    const resp = await api.searchNextMovies(state.next)
    commit('setNextMovieListUrl', resp.data.next)
    const movies = resp.data.results.map(movie => ({
      id: movie.id,
      title: movie.title,
      genres: movie.genres_array.join(' / '),
      released: movie.released,
      runtime: movie.runtime,
      viewCnt: movie.view_count,
      poster: movie.poster,
      imdbRating: movie.imdb_rating,
      imdbVote: movie.imdb_vote,
      imdbId: movie.imdbId,
    }))
    commit('setMovieNextList', movies)
  },

  async searchNextMovies({ state, commit }) {
    const resp = await api.searchNextMovies(state.next)
    commit('setNextMovieListUrl', resp.data.next)
    const movies = resp.data.results.map(movie => ({
      id: movie.id,
      title: movie.title,
      genres: movie.genres_array.join(' / '),
      released: movie.released,
      runtime: movie.runtime,
      viewCnt: movie.view_count,
      poster: movie.poster,
      imdbRating: movie.imdb_rating,
      imdbVote: movie.imdb_vote,
      imdbId: movie.imdbId,
    }))
    commit('setMovieNextList', movies)
  },

  async searchMovie({ commit }, movieId) {
    const resp = await api.searchMovie(movieId)
    let temp = []
    let tag_arr = []
    const movie = {
      id: resp.data.id,
      title: resp.data.title,
      genres: resp.data.genres_array.join(' / '),
      year: resp.data.year,
      released: resp.data.released,
      runtime: resp.data.runtime,
      viewCnt: resp.data.view_count,
      director: resp.data.director,
      writer: resp.data.writer,
      cast: resp.data.cast,
      tags: resp.data.tags_array,
      fullPlot: resp.data.full_plot,
      shortPlot: resp.data.short_plot,
      trailer: resp.data.trailer,
      poster: resp.data.poster,
      metascore: resp.data.metascore,
      imdbRating: resp.data.imdb_rating,
      imdbVote: resp.data.imdb_vote,
      imdbId: resp.data.imdbId,
      movielensId: resp.data.movielensId,
      tmdbId: resp.data.tmdbId,
      youtubeId: resp.data.youtubeId
    }
    for (var i = 0; i < movie.tags.length; i++) {
      temp.push(movie.tags[i])
      if (temp.length === 10){
        tag_arr.push('#' + temp.join(' #'));
        temp = [];
      }
    }
    if (temp.length != 0) {
      tag_arr.push('#' + temp.join(' #'))
    }
    movie.tags = tag_arr;
    commit('setMovie', movie)
  },

  async getRecomendedMovies({ commit }, userId) {
    parmas = {"user_id" : userId }
    const resp = await api.searchMovies(params)
    console.log(resp)

  }
}

// mutations
const mutations = {
  setMovieSearchList(state, movies) {
    state.movieSearchList = movies
  },
  setMovieNextList(state, movies) {
    state.movieSearchList = state.movieSearchList.concat(movies)
  },
  setNextMovieListUrl(state, nextUrl) {
    state.next = nextUrl
  },
  setMovie(state, movie) {
    state.movie = movie
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}