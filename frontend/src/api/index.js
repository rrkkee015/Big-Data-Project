import axios from 'axios'

const apiUrl = '/api'

export default {
  searchMovies(params) {
    return axios.get(`${apiUrl}/movies/`, {
      params,
    })
  },
  searchAccounts() {
    return axios.get(`${apiUrl}/profiles/`)
  },
  addViewCount(movieid) {
    return axios.get(`${apiUrl}/movies/`, {
      params : { id: movieid }
    })
  }
}