'use strict';

var newMemberAppControllers = angular.module('newMemberApp');

newMemberAppControllers.controller('UserController', ['$scope', '$routeParams', '$resource', 'apiRoot',
function($scope, $routeParams, $resource, apiRoot) {

  $scope.unit = $resource(apiRoot + 'unit').query();
  $scope.customFields = $resource(apiRoot + 'unit/' + $routeParams.unitID + '/entries');

  $scope.foo = apiRoot;
  $scope.members = $resource(apiRoot + 'members').query();



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

