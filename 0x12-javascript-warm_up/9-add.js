#!/usr/bin/node

function add(a, b) {
  sum = a + b;
  console.log(sum);
}

a = Math.floor(process.argv[2]);
b = Math.floor(process.argv[3]);

add (a, b);
