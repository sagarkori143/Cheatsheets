# TypeScript Cheatsheet

## Table of Contents

- [Getting Started](#getting-started)
- [Basic Types](#basic-types)
- [Type Assertions](#type-assertions)
- [Interfaces](#interfaces)
- [Classes](#classes)
- [Functions](#functions)
- [Generics](#generics)
- [Enums](#enums)
- [Modules](#modules)
- [Type Inference](#type-inference)
- [Advanced Types](#advanced-types)
- [Utility Types](#utility-types)

## Getting Started

### Installing TypeScript

```sh
npm install -g typescript
```

### Compiling TypeScript

```sh
tsc filename.ts
```

## Basic Types

### Boolean

```sh
let isDone: boolean = false;
```

### Number

```sh
let decimal: number = 6;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;
```

### String

```sh
let color: string = "blue";
color = 'red';
```

### Array

```sh
let list: number[] = [1, 2, 3];
let list: Array<number> = [1, 2, 3];
```

### Tuple

```sh
let x: [string, number];
x = ["hello", 10]; // OK
x = [10, "hello"]; // Error
```

### Enum

```sh
enum Color {Red, Green, Blue}
let c: Color = Color.Green;
```

### Any

```sh
let notSure: any = 4;
notSure = "maybe a string instead";
notSure = false; // okay, definitely a boolean
```

### Void

```sh
function warnUser(): void {
    console.log("This is my warning message");
}
```

### Null and Undefined

```sh
let u: undefined = undefined;
let n: null = null;
```

### Never

```sh
function error(message: string): never {
    throw new Error(message);
}
```

### Object

```sh
declare function create(o: object | null): void;
create({ prop: 0 });
create(null);
```

## Type Assertions

### Angle-bracket syntax

```sh
let someValue: any = "this is a string";
let strLength: number = (<string>someValue).length;
```

### as-syntax

```sh
let someValue: any = "this is a string";
let strLength: number = (someValue as string).length;
```

## Interfaces

### Basic Interface

```sh
interface LabelledValue {
    label: string;
}

function printLabel(labelledObj: LabelledValue) {
    console.log(labelledObj.label);
}

let myObj = {size: 10, label: "Size 10 Object"};
printLabel(myObj);
```

### Optional Properties

```sh
interface SquareConfig {
    color?: string;
    width?: number;
}

function createSquare(config: SquareConfig): {color: string; area: number} {
    let newSquare = {color: "white", area: 100};
    if (config.color) {
        newSquare.color = config.color;
    }
    if (config.width) {
        newSquare.area = config.width * config.width;
    }
    return newSquare;
}

```

### Readonly Properties

```sh
interface Point {
    readonly x: number;
    readonly y: number;
}

let p1: Point = { x: 10, y: 20 };
p1.x = 5; // Error
```

## Classes

### Basic Class

```sh
class Greeter {
    greeting: string;
    constructor(message: string) {
        this.greeting = message;
    }
    greet() {
        return "Hello, " + this.greeting;
    }
}

let greeter = new Greeter("world");
```

### Inheritance

```sh
class Animal {
    move(distanceInMeters: number = 0) {
        console.log(`Animal moved ${distanceInMeters}m.`);
    }
}

class Dog extends Animal {
    bark() {
        console.log('Woof! Woof!');
    }
}

const dog = new Dog();
dog.bark();
dog.move(10);
dog.bark();
```

### Public, private, and protected modifiers

```sh
class Animal {
    private name: string;
    public constructor(theName: string) { this.name = theName; }
    public move(distanceInMeters: number) {
        console.log(`${this.name} moved ${distanceInMeters}m.`);
    }
}
```

## Functions

### Named Function

```sh
function add(x: number, y: number): number {
    return x + y;
}
```

### Anonymous Function

```sh
let myAdd = function(x: number, y: number): number { return x + y; };
```

### Optional and Default Parameters

```sh
function buildName(firstName: string, lastName?: string) {
    if (lastName)
        return firstName + " " + lastName;
    else
        return firstName;
}
```

### Rest Parameters

```sh
function buildName(firstName: string, ...restOfName: string[]) {
    return firstName + " " + restOfName.join(" ");
}
```

## Generics

### Basic Example

```sh
function identity<T>(arg: T): T {
    return arg;
}

let output = identity<string>("myString");
let output = identity("myString"); // type argument inference
```

### Generic Classes

```sh
class GenericNumber<T> {
    zeroValue: T;
    add: (x: T, y: T) => T;
}

let myGenericNumber = new GenericNumber<number>();
myGenericNumber.zeroValue = 0;
myGenericNumber.add = function(x, y) { return x + y; };
```

## Enums

### Numeric Enums

```sh
enum Direction {
    Up = 1,
    Down,
    Left,
    Right
}
```

### String Enums

```sh
enum Direction {
    Up = "UP",
    Down = "DOWN",
    Left = "LEFT",
    Right = "RIGHT"
}
```

## Modules

### Export

```sh
export interface StringValidator {
    isAcceptable(s: string): boolean;
}

export const numberRegexp = /^[0-9]+$/;

export class ZipCodeValidator implements StringValidator {
    isAcceptable(s: string) {
        return s.length === 5 && numberRegexp.test(s);
    }
}
```

### Import

```sh
import { ZipCodeValidator } from "./ZipCodeValidator";

let myValidator = new ZipCodeValidator();
```

## Type Inference

### Basic Inference

```sh
let x = 3; // inferred to be number
```

### Best Common Type

```sh
let x = [0, 1, null]; // inferred to be (number | null)[]
```

## Advanced Types

### Intersection Types

```sh
interface Person {
    name: string;
}

interface Contact {
    email: string;
}

type Employee = Person & Contact;

let employee: Employee = {
    name: 'John Doe',
    email: 'john.doe@example.com'
};
```

### Union Types

```sh
function padLeft(value: string, padding: number | string) {
    if (typeof padding === "number") {
        return Array(padding + 1).join(" ") + value;
    }
    if (typeof padding === "string") {
        return padding + value;
    }
    throw new Error(`Expected string or number, got '${padding}'.`);
}
```

### Type Guards

```sh
function isNumber(x: any): x is number {
    return typeof x === "number";
}

function isString(x: any): x is string {
    return typeof x === "string";
}
```

### Nullable types

```sh
let s: string | null = "foo";
s = null; // OK
s = undefined; // Error
```

## Utility Types

### Partial

```sh
interface Todo {
    title: string;
    description: string;
}

function updateTodo(todo: Todo, fieldsToUpdate: Partial<Todo>) {
    return { ...todo, ...fieldsToUpdate };
}

const todo1 = {
    title: "organize desk",
    description: "clear clutter"
};

const todo2 = updateTodo(todo1, {
    description: "throw out trash"
});
```

### Readonly

```sh
interface Todo {
    title: string;
}

const todo: Readonly<Todo> = {
    title: "Delete inactive users"
};

todo.title = "Hello"; // Error: cannot reassign a readonly property
```

### Record

```sh
interface PageInfo {
    title: string;
}

type Page = "home" | "about" | "contact";

const x: Record<Page, PageInfo> = {
    home: { title: "Home" },
    about: { title: "About" },
    contact: { title: "Contact" }
};
```

### Pick

```sh
interface Todo {
    title: string;
    description: string;
    completed: boolean;
}

type TodoPreview = Pick<Todo, "title" | "completed">;

const todo: TodoPreview = {
    title: "Clean room",
    completed: false
};
```

### Omit

```sh
interface Todo {
    title: string;
    description: string;
    completed: boolean;
}

type TodoPreview = Omit<Todo, "description">;

const todo: TodoPreview = {
    title: "Clean room",
    completed: false
};
```
