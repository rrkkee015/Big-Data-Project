const state = {
  cur: {
    isKnn: false,
    isMf: false,
  }
}

const mutations = {
  setState(state, cur) {
    if (cur == "KNN") {
      state.cur.isKnn = true
      state.cur.isMf = false
    } else {
      state.cur.isKnn = false
      state.cur.isMf = true
    }
  }
}

export default {
  namespaced: true,
  state,
  mutations
}