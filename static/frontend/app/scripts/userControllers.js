'use strict';

var newMemberAppControllers = angular.module('newMemberAppControllers', []);

newMemberAppControllers.controller('UserController', ['$scope', '$routeParams',
function($scope, $routeParams) {
	
	$scope.unitName = $routeParams.unitName;
	$scope.fields = [
	{'fieldName': 'Name',
	'placeHolder': 'Your Name *',
	'requiredMessage': 'Please enter your name.'},
	{'fieldName': 'YearInSchool',
	'placeHolder': 'Your Year In School *',
	'requiredMessage': 'Please enter your year in school.'}, 
	{'fieldName': 'Name',
	'placeHolder': 'Your Name *',
	'requiredMessage': 'Please enter your name.'},
	{'fieldName': 'YearInSchool',
	'placeHolder': 'Your Year In School *',
	'requiredMessage': 'Please enter your year in school.'},
	{'fieldName': 'Name',
	'placeHolder': 'Your Name *',
	'requiredMessage': 'Please enter your name.'},
	{'fieldName': 'YearInSchool',
	'placeHolder': 'Your Year In School *',
	'requiredMessage': 'Please enter your year in school.'}  
	];
 
  	$scope.currentUser = "Bob";
  	$scope.submitted = false;
/*  get fields from the database   */
  
}]);

newMemberAppControllers.controller('SigninController', ['$scope',
function($scope){
	$scope.garbage = "LEMONS!!";
	
}]);

