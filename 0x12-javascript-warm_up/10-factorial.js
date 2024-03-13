#!/usr/bin/node

function factorial (a) {
  if (isNaN(a) || a === 0) {
    console.log(1);
  }
  console.log(a * factorial(a - 1));
}

const a = Math.floor(process.argv[2]);

factorial(a);
