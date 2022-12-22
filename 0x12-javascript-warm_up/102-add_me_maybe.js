#!/usr/bin/node

exports.addMeMaybe = function (x, func) {
  return func(x + 1);
};
