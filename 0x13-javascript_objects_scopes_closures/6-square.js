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

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let count = 0;
    if (!c) {
      for (count; count < this.height; count++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (count; count < this.height; count++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
