import api from '@/services/api'
import router from '@/router'

const state = {
  profile: null,
  error: null,
  signInError: null,
  signUpError: null,
  loading: false,
}


const getters = {
	isAuthenticated (state) {
    return state.profile !== null && state.profile !== undefined
  },
  profileUser: (state) => {
    if (state.profile) {
      return state.profile
    }
  }
}


const actions = {
  async userRegister({commit}, payload) {
    commit('setLoading', true)
    await api.userRegister(payload).then(resp => {
      commit('setLoading', false)
    }).catch(err => {
      commit('setError', err.message)
      commit('setSignUpError', err.message)
      commit('setLoading', false)
    })
  },
  
  async userLogin({commit}, payload) {
    commit('setLoading', true)
    await api.userLogin(payload).then(resp => {
      localStorage.setItem('user', JSON.stringify(resp.data.user))
      commit('setUser', resp.data.profile)
      commit('setLoading', false)
    }).catch(err => {
      commit('setSignInError', err.message)
      commit('setLoading', false)
    })
  },

  userLogout({commit}) {
    commit('setLoading', true)
    const user = JSON.parse(localStorage.getItem('user'))
    api.userLogout(user).then(() => {
      localStorage.removeItem('user')
      commit('setUser', null)
      commit('setLoading', false)
      alert('Completed logged out.')
      router.push({name: 'landing'})
    }).catch(err => {
      localStorage.removeItem('user')
      commit('setUser', null)
      commit('setError', err.message)
      commit('setLoading', false)
      router.push({name: 'landing'})
    })
  },

  async autoLogin({commit}) {
    commit('setLoading', true)
    const user = JSON.parse(localStorage.getItem('user'))
    await api.userCheck(user).then(resp => {
      if (resp.data.username === user.username) {
        commit('setUser', resp.data.profile)
        commit('setLoading', false)
      } else {
        localStorage.removeItem('user')
        commit('setUser', null)
        commit('setLoading', false)
        alert('The session has expired due to inactivity.')
        router.push({name: 'landing'})
      }
      commit('setLoading', false)
    }).catch(err => {
      localStorage.removeItem('user')
      commit('setError', err.message)
      commit('setUser', null)
      commit('setLoading', false)
      router.push({name: 'landing'})
    })
  }
}


const mutations = {
  setUser(state, payload) {
    state.profile = payload
  },
  setError(state, payload) {
    state.error = payload
  },
  setSignInError(state, payload) {
    state.signInError = payload
  },
  setSignUpError(state, payload) {
    state.signUpError = payload
  },
  setLoading(state, payload) {
    state.loading = payload
  },
  initError(state) {
    state.signUpError = null
    state.signInError = null
  }
}


export default {
  namespaced: true,
	state,
	getters,
  actions,
  mutations
}