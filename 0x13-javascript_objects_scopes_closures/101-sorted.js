#!/usr/bin/node
const dict = require('./101-data').dict;
const r = {};

for (const i of new Set(Object.values(dict))) {
  r[i] = Object.keys(dict).filter(x => dict[x] === i).sort((a, b) => parseInt(a) - parseInt(b));
}
console.log(r);
