#!/usr/bin/node
const args = process.argv;
args.splice(0, 2);
if (!args[0]) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
