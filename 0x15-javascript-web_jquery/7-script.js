$.get("https://swapi-api.hbtn.io/api/people/5/?format=json", (data) => {
  console.log(data.name);
  $("#character").text(data.name);
});
