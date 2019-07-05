(function(){
	'use strict';
	angular
		.module('src.tanques',[
			'dx',
			'ui.bootstrap',
			'src.tanques.controller',
			'agricola.config',
			])
	angular
		.module('src.tanques.controller',[]);
	angular
		.module('src.tanques')
		.run(run);
	run.$inject=['$http']
	function run($http){
		$http.defaults.xsrfHeaderName='X-CSRFToken';
		$http.defaults.xsrfCookieName='csrftoken';
	}
})();