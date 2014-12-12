var constants = angular.module('frontendApp.constants', []);

this.createServerRoot = function(){
  var currentUrl = window.location.href;

  if(currentUrl.indexOf('localhost') > -1 || currentUrl.indexOf('127.0.0') > -1){
    return 'http://localhost:8000/api/';
  } else{
    return 'http://104.131.150.102:8000/api/';
  }
};

this.createApiVersion = function(){ return 'v1'};

this.createApiRoot = function(){
  return this.createServerRoot() + this.createApiVersion() + '/';
};

constants.constant('serverRoot', this.createServerRoot());
constants.constant('apiVersion', this.createApiVersion());
constants.constant('apiRoot', this.createApiRoot());