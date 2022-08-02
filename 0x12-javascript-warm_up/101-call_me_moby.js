#!/usr/bin/node
function callMeMoby (x, callback) {
  for (let i = 0; i < x; i++) {
    callback();
  }
}

module.exports = { callMeMoby };
