#!/usr/bin/node

const args = process.argv;
const num = process.argv[2];
const arg_3 = process.argv[3]
if (!num || !arg_3) {
  console.log('0');
}
for (let i = 1; i < args.length; i++) {
  if (args[i] > num) {
    console.log(num);
  }
}
