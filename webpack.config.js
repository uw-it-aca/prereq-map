const path = require("path")
const webpack = require('webpack')
const BundleTracker = require('webpack-bundle-tracker')
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {

  mode: "development",
  context: __dirname,

  entry : {
    vue_curriculum: './prereq_map/static/prereq_map/js/curriculum',
  },

  optimization: {
		splitChunks: {
			cacheGroups: {
				commons: {
					chunks: "initial",
					minChunks: 2,
					maxInitialRequests: 5, // The default limit is too small to showcase the effect
					minSize: 0 // This is example is too small to create commons chunks
				},
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
