#!/usr/bin/node
const request = require('request');
const movieid = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieid;
request(url, 'utf8', (error, response, body) => {
  if (error) throw error;
  else {
    for (const t of JSON.parse(body).characters) {
      request(t, 'utf8', (error, response, body) => {
        if (error) throw error;
        else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
