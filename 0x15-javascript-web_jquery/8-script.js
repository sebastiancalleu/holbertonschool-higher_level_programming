fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(function(data){
    for (let i = 0; i < data.results.length; i++) {
      $("#list_movies").append("<li>"+data.results[i].title+"</li>")
    }
  });
