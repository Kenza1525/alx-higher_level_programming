#!/usr/bin/node

const args = parseInt(process.argv[2]);
const x = 'X';

if (args) {
  for (let i = 0; i < args; i++) {
    for (let j = 0; j < args; j++) {
      process.stdout.write(x);
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
