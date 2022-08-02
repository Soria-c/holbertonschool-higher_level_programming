#!/usr/bin/node
const args = process.argv;
const argsNumber = args.length - 2;

if (!argsNumber) {
  console.log('No argument');
} else if (argsNumber === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments Found');
}
