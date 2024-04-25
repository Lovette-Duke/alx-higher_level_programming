#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(api, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
