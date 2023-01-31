#!/usr/bin/node

const args = process.argv.slice(2);

const number = parseInt(args[0]);
let square = '';

if (number === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    for (let j = 0; j < number; j++) {
      square += 'x';
    }
    square += '\n';
  }
  console.log(square);
}
