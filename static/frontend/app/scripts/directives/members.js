(function() {
	var app = angular.module('NewMember', ['new-member-table']);

})();

(function() {
	var app = angular.module('new-member-table', ['frontendApp.constants', 'ngResource']);

	app.directive("memberTable", ["$http", 'apiRoot', '$resource', function(apiRoot, $resource) {
		return {
			restrict: 'E',
			templateUrl: "templates/new-member-table.html",

			controller: function($http, apiRoot, $resource) {

				this.newMembers = $resource(apiRoot + 'members', 
					{'query': { method:'GET', isArray:true }}).query();

				// $http
			 //      .get('scripts/data.json')
			 //      .success(function(data){
			 //        table.newMembers = data;
			 //      })
			 //      .error(function(data, statusCode, headers, config){
			 //        console.log("Something's not right..." + data);
			 //      });

			},
			controllerAs: 'newMemberCtrl'
		};
	}]);

})();