#!/usr/bin/node
const axios = require('axios');

let numberOfAppearances = 0;
axios.get(process.argv[2]).then((r) => {
  for (const i of r.data.results) {
    for (const j of i.characters) {
      const ar = j.split('/');
      if (ar[ar.length - 2] === '18') numberOfAppearances++;
    }
  }
  console.log(numberOfAppearances);
});
