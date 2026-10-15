// document.getElementById("btn").onclick = function () {
//   document.getElementById("title").innerText = "Changed from script.js! 🚀";
// };

let userName = "Newgen";
let age = 21;
console.log(userName); // Newgen
console.log(age); 

let score = 0;
console.log(score); // 0

score = 10;         // updating the value
console.log(score); // 10

score = score + 5;
console.log(score); // 15

let city;
console.log(city); // undefined

city = "Pune";
console.log(city); // Pune

// const PI = 3.14;
// console.log(PI); // 3.14

if (true) {
  let aa = 10;
  var bb = 20;
  console.log(aa); // I am block scoped!
}
// console.log(aa); // ReferenceError: aa is not defined
console.log(bb); // I am function scoped!


// area of circle

let radius = 7;
const PI = 3.14159265;
let area = PI * radius * radius;
console.log(area); // 153.93804000000002