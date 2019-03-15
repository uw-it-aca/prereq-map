const path = require("path")
const webpack = require('webpack')
const BundleTracker = require('webpack-bundle-tracker')
const VueLoaderPlugin = require('vue-loader/lib/plugin')

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

    new BundleTracker({filename: './webpack-stats.json'}),
    new VueLoaderPlugin(),

  ],

  module: {
      rules: [
          {
              test: /\.vue$/,
              loader: 'vue-loader'
          },
          {
              test: /\.(css|scss|less)/,
              loaders: ['style-loader', 'css-loader', 'sass-loader', 'less-loader']
          }
      ]
  },

  resolve: {
    extensions: ['.js']
  }

}
