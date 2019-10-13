import api from '../../services/api'

const state = {
  infoList: []
}

const actions = {
  async getAllInfo({ commit }) {
    const resp = await api.getInfo()
    commit('setAllInfo', resp.data)
  }
}

const mutations = {
  setAllInfo(state, info) {
    state.infoList = info
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}