#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    const h = this.height;
    const arr = `${c},`.repeat(h).split(',').splice(0, h);
    console.log(arr.map((x) => x.repeat(this.width)).join('\n'));
  }
}

module.exports = Square;
