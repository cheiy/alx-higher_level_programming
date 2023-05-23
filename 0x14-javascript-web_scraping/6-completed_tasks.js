#!/usr/bin/node
const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const complete = {};
    const tasks = JSON.parse(body);
    tasks.forEach(task => {
      if (task.completed === true) {
        if (complete[task.userId] === undefined) {
          complete[task.userId] = 1;
        } else {
          complete[task.userId] += 1;
        }
      }
    });
    console.log(complete);
  } else {
    console.log('An error occurred. Status code:' + response.statusCode);
  }
});
