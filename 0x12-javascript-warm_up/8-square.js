#!/usr/bin/node
const firstArg = parseInt(process.argv[2]);
if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArg; i++) {
    console.log('X'.repeat(firstArg));
  }
}
