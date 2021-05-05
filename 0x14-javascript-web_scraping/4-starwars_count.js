#!/usr/bin/node

const request = require('request');

const ID = 18;

request(process.argv[2], function (err, res, body) {
  if (res.statusCode === 200) {
    const dct1 = JSON.parse(body);
    const dct2 = dct1.results;
    let count = 0;
    let items = 0;
    let character = 0;
    for (items of dct2) {
      for (character of items.characters) {
        if (character.includes(ID)) { count += 1; }
      }
    }
    console.log(count);
  } else {
    console.log(err);
  }
});
