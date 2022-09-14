#!/usr/bin/node
const axios = require('axios');

const promises = [];
axios.defaults.baseURL = 'https://swapi-api.hbtn.io/api/films/';
axios
  .get(process.argv[2])
  .then((r) => {
    for (const i of r.data.characters) {
      promises.push(axios.get(i));
    }
    Promise.all(promises)
      .then((r) => {
        for (const j of r) {
          console.log(j.data.name);
        }
      })
      .catch((e) => console.log(e));
  })
  .catch((e) => console.log(e));
