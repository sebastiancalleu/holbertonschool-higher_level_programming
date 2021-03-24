#!/usr/bin/node

const firstfile = process.argv[2];
const secondfile = process.argv[3];
const concatfile = process.argv[4];
const fs = require('fs');
const data = fs.readFileSync(firstfile, 'utf8');
const data1 = fs.readFileSync(secondfile, 'utf8');

fs.writeFileSync(concatfile, data + data1, 'utf8');
