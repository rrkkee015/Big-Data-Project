import api from '../../api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  // shape: [{ id, username, is_staff, ratings, gender, age, occupation, user}]
  accountList: []
}

// actions
const actions = {
  async searchMovies({ commit }, params) {
    const resp = await api.searchMovies(params)
    const movies = resp.data.map(d => ({
      id: d.id,
      title: d.title,
      genres: d.genres_array,
      viewCount: d.view_cnt,
      averageRating: d.average_rating,
      users: d.ratings,
    }))

    commit('setMovieSearchList', movies)
  },
  async searchAccounts({ commit }) {
    const resp = await api.searchAccounts()
    const accounts = resp.data.map(d => ({
      user: d.user,
      username: d.username,
      gender: d.gender,
      occupation: d.occupation,
      age: d.age,
      ratings: d.ratings
    }))

    commit('setAccountsList', accounts)
  },
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