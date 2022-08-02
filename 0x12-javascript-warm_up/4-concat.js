#!/usr/bin/node
const args = process.argv;
args.splice(0, 2);
console.log(`${args[0]} is ${args[1]}`);
