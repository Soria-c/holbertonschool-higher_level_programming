#!/usr/bin/node
const s = parseInt(process.argv[2]);
if (isNaN(s) || process.argv.length <= 2) {
  console.log('Missing size');
}
if (s > 0) {
  const arr = 'X,'.repeat(s).split(',').splice(0, s);
  console.log(arr.map((x) => x.repeat(s)).join('\n'));
}
