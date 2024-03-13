#!/usr/bin/node

const data100 = require('./100-data').list;

const mapData = data100.map((x, index) => x * index);

console.log(data100);
console.log(mapData);
