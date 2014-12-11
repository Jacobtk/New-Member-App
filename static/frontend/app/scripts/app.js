'use strict';

var newMemberApp = angular.module('newMemberApp', [
	'ngRoute',
	'newMemberAppControllers'
]);

newMemberApp.config(
[
	'$routeProvider',
	function($routeProvider)
	{
		$routeProvider.
		when
		('/signin', 
			{
				templateUrl: 'views/signin.html',
				controller : 'SigninController'
			}
		). 
		when
		('/form/:unitName', 
			{
				templateUrl: 'views/form.html',
				controller: 'UserController'
			}
		).
		otherwise
		(
			{
				redirectTo: '/signin'
			}
		);
	}
]);
