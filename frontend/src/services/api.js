import axios from 'axios'

// const apiUrl = '/api'
const apiUrl = 'http://52.78.2.29/api'

export default {
  // General
  getInfo() {
    return axios.get(`${apiUrl}/info/`)
  },

  
  // Movies
  searchMovies(params) {
    return axios.get(`${apiUrl}/movies/`, {
      params,
    })
  },
  searchNextMovies(url) {
    return axios.get(url)
  },
  searchMovie(movieId) {
    return axios.get(`${apiUrl}/movies/${movieId}`)
  },
  getRandomMovie() {
    return axios.get(`${apiUrl}/movies/random/`)
  },
  getRecommendedMovies(params) {
    return axios.get(`${apiUrl}/bigdata/recommended/movies`, {params})
  },


  // Profiles
  getAllProfiles(pageNum) {
    var params = {
      "params": { "page": pageNum }
    }
    return axios.get(`${apiUrl}/profiles/`, params)
  },
  getSingleProfile(nickname, token) {
    return axios.get(`${apiUrl}/profiles/${nickname}/`, {headers: {"Authorization": "hnd " + token}})
  },
  editSingleProfile(params) {
    var nickname = params.user
    delete params.user
    return axios.patch(`${apiUrl}/profiles/${nickname}/`, params)
  },

  setRating(params, token) {
    return axios.post(`${apiUrl}/ratings/`, params, {headers: {"Authorization": "hnd " + token}})
  },
  patchRating(ratingId, params, token) {
    return axios.patch(`${apiUrl}/ratings/${ratingId}/`, params, {headers: {"Authorization": "hnd " + token}})
  },

  
  // Authentication
  userRegister(params) {
    return axios.post(`${apiUrl}/auth/register/`, params)
  },
  userLogin(params) {
    return axios.post(`${apiUrl}/auth/login/`, params)
  },
  userCheck(user) {
    return axios.get(`${apiUrl}/auth/user/`, {headers: {"Authorization": "hnd "+ user.token}})
  },
  userLogout(user) {
    return axios.post(`${apiUrl}/auth/logout/`, {headers: {'Authorization': 'hnd '+ user.token}})
  },

  
}
