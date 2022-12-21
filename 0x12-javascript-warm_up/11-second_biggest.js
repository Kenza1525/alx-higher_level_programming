#!/usr/bin/node

const args = process.argv;
const num = process.argv[2];
const arg3 = process.argv[3];
const arr = [];
if (!num || !arg3) {
  console.log('0');
}
for (let i = 2; i < args.length; i++) {
  arr.push(parseInt(args[i]));
}
arr.sort(function (a, b) { return a - b; });
console.log(arr[arr.length - 2]);
