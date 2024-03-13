#!/usr/bin/node

const data100 = require('./100-data').data100;

const mapData = data100.map((x, index) => x * index);

console.log(data100);
console.log(mapData);
