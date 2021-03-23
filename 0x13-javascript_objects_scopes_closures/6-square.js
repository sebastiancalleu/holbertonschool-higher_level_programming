#!/usr/bin/node

const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let count = 0; count < this.height; count++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
