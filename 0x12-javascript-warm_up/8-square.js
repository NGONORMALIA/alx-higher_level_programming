#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (!(arg)) {
  console.log('Missing size');
} else {
  for (let count = 0; count < arg; count++) {
    console.log('X'.repeat(arg));
  }
}
