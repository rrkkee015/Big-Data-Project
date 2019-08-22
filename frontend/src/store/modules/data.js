import api from '../../api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  accountList: [],
}

// actions
const actions = {
  async searchMovies({ commit }, params) {
    const resp = await api.searchMovies(params)
    const movies = resp.data.map(d => ({
      id: d.id,
      title: d.title,
      genres: d.genres_array,
      viewCnt: d.view_cnt,
      rating: d.average_rating,
    }))

    commit('setMovieSearchList', movies)
  },
  async searchAccounts({ commit }, params) {
    const resp = await api.searchAccounts(params)
    const accounts = resp.data.map(d => ({
      user: d.user,
      username: d.username,
      gender: d.gender,
      occupation: d.occupation,
      age: d.age
    }))

    commit('setAccountsList', accounts)
  }
}

// mutations
const mutations = {
  setMovieSearchList(state, movies) {
    state.movieSearchList = movies.map(m => m)
  },
  setAccountsList(state, accounts) {
    state.accountList = accounts.map(m => m)
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}