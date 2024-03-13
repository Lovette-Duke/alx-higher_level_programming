#!/usr/bin/node

function factorial (a) {
  if (isNaN(a) || a === 0) {
    return (1);
  }
  return(a * factorial(a - 1));
}

const a = Math.floor(process.argv[2]);

console.log(factorial(a));
