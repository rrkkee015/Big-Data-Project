import api from '../../services/api'

// initial state
const state = {
  movieRandomList: [],
}

// actions
const actions = {
  async getRandomMovie({ commit }) {
    const resp = await api.getRandomMovie()
    const movies = resp.data.map(movie => ({
      id: movie.id,
      title: movie.title,
      genres: movie.genres_array.join(' / '),
      year: movie.year,
      released: movie.released,
      runtime: movie.runtime,
      viewCnt: movie.view_count,
      director: movie.director,
      writer: movie.writer,
      cast: movie.cast,
      fullPlot: movie.full_plot,
      shortPlot: movie.short_plot,
      trailer: movie.trailer,
      poster: movie.poster,
      metascore: movie.metascore,
      imdbRating: movie.imdb_rating,
      imdbVote: movie.imdb_vote,
      imdbId: movie.imdbId,
      movielensId: movie.movielensId,
      tmdbId: movie.tmdbId,
      youtubeId: movie.youtubeId
    }))
    commit('setRandomMovieList', movies)
  }
}

// mutations
const mutations = {
  setRandomMovieList(state, movies) {
    state.movieRandomList = movies.map(m => m)
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}