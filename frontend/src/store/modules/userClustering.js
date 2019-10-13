const state = {
  cur: {
    isKMeans: false,
    isHierarchical: false,
    isEM: false
  }
}

const mutations = {
  setState(state, cur) {
    if (cur == "K-Means") {
      state.cur.isKMeans = true
      state.cur.isHierarchical = false
      state.cur.isEM = false
    } else if (cur == "Hierarchical") {
      state.cur.isKMeans = false
      state.cur.isHierarchical = true
      state.cur.isEM = false
    } else {
      state.cur.isKMeans = false
      state.cur.isHierarchical = false
      state.cur.isEM = true
    }
  }
}

export default {
  namespaced: true,
  state,
  mutations
}