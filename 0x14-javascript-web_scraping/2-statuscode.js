#!/usr/bin/node
const request = require('request');

request(process.argv[2], { method: 'GET' }, (err, { statusCode }) => {
  if (err) return console.log(err);
  console.log(`code: ${statusCode}`);
});
