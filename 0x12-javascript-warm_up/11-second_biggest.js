#!/usr/bin/node

let count1 = 0;
let count2 = 2;
let number;
const arr1 = [];
while (process.argv[count1]) { count1++; }

if (count1 < 4) {
  console.log(0);
} else {
  for (count2; count2 < count1; count2++) {
    number = parseInt(process.argv[count2]);
    arr1.push(number);
  }
  arr1.sort(function (a, b) { return b - a; });
  for (count2 = 1; count2 < count1; count2++) {
    if (arr1[count2] !== arr1[count2 - 1]) {
      console.log(arr1[count2]);
      break;
    }
  }
}
