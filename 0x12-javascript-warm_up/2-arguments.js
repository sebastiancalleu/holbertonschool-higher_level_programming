#!/usr/bin/node

let count = 0;
while (process.argv[count]) { count++; }

if (count === 2) { console.log('No argument'); } else if (count === 3) { console.log('Argument found'); } else { console.log('Arguments found'); }
