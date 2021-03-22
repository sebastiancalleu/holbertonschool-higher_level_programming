#!/usr/bin/node

let count1 = 0;
let number;
let number1;
let suma;
while (process.argv[count1]) { count1++; }

if (count1 < 4) {
  console.log(NaN);
} else {
  number = parseInt(process.argv[2]);
  number1 = parseInt(process.argv[3]);
  suma = add(number, number1);
  console.log(suma);
}

function add (a, b) {
  return a + b;
}
