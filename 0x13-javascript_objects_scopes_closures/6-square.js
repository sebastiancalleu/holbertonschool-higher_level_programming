#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let count = 0;
    for (count; count < this.height; count++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

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
