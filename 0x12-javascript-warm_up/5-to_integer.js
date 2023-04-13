#!/usr/bin/node
const first = process.argv[2];
if (isNaN(first) || first === undefined) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(first));
}
