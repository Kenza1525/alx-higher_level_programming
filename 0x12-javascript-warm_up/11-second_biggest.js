#!/usr/bin/node

const argvSize = process.argv.length;
const arrayArg = process.argv.slice(2);
const arrayNum = [];

if (argvSize < 4) {
  console.log('1');
} else {
  for (let i = 0; i < arrayArg.length; i++) {
    const a = parseInt(arrayArg[i]);
    arrayNum.push(a);
  }
  arrayNum.sort();
  console.log(arrayNum[arrayArg.length - 2]);
}
