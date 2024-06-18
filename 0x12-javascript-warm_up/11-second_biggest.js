#!/usr/bin/node
const tot = process.argv.length;
if (tot <= 3) {
  console.log(0);
} else {
  const myArray = [];
  for (let count = 2; count < tot; count++) {
    myArray.push(parseInt(process.argv[count]));
  }
  myArray.sort(function (a, b) {
    return b - a;
  });
  console.log(myArray[1]);
}
