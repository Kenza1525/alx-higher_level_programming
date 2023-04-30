#!/usr/bin/node

const num = process.argv[2];

function getFactorial (num) {
  if (!num) {
    return 1;
  } else {
    return (num * getFactorial(num - 1));
  }
}
console.log(getFactorial(num));
