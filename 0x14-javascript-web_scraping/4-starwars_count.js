#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
let count = 0;
req(url, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const json = JSON.parse(body);
  const results = json.results;
  for (let i = 0; i < results.length; i++) {
    if (results[i].characters) {
      for (const j of results[i].characters) {
        if (j.includes('18')) {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});
