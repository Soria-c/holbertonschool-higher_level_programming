#!/usr/bin/node
const args = process.argv;
// const range = n => [...Array(n).keys()];
const number = parseInt(args[2]);

if (args.length === 2) {
  console.log('Missing number of occurrences');
}

if (number >= 1) {
  process.stdout.write('C is fun\n'.repeat(number));
}
