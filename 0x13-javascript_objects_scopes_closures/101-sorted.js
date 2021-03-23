#!/usr/bin/node

const ob1 = require('./101-data');
const dct1 = ob1.dict;
const dct2 = {};
for (const [, value] of Object.entries(dct1)) {
  dct2[value] = [];
}
for (const [key, value] of Object.entries(dct1)) {
  dct2[value].push(key);
}
console.log(dct2);
