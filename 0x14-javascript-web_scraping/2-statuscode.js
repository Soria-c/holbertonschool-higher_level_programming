#!/usr/bin/node
const axios = require('axios');

axios
  .get(process.argv[2])
  .then((r) => {
    console.log(`code: ${r.status}`);
  })
  .catch((e) => {
    console.log(`code: ${e.response.status}`);
  });
