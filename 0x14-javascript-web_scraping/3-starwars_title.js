#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  const dct1 = JSON.parse(body);
  console.log(dct1.title);
});
