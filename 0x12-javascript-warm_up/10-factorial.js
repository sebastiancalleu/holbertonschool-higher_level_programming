#!/usr/bin/node

let count1 = 0;
let number;
let fact;
while (process.argv[count1]) { count1++; }

if (count1 < 3) {
  console.log(NaN);
} else {
  number = parseInt(process.argv[2]);
  fact = fctorial(number);
  console.log(fact);
}

function fctorial (a) {
  if (a === 1) {
    return (1);
  } else {
    return (a * fctorial(a - 1));
  }
}
