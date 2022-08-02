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
    const arr = 'X,'.repeat(h).split(',').splice(0, h);
    console.log(arr.map((x) => x.repeat(this.width)).join('\n'));
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width]
  }
}

module.exports = Rectangle;
