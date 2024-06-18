#!/usr/bin/node
const arg = process.argv.length;
/*if (arg >= 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}*/
console.log(arg === 2 ? 'No argument' : arg === 3 ? 'Argument found' : 'Arguments found');
