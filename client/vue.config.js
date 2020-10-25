var path = require("path")

module.exports = {
	publicPath : '',
	devServer : {
		proxy : { // proxyTable 설정
			'/api' : {
				target : 'https://osam-server.run.goorm.io/api',
				changeOrigin : true,
				pathRewrite : {
					'^/api' : ''
				}
			}
		},
		disableHostCheck : true,
	},
	outputDir : path.resolve(__dirname, "../server/public/"),
}