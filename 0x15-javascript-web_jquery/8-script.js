$.get("https://swapi-api.hbtn.io/api/films/?format=json", (data) => {
  console.log(data);
  for (let i of data.results){
    $("#list_movies").append(`<li>${i.title}</li>`);

  }
});
