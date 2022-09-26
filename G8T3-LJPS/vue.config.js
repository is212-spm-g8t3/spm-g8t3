module.exports = {
	runtimeCompiler: true,

	chainWebpack: config => {
		config
			.plugin('html')
			.tap(args => {
				args[0].title = 'Learning Journey Planning System - G8T3'
				return args
			})
	}
}
