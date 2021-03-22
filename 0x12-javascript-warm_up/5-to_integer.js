#!/usr/bin/node

let count = 0;
let number;
while (process.argv[count]) { count++; }

if (count === 2) { console.log('Not a number'); } else { number = parseInt(process.argv[2]); if (number) { console.log('My number:', number); } else { console.log('Not a number'); } }
