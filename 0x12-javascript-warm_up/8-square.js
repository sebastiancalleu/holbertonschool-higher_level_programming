#!/usr/bin/node

let count1 = 0;
let count2 = 0;
let number;
while (process.argv[count1]) { count1++; }

if (count1 === 2) {
  console.log('Missing size');
} else {
  number = parseInt(process.argv[2]);
  if (number) {
    for (count2 = 0; count2 < number; count2++) { console.log('X'.repeat(number)); }
  } else {
    console.log('Missing size');
  }
}
