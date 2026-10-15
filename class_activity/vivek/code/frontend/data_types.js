
console.log("Data Types in JavaScript");

// numbers
let a = 10;
let b = 20.5;
let c = -5;

console.log("Value of a:", a);
console.log("Value of b:", b);
console.log("Value of c:", c);

console.log("Type of a:", typeof a);
console.log("Type of b:", typeof b);
console.log("Type of c:", typeof c);

console.log(10 / 0);        // Infinity
console.log("abc" * 3);     // NaN (Not a Number)
console.log(typeof NaN);    // "number" (funny but true!)

// strings

let firstname = "Vivek";
let language = 'JavaScript';
let greeting = `Hi there! my name is ${firstname}, the language im learning is ${language}`;

console.log(firstname);
console.log(language);
console.log(greeting);
console.log(typeof greeting)

// Boolean
let isTodaySunday = true;
let isTodayFriday = false;

console.log(isTodayFriday);
console.log(isTodaySunday);
console.log(typeof isTodaySunday);
console.log(typeof isTodayFriday);

// undefined and null
let aa;
console.log(typeof aa);

let bb = null;
console.log(typeof bb);
console.log('bb', bb)
console.log('aa', aa)

// typeof operator
// unary, binary, ternary operator
// arithmatic operators
let x = 10;
x++;
console.log(x);       // 11
console.log(10 % 2);  // 0 → even number!
console.log(7 % 2);   // 1 → odd number!
    
// assignment operators
let balance = 1000;
balance += 500;   // 1500
// balance = balance + 500
balance -= 200;   // 1300
console.log(balance);

// comparision operators
// Operator	Meaning	Example	Result
// >	greater than	5 > 3	true
// <	less than	5 < 3	false
// >=	greater than or equal	5 >= 5	true
// <=	less than or equal	4 <= 3	false
// ==	equal (loose)	5 == "5"	true 😮
// ===	equal (strict)	5 === "5"	false ✅
// !=	not equal (loose)	5 != "5"	false
// !==	not equal (strict)	5 !== "5"	true
console.log(5 < 3);
console.log(5 > 3);
console.log(5 <= 3);
console.log(5 >= 3);
console.log(5 != '5');
console.log(5 !== '5');
console.log(5 == '5'); // true
console.log(5 === '5'); // false

// logical operators

let age = 20;
let hasTicket = true;

console.log(age >= 18 && hasTicket); // true  (both true)
console.log(age < 18 || hasTicket);  // true  (one is true)
console.log(!hasTicket);             // false