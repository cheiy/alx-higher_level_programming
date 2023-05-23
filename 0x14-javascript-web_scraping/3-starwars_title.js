#!/usr/bin/node
const process = require('process');
const req = require('request');
const id = process.argv[2];
const endpoint = 'https://swapi-api.alx-tools.com/api/films/' + id;

req(endpoint, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
