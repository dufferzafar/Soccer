var app = angular.module("instantSearch", ['ngSanitize']);

// Create the instant search filter
app.filter('searchFor', function() {
    return function(arr, searchString) {
        if(!searchString) {
            return [];
        }

        var result = [];
        searchString = searchString.toLowerCase();

        var cnt = 0;
        var perPage = 15;

        for (var i = 0; i < arr.length; i++) {
            if(arr[i].title.toLowerCase().indexOf(searchString) !== -1) {
                result.push(arr[i]);
                cnt++
            }
            if(cnt > perPage) {
                break;
            }
        };
        return result;
    };
});

app.filter('highlight', function($sce) {
    return function (text, search) {
        return $sce.trustAsHtml(text.replace(new RegExp(search, 'gi'), '<span class="highlight">$&</span>'));
    };
});

// The controller
function InstantSearchController($scope) {
    $scope.items = [];

    var urls = [
        "data/projects/2014.json",
        "data/projects/2013.json",
        "data/projects/2012.json",
        "data/projects/2011.json",
        "data/projects/2010.json",
        "data/projects/2009.json",
    ];

    for (var i = 0; i < urls.length; i++) {
        $.ajax({
            url: urls[i]
        }).done(function (data){
            // data=JSON.parse(data);
            Array.prototype.push.apply($scope.items, data.projects);
        });
    };
}
