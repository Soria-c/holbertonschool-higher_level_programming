#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log(parseInt('1'));
  process.exit();
}
function factorial (x) {
  if (x === 0) {
    return (1);
  }
  return (x * factorial(x - 1));
}
console.log(factorial(number));
