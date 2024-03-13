#!/usr/bin/node

exports.converter = function (base) {
  function convert10 (num) {
    return num.toString(base);
  }
  return convert10;
};
