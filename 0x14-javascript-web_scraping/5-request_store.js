#!/usr/bin/node
const axios = require('axios');
const fs = require('fs');

axios.get(process.argv[2]).then((r) => {
  fs.writeFile(process.argv[3], r.data, 'utf-8', (e) => {
    if (e) console.log(e);
  });
});
