const path = require('path');

module.exports = {
  entry: './src/front/index.js',
  output: {
    path: path.resolve('src/static/'),
    filename: 'index_bundle.js',
    publicPath: ""
  },
  module: {
    rules: [
      { test: /\.js$/, loader: 'babel-loader', exclude: /node_modules/ }
    ]
  },
  devServer: {
    contentBase: [path.resolve(__dirname, 'src'), path.resolve(__dirname, 'src/static')],
    index: 'index.html',
    historyApiFallback: true,
    proxy: {
      '/api': 'http://localhost:5000'
    }
  },
  optimization: {
    minimize: false
  }
}
