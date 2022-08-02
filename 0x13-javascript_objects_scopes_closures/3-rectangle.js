#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const h = this.height;
    const arr = '#,'.repeat(h).split(',').splice(0, h);
    console.log(arr.map((x) => x.repeat(this.width)).join('\n'));
  }
}

module.exports = Rectangle;
