var app = angular.module('workloadManagementApp');

    app.factory('Project', ['$resource', 'apiRoot',
        function($resource, apiRoot){
            var result = $resource(apiRoot + 'projects/:id', {id: '@id'},
            {
              'update': { method:'PUT' }
            });
            return result;
        }
    ]);