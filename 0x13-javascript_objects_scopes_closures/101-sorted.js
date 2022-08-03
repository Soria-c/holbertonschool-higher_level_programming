#!/usr/bin/node
const dict = require('./101-data').dict;
const val = Object.values(dict);
const kys = Object.keys(dict);
const uniq = val.filter((val, ind, arr) => arr.indexOf(val) === ind);
const r = {};

for (const i of uniq) {
  r[i] = kys.filter(x => dict[x] === i);
}
console.log(r);
