const path = require("path")
const webpack = require('webpack')
const BundleTracker = require('webpack-bundle-tracker')
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const CleanWebpackPlugin = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

module.exports = {

    mode: "development",
    context: __dirname,

    entry: {
        base: './prereq_map/static/prereq_map/js/base.js',
        curriculum: './prereq_map/static/prereq_map/js/pages/curriculum/index.js',
        course: './prereq_map/static/prereq_map/js/pages/course/index.js'
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
        new BundleTracker({
            filename: './prereq_map/static/webpack-stats.json'
        }),
        new VueLoaderPlugin(),
        new MiniCssExtractPlugin({
            filename: "[name]-[hash].css",
        })
    ],

    module: {
        rules: [{
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.s[ac]ss$/,
                use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"]
            },
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader, "css-loader"]
            }
        ]
    },

    resolve: {
        extensions: ['.js']
    }

}
