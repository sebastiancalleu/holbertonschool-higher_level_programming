#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, res, body) {
  if (res.statusCode === 200) {
    const dct1 = JSON.parse(body);
    let character = 0;
    for (character in dct1.characters) {
      request(dct1.characters[character], function (err, res, body) {
        if (res.statusCode === 200) {
          console.log(character);
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
