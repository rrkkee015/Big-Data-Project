module.exports = {
  publicPath: '/',
  devServer: {
    proxy: {
      '/api': {
        // target: 'http://localhost:8000/',
        target: 'http://52.78.2.29/',
      },
      '/cluster': {
        // target: 'http://localhost:8000/',
        target: 'http://52.78.2.29/',
      },
      '/static/posters': {
        target: 'http://localhost:8000/',
      },
    }
  },
  lintOnSave: false
}