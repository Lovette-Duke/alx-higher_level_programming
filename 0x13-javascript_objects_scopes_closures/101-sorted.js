#!/usr/bin/node

const data101 = require('./101-data').dict;

const sortDict = {};
for (const key in data101) {
  if (sortDict[data101[key]] === undefined) {
    sortDict[data101[key]] = [];
  }
  sortDict[data101[key]].push(key);
}

console.log(sortDict);
