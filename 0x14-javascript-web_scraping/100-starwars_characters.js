#!/usr/bin/node
const axios = require('axios');

axios.defaults.baseURL = 'https://swapi-api.hbtn.io/api/films/';
axios.get(process.argv[2]).then((r) => {
  for (const i of r.data.characters) {
    axios.get(i).then((rr) => {
      console.log(rr.data.name);
    }).catch(e => console.log(e));
  }
}).catch(e => console.log(e));
