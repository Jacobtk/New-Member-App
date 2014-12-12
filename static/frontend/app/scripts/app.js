'use strict';

var newMemberApp = angular.module('newMemberApp', [
	'ngRoute',
    'ngResource',
    'frontendApp.constants'
//    ,
//	'newMemberAppControllers'
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
		('/thankyou/:unitID',
			{
				templateUrl: 'views/thankyou.html',
				controller: 'UserController'
			}
		).
		when
		('/form/:unitID', 
			{
				templateUrl: 'views/form.html',
				controller: 'UserController'
			}
		).
		when
		('/lists/new/:unitName',
			{
				templateUrl: 'views/new-members.html',
				controller: 'SigninController'
			}
		).
		when
		('/lists/current/:unitName',
			{
				templateUrl: 'views/members.html',
				controller: 'SigninController'
			}
		);
	}
]);
