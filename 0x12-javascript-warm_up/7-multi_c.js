#!/usr/bin/node
const ourString = 'C is fun';
let numOfTimes = 0;
if (process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  numOfTimes = parseInt(process.argv[2]);
}
for (let i = 0; i < numOfTimes; i++) {
  console.log(ourString);
}
