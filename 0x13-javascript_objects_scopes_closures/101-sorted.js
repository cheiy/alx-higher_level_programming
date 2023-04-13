#!/usr/bin/node
const dict = require('./101-data').dict;
const Keys = Object.keys(dict);
const values = Object.values(dict);
let matched;
const result = {};
for (let i = 0; i < values.length; i++) {
  result[JSON.stringify(values[i])] = [];
  matched = Keys.filter(key => dict[key] === values[i]);
  matched.forEach(item => result[JSON.stringify(values[i])].push(item));
}
console.log(result);
