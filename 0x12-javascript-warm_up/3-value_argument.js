#!/usr/bin/node

let count = 0;
while (process.argv[count]) { count++; }

if (count === 2) { console.log('No argument'); } else { console.log(process.argv[2]); }
