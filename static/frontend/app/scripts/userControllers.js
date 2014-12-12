'use strict';

var newMemberAppControllers = angular.module('newMemberAppControllers', []);

newMemberAppControllers.controller('UserController', ['$scope', '$routeParams',
function($scope, $routeParams) {
	
	$scope.unitName = $routeParams.unitName;
	$scope.fields = [1,2,3,45,6,7844

	];
 
  	$scope.currentUser = "Bob";
  	$scope.submitted = false;
/*  get fields from the database   */
  
}]);

newMemberAppControllers.controller('SigninController', ['$scope',
function($scope){
	$scope.garbage = "LEMONS!!";
	
}]);

