const state = {
  navBarShow: true,
  infoSnackbarShow: false,
}

const mutations = {
  checkNavBar(state, toggle) {
    state.navBarShow = toggle
  },
  toggleProfileSnackBar(state, toggle) {
    state.infoSnackbarShow = toggle
  }
}

export default {
  namespaced: true,
  state,
  mutations
}