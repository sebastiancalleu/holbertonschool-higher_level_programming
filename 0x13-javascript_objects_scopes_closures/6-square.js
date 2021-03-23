#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    let count = 0;
    if (c === undefined) {
		this.print()
    } else {
      for (count; count < this.height; count++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
