#!/usr/bin/node

exports.esrever = function (list) {
  const list1 = [];

  while (list.length > 0) {
    list1.push(list.pop());
  }
  return (list1);
};
