#!/usr/bin/node
const axios = require('axios');

const users = {};
axios.get(process.argv[2]).then((r) => {
  for (const i of r.data) {
    if (!Object.prototype.hasOwnProperty.call(users, i.userId)) users[i.userId] = 0;
    if (i.completed) users[i.userId] += 1;
  }
  console.log(users);
}).catch((e) => {
  if (e) console.log(e);
});
