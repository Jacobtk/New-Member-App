'use strict';

var newMemberAppControllers = angular.module('newMemberApp');

newMemberAppControllers.controller('UserController', ['$scope', '$routeParams', '$resource', 'apiRoot',
function($scope, $routeParams, $resource, apiRoot) {

	$scope.unitID = $routeParams.unitID;

  $scope.unit = $resource(apiRoot + 'units/' + $scope.unitID, {
          'query': { method:'GET', isArray:false }
        }).get();
  $scope.customFields = $resource(apiRoot + 'unit/' + $routeParams.unitID + '/entries').query();

  $scope.foo = apiRoot;
  $scope.members = $resource(apiRoot + 'members').query();

  $scope.currentUser = "Bob";
  $scope.submitted = false;
/*  get fields from the database   */
}]);

newMemberAppControllers.controller('SigninController', ['$scope',
function($scope){
	$scope.garbage = "LEMONS!!";
	
}]);

