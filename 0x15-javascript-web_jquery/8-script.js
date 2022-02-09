// Add a list of the titles of all the movies to the UL#list_movies element
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data, status){
    for (let movie in data.results) {
        $('ul#list_movies').append(`<li>${movie.title}</li>`);
    }
});