# JavaScript Cheatsheet

## Table of Contents

- [Variables](#variables)
- [Data Types](#data-types)
- [Operators](#operators)
- [Conditionals](#conditionals)
- [Loops](#loops)
- [Functions](#functions)
- [Objects](#objects)
- [Arrays](#arrays)
- [ES6 Features](#es6-features)
- [DOM Manipulation](#dom-manipulation)
- [Events](#events)
- [Async Programming](#async-programming)

## Variables

### var

```javascript
var name = 'John';
```

### let

```javascript
let age = 30;
```

### const

```javascript
const PI = 3.14;
```

## Data Types
### Primitive Types
- String
- Number
- Boolean
- Null
- Undefined
- Symbol
### Non-Primitive Types
- Object
- Array
- Function
### Examples
```javascript
let name = 'Alice'; // String
let age = 25; // Number
let isStudent = true; // Boolean
let value = null; // Null
let x; // Undefined
let symbol = Symbol('sym'); // Symbol
```

## Operators

### Arithmetic Operators

```javascript
let sum = 10 + 5; // Addition
let difference = 10 - 5; // Subtraction
let product = 10 * 5; // Multiplication
let quotient = 10 / 5; // Division
let remainder = 10 % 3; // Modulus
let exponent = 2 ** 3; // Exponentiation
```

### Assignment Operators

```javascript
let x = 10;
x += 5; // Equivalent to x = x + 5
x -= 5; // Equivalent to x = x - 5
x *= 5; // Equivalent to x = x * 5
x /= 5; // Equivalent to x = x / 5
x %= 5; // Equivalent to x = x % 5
x **= 5; // Equivalent to x = x ** 5
```

### Comparison Operators

```javascript
let a = 10;
let b = 5;

a == b; // Equal to
a === b; // Strict equal to
a != b; // Not equal to
a !== b; // Strict not equal to
a > b; // Greater than
a >= b; // Greater than or equal to
a < b; // Less than
a <= b; // Less than or equal to
```

### Logical Operators

```javascript
let a = true;
let b = false;

a && b; // Logical AND
a || b; // Logical OR
!a; // Logical NOT
```

## Conditionals

### if Statement

```javascript
if (condition) {
  // code to be executed if condition is true
}
```

### if...else Statement

```javascript
if (condition) {
  // code to be executed if condition is true
} else {
  // code to be executed if condition is false
}
```

### else if Statement

```javascript
if (condition1) {
  // code to be executed if condition1 is true
} else if (condition2) {
  // code to be executed if condition2 is true
} else {
  // code to be executed if both condition1 and condition2 are false
}
```

### switch Statement

```javascript
switch (expression) {
  case value1:
    // code to be executed if expression equals value1
    break;
  case value2:
    // code to be executed if expression equals value2
    break;
  default:
    // code to be executed if expression doesn't match any case
}
```

## Loops

### for Loop

```javascript
for (let i = 0; i < 5; i++) {
  // code to be executed
}
```

### while Loop

```javascript
let i = 0;
while (i < 5) {
  // code to be executed
  i++;
}
```

### do...while Loop

```javascript
let i = 0;
do {
  // code to be executed
  i++;
} while (i < 5);
```

### for...in Loop

```javascript
let obj = {a: 1, b: 2, c: 3};
for (let key in obj) {
  // code to be executed
}
```

### for...of Loop

```javascript
let arr = [1, 2, 3];
for (let value of arr) {
  // code to be executed
}
```

## Functions

### Function Declaration

```javascript
function add(a, b) {
  return a + b;
}
```

### Function Expression

```javascript
const add = function(a, b) {
  return a + b;
};
```

### Arrow Function

```javascript
const add = (a, b) => a + b;
```

## Objects

### Object Literal

```javascript
let person = {
  name: 'John',
  age: 30,
  greet: function() {
    console.log('Hello');
  }
};
```

### Accessing Properties

```javascript
person.job = 'Developer'; // Adding a property
person.age = 31; // Modifying a property
```

### Adding/Modifying Properties

```javascript
person.job = 'Developer'; // Adding a property
person.age = 31; // Modifying a property
```

### Deleting Properties

```javascript
delete person.age;
```

## Arrays

### Array Literal

```javascript
let numbers = [1, 2, 3, 4, 5];
```

### Accessing Elements

```javascript
console.log(numbers[0]);
```

### Adding Elements

```javascipt
numbers.push(6); // Adds to the end
numbers.unshift(0); // Adds to the beginning
```

### Removing Elements

```javascript
numbers.pop(); // Removes from the end
numbers.shift(); // Removes from the beginning
```

### Iterating Over Arrays

```javascript
numbers.forEach(function(number) {
  console.log(number);
});

numbers.forEach(number => console.log(number)); // Using arrow function
```

## ES6 Features

### let and const

```javascript
let name = 'John';
const PI = 3.14;
```

### Arrow Functions

```javascript
const greet = () => console.log('Hello');
```

### Template Literals

```javascipt
let name = 'John';
let message = `Hello, ${name}!`;
```

### Destructuring Assignment

```javascript
let person = {name: 'John', age: 30};
let {name, age} = person;

let arr = [1, 2, 3];
let [a, b, c] = arr;
```

### Default Parameters

```javascript
function greet(name = 'Guest') {
  console.log(`Hello, ${name}`);
}
```

### Spread Operator

```javascript
let arr1 = [1, 2, 3];
let arr2 = [...arr1, 4, 5];
```

### Rest Parameters

```javascript
function sum(...numbers) {
  return numbers.reduce((acc, curr) => acc + curr, 0);
}
```

### Classes

```javascript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, my name is ${this.name}`);
  }
}

let john = new Person('John', 30);
john.greet();
```

## DOM Manipulation

### Selecting Elements

```javascript
document.getElementById('id');
document.getElementsByClassName('class');
document.getElementsByTagName('tag');
document.querySelector('selector');
document.querySelectorAll('selector');
```

### Modifying Elements

```javascript
let element = document.getElementById('id');
element.innerHTML = 'New Content';
element.style.color = 'blue';
element.classList.add('new-class');
```

### Creating Elements

```javascipt
let newElement = document.createElement('div');
newElement.innerHTML = 'Hello, World!';
document.body.appendChild(newElement);
```

### Removing Elements

```javascript
let element = document.getElementById('id');
element.remove();
```

## Events

### Adding Event Listeners

```javascript
let button = document.getElementById('button');
button.addEventListener('click', function() {
  console.log('Button clicked');
});
```

### Removing Event Listeners

```javascript
function handleClick() {
  console.log('Button clicked');
}

button.removeEventListener('click', handleClick);
```

## Async Programming

### Callbacks

```javascript
function fetchData(callback) {
  setTimeout(() => {
    callback('Data fetched');
  }, 1000);
}

fetchData(data => {
  console.log(data);
});
```

### Promises

```javascript
let promise = new Promise((resolve, reject) => {
  let success = true;
  if (success) {
    resolve('Success');
  } else {
    reject('Error');
  }
});

promise.then(result => {
  console.log(result);
}).catch(error => {
  console.log(error);
});
```

### Async/Await

```javascript
async function fetchData() {
  let response = await fetch('url');
  let data = await response.json();
  console.log(data);
}

fetchData();
```
