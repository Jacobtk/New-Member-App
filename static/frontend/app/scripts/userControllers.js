'use strict';

var newMemberAppControllers = angular.module('newMemberAppControllers', []);

newMemberAppControllers.controller('UserController', ['$scope', '$routeParams',
function($scope, $routeParams) {
	
	$scope.unitID = $routeParams.unitID;
	$scope.fields = [
	
	];
 
  	$scope.currentUser = "Bob";
  	$scope.submitted = false;
/*  get fields from the database   */
  
}]);

newMemberAppControllers.controller('SigninController', ['$scope',
function($scope){
	$scope.garbage = "LEMONS!!";
	
}]);

