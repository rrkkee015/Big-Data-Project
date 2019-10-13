import api from '../../services/api'
import router from '@/router'

// initial state
const state = {
  error: null,
	loading: false,
	
	ratingCnt: 0,
	newRatings: {},
}

const getters = {
	newRatings(state) {
		return state.newRatings
	}
}

// actions
const actions = {
	setRating({commit}, payload) {
		commit('setLoading', true)
		const user = JSON.parse(localStorage.getItem('user'))
		/*
		payload: {
			"rating": 4,
			"movieId": 1
		}
		*/
		api.setRating(payload, user.token).then(resq => {
			commit('setLoading', false)
		}).catch(err => {
			commit('setError', err.message)
			commit('setLoading', false)
		})
	},
	setRatings({commit}, payload) {
		commit('setLoading', true)
		const user = JSON.parse(localStorage.getItem('user'))
		/*
		payload: {
			movieId: rating,
			movieId: rating,
			...
		}
		*/
		const newRatings = payload
		for (var key in newRatings) {
			var movieId = key
			var score = newRatings[key]
			api.setRating({'rating': score, 'movieId': movieId}, user.token).then(resq => {
				commit('setLoading', false)
				router.push({name: 'home'})
			}).catch(err => {
				commit('setError', err.message)
				commit('setLoading', false)
			})
		}
	},

	patchRating({commit}, payload) {
		commit('setLoading', true)
		const user = JSON.parse(localStorage.getItem('user'))
		api.patchRating(payload.ratingId, payload.params, user.token).then(resq => {
			commit('setLoading', false)
		}).catch(err => {
			commit('setError', err.message)
			commit('setLoading', false)
		})
	}
}

// mutations
const mutations = {
	setError(state, payload) {
    state.error = payload
  },
  setLoading(state, payload) {
    state.loading = payload
	},
	initRatingCnt(state) {
		state.ratingCnt = 0
		state.newRatings = {}
	},
	collectRating(state, newRating) {
		state.newRatings[newRating[0]] = newRating[1]
	},
	deleteCollectedRating(state, movieId) {
		delete state.newRatings[movieId];
	},
	countCollectedRating(state) {
		Object.size = function(obj) {
			var size = 0, key;
			for (key in obj) {
				if (obj.hasOwnProperty(key)) size++;
			}
			return size;
		};
		state.ratingCnt = Object.size(state.newRatings)
	},
}

export default {
  namespaced: true,
	state,
	getters,
  actions,
  mutations
}