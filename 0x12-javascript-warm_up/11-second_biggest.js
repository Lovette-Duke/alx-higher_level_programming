#!/usr/bin/node

const arg = process.argv.slice(2);
const argc = process.argv.length;

if (argc <= 3) {
  console.log(0);
} else {
  arg.sort((a, b) => b - a);
  console.log(arg[1]);
}
