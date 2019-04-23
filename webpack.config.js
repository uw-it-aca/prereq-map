const path = require("path")
const webpack = require('webpack')
const BundleTracker = require('webpack-bundle-tracker')
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const CleanWebpackPlugin = require('clean-webpack-plugin');

module.exports = {

  mode: "development",
  context: __dirname,

  entry : {
    vue_curriculum: './prereq_map/static/prereq_map/js/curriculum',
    vue_course: './prereq_map/static/prereq_map/js/course'
  },

  optimization: {
		splitChunks: {
			cacheGroups: {
				vendor: {
					test: /node_modules/,
					chunks: "initial",
					name: "vendor",
					priority: 10,
					enforce: true
				}
			}
		}
	},

  output: {
      path: path.resolve('./prereq_map/static/prereq_map/bundles/'),
      filename: "[name]-[hash].js",
  },

  plugins: [
    new CleanWebpackPlugin(),
    new BundleTracker({filename: './prereq_map/static/webpack-stats.json'}),
    new VueLoaderPlugin(),
  ],

  module: {
      rules: [
          {
              test: /\.vue$/,
              loader: 'vue-loader'
          },
          {
              test: /\.(css|scss)/,
              loaders: ['style-loader', 'css-loader', 'sass-loader']
          }
      ]
  },

  resolve: {
    extensions: ['.js']
  }

}
