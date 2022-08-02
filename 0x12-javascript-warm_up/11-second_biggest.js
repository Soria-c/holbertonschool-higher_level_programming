#!/usr/bin/node
let args = process.argv;
args.splice(0, 2);
args = args.map(x => parseInt(x)).sort().reverse();
console.log(args[1]);
