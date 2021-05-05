#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (res.statusCode === 200) {
    const dct1 = JSON.parse(body);
    const dct2 = {};
    for (const items of dct1) {
      if (items.completed === true) {
        if (items.userId in dct2) {
          dct2[items.userId] += 1;
        } else {
          dct2[items.userId] = 1;
        }
      }
    }
    console.log(dct2);
  } else {
    console.log(err);
  }
});
