#!/usr/bin/node

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

const a = Math.floor(process.argv[2]);
const b = Math.floor(process.argv[3]);

add(a, b);
