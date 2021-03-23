#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let count = 0;
  let occur = 0;

  for (count; list[count]; count++) {
    if (list[count] === searchElement) {
      occur++;
    }
  }
  return occur;
}
module.exports.nbOccurences = nbOccurences;
