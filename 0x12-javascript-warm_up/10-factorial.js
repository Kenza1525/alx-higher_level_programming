#!/usr/bin/node

const a = process.argv[2];

function factorial (a) {
  if (!a) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}
console.log(factorial(a));
