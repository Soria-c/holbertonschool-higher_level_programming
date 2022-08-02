#!/usr/bin/node
function addMeMaybe (x, callBack) {
  callBack(x + 1);
}

module.exports = { addMeMaybe };
