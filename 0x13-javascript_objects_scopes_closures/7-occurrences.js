#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let countNb = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      countNb++;
    }
  }
  return countNb;
};
