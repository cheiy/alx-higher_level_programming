#!/usr/bin/node
const firstArg = parseInt(process.argv[2]);
function Factorial (num) {
  if (num < 0) {
    return (-1);
  }
  if (num === 0 || isNaN(num)) {
    return (1);
  }
  return (num * Factorial(num - 1));
}

console.log(Factorial(firstArg));
