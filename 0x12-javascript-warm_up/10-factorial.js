#!/usr/bin/node
const arg1 = parseInt(process.argv[2]);
let arg = 1;
if (!(arg)) {
  console.log(1);
} else {
  for (let count = 1; count <= arg1; count++) {
    arg *= count;
  }
  console.log(arg);
}
