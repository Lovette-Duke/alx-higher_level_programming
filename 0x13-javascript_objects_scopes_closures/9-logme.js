#!/usr/bin/node

let lugNum = -1;

exports.logMe = function (item) {
  lugNum++;
  console.log(lugNum + ': ' + item);
};
