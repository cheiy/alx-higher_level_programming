#!/usr/bin/node
const arg3 = process.argv[2];
if (arg3 == null) {
  console.log('No argument');
} else {
  console.log(arg3);
}
