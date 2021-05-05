#!/usr/bin/node

const request = require('request');

const ID = 18;
const characterurl = 'https://swapi-api.hbtn.io/api/people/' + ID + '/';

request(process.argv[2], function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  const dct1 = JSON.parse(body);
  const dct2 = dct1.results;
  let count = 0;
  let items = 0;
  let character = 0;
  for (items in dct2) {
    for (character in dct2[items].characters) {
      if (dct2[items].characters[character] === characterurl) { count += 1; }
    }
  }
  console.log(count);
});