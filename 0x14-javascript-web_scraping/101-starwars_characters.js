#!/usr/bin/node
const request = require('request');
const movieid = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieid;
request(url, (error, response, body) => {
  if (error) throw error;
  else {
    send(JSON.parse(body).characters, 0);
  }
});

function send (person, index) {
  if (index >= person.length) {
    return;
  }
  request(person[index], (error, response, body) => {
    if (error) throw error;
    else {
      console.log(JSON.parse(body).name);
      return send(person, ++index);
    }
  });
}
