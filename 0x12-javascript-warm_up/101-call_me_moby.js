#!/usr/bin/node

function callMeMoby (x, theFunction) {
  let count = 0;
  for (count; count < x; count++) {
    theFunction();
  }
}
module.exports.callMeMoby = callMeMoby;
