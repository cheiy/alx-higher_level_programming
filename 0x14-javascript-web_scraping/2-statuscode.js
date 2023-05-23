#!/usr/bin/node
const process = require('process');
const request = require('request');
const url = process.argv[2];

request(url, function (err, response) {
  if (err) {
    console.error(err);
  }
  console.log('code:', response.statusCode);
});
