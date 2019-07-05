(function(){
	'use  strict';
	angular
		.module('src.tanques.controller')
		.controller('Tanques',TanquesController);
	TanquesController.$inject=['$http','$scope'];
	function TanquesController($http,$scope){
		var vm = this;
		$scope.valor="Angular funcionando";
	}
})();