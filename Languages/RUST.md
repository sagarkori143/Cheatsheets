# Rust Programming Language Tutorial

## Table of Contents
1. [Introduction to Rust](#introduction-to-rust)
2. [Installation](#installation)
3. [Hello, World!](#hello-world)
4. [Variables and Constants](#variables-and-constants)
5. [Data Types](#data-types)
6. [Functions](#functions)
7. [Control Flow](#control-flow)
8. [Ownership](#ownership)
9. [References and Borrowing](#references-and-borrowing)
10. [Slices](#slices)
11. [Structs](#structs)
12. [Enums](#enums)
13. [Pattern Matching](#pattern-matching)
14. [Modules and Packages](#modules-and-packages)
15. [Collections](#collections)
16. [Error Handling](#error-handling)
17. [Generics](#generics)
18. [Traits](#traits)
19. [Lifetimes](#lifetimes)
20. [Smart Pointers](#smart-pointers)
21. [Concurrency](#concurrency)
22. [Macros](#macros)
23. [Crates and Cargo](#crates-and-cargo)
24. [Testing](#testing)
25. [Documentation](#documentation)
26. [Best Practices](#best-practices)

---

## Introduction to Rust

Rust is a systems programming language focused on safety, speed, and concurrency. It achieves memory safety without a garbage collector and is designed to be both fast and safe.

---

## Installation

To install Rust, use `rustup`, the Rust toolchain installer:
```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
After installation, you can update Rust with:
```sh
rustup update
```

---

## Hello, World!

Create a new Rust project using Cargo:
```sh
cargo new hello_world
cd hello_world
```
Edit `src/main.rs`:
```rust
fn main() {
    println!("Hello, world!");
}
```
Run the program:
```sh
cargo run
```

---

## Variables and Constants

### Variables
```rust
fn main() {
    let mut x = 5;
    println!("The value of x is: {}", x);
    x = 6;
    println!("The value of x is: {}", x);
}
```

### Constants
```rust
const MAX_POINTS: u32 = 100_000;
```

---

## Data Types

### Scalar Types
- Integer
- Floating-point
- Boolean
- Character

### Compound Types
- Tuple
- Array

### Examples
```rust
fn main() {
    let x: i32 = 42;
    let y: f64 = 3.14;
    let is_active: bool = true;
    let character: char = 'A';

    let tuple: (i32, f64, u8) = (500, 6.4, 1);
    let array: [i32; 3] = [1, 2, 3];
}
```

---

## Functions

### Definition
```rust
fn main() {
    another_function();
}

fn another_function() {
    println!("Another function.");
}
```

### Parameters
```rust
fn main() {
    print_value(5);
}

fn print_value(x: i32) {
    println!("The value is: {}", x);
}
```

### Return Values
```rust
fn main() {
    let x = five();
    println!("The value of x is: {}", x);
}

fn five() -> i32 {
    5
}
```

---

## Control Flow

### If Statements
```rust
fn main() {
    let number = 6;

    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }
}
```

### Loops
- `loop`
- `while`
- `for`

### Examples
```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;
        if counter == 10 {
            break counter * 2;
        }
    };

    println!("The result is {}", result);

    let mut number = 3;

    while number != 0 {
        println!("{}!", number);
        number -= 1;
    }

    let a = [10, 20, 30, 40, 50];

    for element in a.iter() {
        println!("the value is: {}", element);
    }
}
```

---

## Ownership

### Ownership Rules
1. Each value in Rust has a variable that’s called its owner.
2. There can only be one owner at a time.
3. When the owner goes out of scope, the value will be dropped.

### Example
```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1;
    // println!("{}", s1); // This will cause an error
}
```

---

## References and Borrowing

### References
```rust
fn main() {
    let s1 = String::from("hello");
    let len = calculate_length(&s1);
    println!("The length of '{}' is {}.", s1, len);
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

### Mutable References
```rust
fn main() {
    let mut s = String::from("hello");
    change(&mut s);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```

---

## Slices

Slices let you reference a contiguous sequence of elements in a collection rather than the whole collection.

### String Slices
```rust
fn main() {
    let s = String::from("hello world");
    let hello = &s[0..5];
    let world = &s[6..11];
    println!("{} {}", hello, world);
}
```

### Array Slices
```rust
fn main() {
    let a = [1, 2, 3, 4, 5];
    let slice = &a[1..3];
    println!("{:?}", slice);
}
```

---

## Structs

### Definition
```rust
struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}
```

### Instantiation
```rust
fn main() {
    let user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };
}
```

### Methods
```rust
impl User {
    fn full_name(&self) -> String {
        format!("{} <{}>", self.username, self.email)
    }
}

fn main() {
    let user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };

    println!("{}", user1.full_name());
}
```

---

## Enums

### Definition
```rust
enum IpAddrKind {
    V4,
    V6,
}
```

### Instantiation
```rust
fn main() {
    let four = IpAddrKind::V4;
    let six = IpAddrKind::V6;
}
```

### Enums with Data
```rust
enum IpAddr {
    V4(String),
    V6(String),
}

fn main() {
    let home = IpAddr::V4(String::from("127.0.0.1"));
    let loopback = IpAddr::V6(String::from("::1"));
}
```

---

## Pattern Matching

### `match` Keyword
```rust
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> u32 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```

### `if let`
```rust
fn main() {
    let some_value = Some(3);
    if let Some(3) = some_value {
        println!("Three");
    }
}
```

---

## Modules and Packages

### Modules
```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

fn main() {
    crate::front_of_house::hosting::add_to_waitlist();
}
```

### Packages and Crates
Packages are a collection of crates. A crate can be a binary or a library.

---

## Collections

### Vectors
```rust
fn main() {
    let v: Vec<i32> = Vec::new();
    let v = vec![1, 2, 3];
}
```

### Strings
```rust
fn main() {
    let mut s = String::from("foo");
    s.push_str("bar");
}
```

### Hash Maps
```rust
use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);
}
```

---

## Error Handling

### `Result`
```rust
use std::fs

::File;
use std::io::ErrorKind;

fn main() {
    let f = File::open("hello.txt");

    let _f = match f {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {:?}", e),
            },
            other_error => panic!("Problem opening the file: {:?}", other_error),
        },
    };
}
```

### `panic!`
```rust
fn main() {
    panic!("crash and burn");
}
```

---

## Generics

### Definition
```rust
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in list {
        if item > largest {
            largest = item;
        }
    }
    largest
}
```

---

## Traits

### Definition
```rust
pub trait Summary {
    fn summarize(&self) -> String;
}
```

### Implementation
```rust
pub struct Article {
    pub headline: String,
    pub content: String,
}

impl Summary for Article {
    fn summarize(&self) -> String {
        format!("{}, {}", self.headline, self.content)
    }
}
```

### Default Implementation
```rust
pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}
```

---

## Lifetimes

### Basic Lifetime Annotation
```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

### Structs with Lifetimes
```rust
struct ImportantExcerpt<'a> {
    part: &'a str,
}

fn main() {
    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.').next().expect("Could not find a '.'");
    let i = ImportantExcerpt { part: first_sentence };
}
```

---

## Smart Pointers

### Box<T>
```rust
fn main() {
    let b = Box::new(5);
    println!("b = {}", b);
}
```

### Rc<T>
```rust
use std::rc::Rc;

fn main() {
    let a = Rc::new(5);
    let b = Rc::clone(&a);
    println!("a = {}, b = {}", a, b);
}
```

### RefCell<T>
```rust
use std::cell::RefCell;

fn main() {
    let x = RefCell::new(5);
    *x.borrow_mut() += 1;
    println!("x = {:?}", x);
}
```

---

## Concurrency

### Threads
```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {} from the spawned thread!", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {} from the main thread!", i);
        thread::sleep(Duration::from_millis(1));
    }

    handle.join().unwrap();
}
```

### Channels
```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
    });

    let received = rx.recv().unwrap();
    println!("Got: {}", received);
}
```

---

## Macros

### Declarative Macros
```rust
macro_rules! say_hello {
    () => {
        println!("Hello!");
    };
}

fn main() {
    say_hello!();
}
```

### Procedural Macros
Procedural macros are more complex and typically used for code generation.

---

## Crates and Cargo

### Creating a New Crate
```sh
cargo new my_crate
```

### Building and Running
```sh
cargo build
cargo run
```

### Adding Dependencies
Add dependencies in `Cargo.toml`:
```toml
[dependencies]
serde = "1.0"
```

---

## Testing

### Writing Tests
```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
```

### Running Tests
```sh
cargo test
```

---

## Documentation

### Writing Documentation
Use `///` for documentation comments:
```rust
/// Adds one to the given number.
///
/// # Examples
///
/// ```
/// let five = 5;
/// assert_eq!(6, add_one(five));
/// ```
fn add_one(x: i32) -> i32 {
    x + 1
}
```

### Generating Documentation
```sh
cargo doc --open
```

---

## Best Practices

### Tips
1. **Write Idiomatic Rust**: Follow Rust conventions and idioms.
2. **Use `rustfmt`**: Automatically format your code.
3. **Use `clippy`**: Catch common mistakes and improve your Rust code.
4. **Document Your Code**: Write clear and concise documentation.
5. **Test Thoroughly**: Write tests for all critical code paths.
6. **Handle Errors Gracefully**: Use `Result` and `Option` effectively.
7. **Keep Dependencies Updated**: Regularly update and audit dependencies.
8. **Learn from the Community**: Engage with the Rust community for best practices and support.

---

This tutorial provides a comprehensive overview of Rust, from basic concepts to advanced techniques. By mastering these topics, you'll be able to write safe, concurrent, and efficient Rust programs.