import axios from 'axios'

const clusterUrl = '/cluster'

export default {
    getClusterMovieKmeans(params) {
        return axios.get(`${clusterUrl}/movie/kmeans`, {
        params,
        })
    },
}
