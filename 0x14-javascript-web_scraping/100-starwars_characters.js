#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, res, body) {
  if (res.statusCode === 200) {
    const dct1 = JSON.parse(body);
    let character = 0;
    for (character of dct1.characters) {
      request(character, function (err, res, body) {
        if (res.statusCode === 200) {
          const dct3 = JSON.parse(body);
          console.log(dct3.name);
        } else {
          console.log(err);
        }
      });
    }
  } else {
    console.log(err);
  }
});
