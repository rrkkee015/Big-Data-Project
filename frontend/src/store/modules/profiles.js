import api from '../../services/api'

// initial state
const state = {
  singleProfile: {
    user: '',
    age: '',
    occupation: '',
    gender: '',
    ratings: [],
  },
  ratingsLength: 0,
  allProfiles: {},
  page: 1
}

const getters = {
  ratingsLength: (state) => {
    if (state.singleProfile) {
      return state.singleProfile.ratings.length
    }
  },
  ratings: (state) => {
    if (state.singleProfile) {
      return state.singleProfile.ratings
    }
  },
  profile: (state) => {
    if (state.singleProfile) {
      return state.singleProfile
    }
  }
}

// actions
const actions = {
  async getSingleProfile({ commit }, nickname) {
    const user = JSON.parse(localStorage.getItem('user'))
    const resp = await api.getSingleProfile(nickname, user.token)
    commit('setRatingsLength', resp.data.ratings.length)
    commit('setSingleProfile', resp.data)
  },

  async editSingleProfile({ commit }, params) {
    const resp = await api.editSingleProfile(params)
    commit('setSingleProfile', resp.data)
    commit('auth/setUser', resp.data, { root: true })
  },

  async getAllProfiles({ commit }, pageNum) {
    const resp = await api.getAllProfiles(pageNum)
    commit('setAllProfiles', resp.data)
  }
}

// mutations
const mutations = {
  setSingleProfile(state, profile) {
    state.singleProfile = profile
  },
  setRatingsLength(state, len) {
    state.ratingsLength = len
  },
  setAllProfiles(state, allProfiles) {
    state.allProfiles = allProfiles
  },
  setPage(state, page) {
    state.page = page
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}