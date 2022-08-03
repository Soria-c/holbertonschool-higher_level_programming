#!/usr/bin/node
const dict = require('./101-data').dict;
const values = Object.values(dict);
const kys = Object.keys(dict);
const uniq = values.filter((val, ind) => values.indexOf(val) === ind).sort();
const r = {};

for (const i of uniq) {
  r[i] = kys.filter(x => dict[x] === i).sort((a, b) => parseInt(a) - parseInt(b));
}
console.log(r);
