#!/usr/bin/node
const process = require('process');
const fs = require('fs');
const fName = process.argv[2];
const content = process.argv[3];

fs.writeFile(fName, content, 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
