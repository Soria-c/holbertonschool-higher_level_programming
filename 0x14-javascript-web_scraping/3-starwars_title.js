#!/usr/bin/node
const axios = require('axios');

axios.defaults.baseURL = 'https://swapi-api.hbtn.io/api/films/';
axios
  .get(process.argv[2])
  .then((r) => {
    console.log(r.data.title);
  })
  .catch((e) => {
    console.log(e.response.status);
  });
