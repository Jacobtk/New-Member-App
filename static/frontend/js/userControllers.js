'use strict';

var newMemberApp = angular.module('newMemberApp', []);

newMemberApp.controller('UserController', function($scope, $http) {
	
	$scope.unitName = "BYU Party Ward";
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
  
});

