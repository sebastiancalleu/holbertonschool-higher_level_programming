#!/usr/bin/node

exports.esrever = function (list) {
  const lt1 = [];
  const count = 0;
  newfunc(list, lt1, count);
  return lt1;
};

function newfunc (list, lt1, count) {
  if (!list[count]) {
    return;
  } else {
    newfunc(list, lt1, count + 1);
  }
  lt1.push(list[count]);
}
