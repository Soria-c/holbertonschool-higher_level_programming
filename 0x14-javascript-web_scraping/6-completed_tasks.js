#!/usr/bin/node
const axios = require('axios');

const users = {};
axios
  .get(process.argv[2])
  .then((r) => {
    for (const i of r.data) {
      if (i.completed) {
        if (!Object.prototype.hasOwnProperty.call(users, i.userId)) users[i.userId] = 0;
        users[i.userId] += 1;
      }
    }
    console.log(users);
  })
  .catch((e) => console.log(e));
