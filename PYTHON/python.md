# Beginner Level Python Tutorial

## Introduction to Python

### What is Python?
- Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991.
- Python supports multiple programming paradigms including procedural, object-oriented, and functional programming.

### Why Python?
- Python is widely used in various fields such as web development, data science, machine learning, artificial intelligence, automation, and more.
- It has a large standard library and an active community, making it easy to find solutions to problems and learn from others.
- Python's simple syntax and readability make it suitable for beginners as well as experienced developers.

### Installing Python
- Visit the official Python website [python.org](https://www.python.org/) and download the installer for your operating system.
- Run the installer and follow the installation instructions.
- Make sure to check the option to add Python to the system PATH during installation so you can run Python from the command line.

## Basic Syntax

### Variables and Data Types
- In Python, variables are used to store data values. You can assign a value to a variable using the assignment operator `=`.
- Python supports various data types including integers, floats, strings, booleans, lists, tuples, dictionaries, and sets.
- Example:
    ```python
    # Variable assignment
    x = 10
    name = "John"
    is_student = True

    # Data types
    age = 25           # Integer
    height = 5.9       # Float
    message = "Hello"  # String
    ```

### Comments
- Comments are used to add notes or explanations within the code. They are ignored by the Python interpreter.
- Single-line comments start with `#`, while multi-line comments can be enclosed within triple quotes `'''` or `"""`.
- Example:
    ```python
    # This is a single-line comment

    '''
    This is a multi-line
    comment
    '''
    ```

### Indentation
- Python uses indentation to define code blocks, such as those within loops, conditional statements, and function definitions.
- Indentation is typically done using four spaces.
- Example:
    ```python
    if x > 5:
        print("x is greater than 5")
    else:
        print("x is less than or equal to 5")
    ```

### Basic Input/Output
- Python provides built-in functions for taking input from the user (`input()`) and displaying output (`print()`).
- Example:
    ```python
    # Input from user
    name = input("Enter your name: ")

    # Output
    print("Hello,", name)
    ```

## Operators

### Arithmetic Operators
- Arithmetic operators are used to perform mathematical operations such as addition, subtraction, multiplication, division, etc.
- Examples:
    ```python
    x = 10
    y = 5

    addition = x + y
    subtraction = x - y
    multiplication = x * y
    division = x / y
    ```

### Comparison Operators
- Comparison operators are used to compare two values and return a boolean result (`True` or `False`).
- Examples:
    ```python
    x = 10
    y = 5

    greater_than = x > y
    less_than_or_equal = x <= y
    equal = x == y
    not_equal = x != y
    ```

### Logical Operators
- Logical operators are used to combine conditional statements and return a boolean result.
- Examples:
    ```python
    x = 10
    y = 5

    logical_and = (x > 5) and (y < 10)
    logical_or = (x > 5) or (y > 10)
    logical_not = not (x > 5)
    ```

## Control Flow

### Conditional Statements (if, elif, else)
- Conditional statements are used to execute different blocks of code based on certain conditions.
- Example:
    ```python
    age = 20

    if age >= 18:
        print("You are an adult")
    elif age >= 13:
        print("You are a teenager")
    else:
        print("You are a child")
    ```

### Loops (for, while)
- Loops are used to repeat a block of code multiple times.
- The `for` loop is used when you know the number of iterations in advance, while the `while` loop is used when you want to repeat a block of code until a condition is met.
- Examples:
    ```python
    # For loop
    for i in range(5):
        print(i)

    # While loop
    x = 0
    while x < 5:
        print(x)
        x += 1
    ```

### Break and Continue
- The `break` statement is used to exit a loop prematurely, while the `continue` statement is used to skip the rest of the code inside the loop for the current iteration and move to the next iteration.
- Examples:
    ```python
    # Break example
    for i in range(10):
        if i == 5:
            break
        print(i)

    # Continue example
    for i in range(5):
        if i == 2:
            continue
        print(i)
    ```

## Data Structures

### Lists
- Lists are ordered collections of items that can be of any data type.
- Lists are mutable, meaning you can change the elements after the list is created.
- Example:
    ```python
    # Creating a list
    numbers = [1, 2, 3, 4, 5]

    # Accessing elements
    print(numbers[0])   # Output: 1

    # Modifying elements
    numbers[0] = 10

    # Adding elements
    numbers.append(6)

    # Removing elements
    numbers.remove(3)
    ```

### Tuples
- Tuples are ordered collections of items similar to lists, but they are immutable, meaning you cannot change the elements after the tuple is created.
- Example:
    ```python
    # Creating a tuple
    person = ("John", 25, "Male")

    # Accessing elements
    print(person[0])   # Output: John

    # Tuples are immutable
    # person[0] = "Jane"  # This will raise an error
    ```

### Dictionaries
- Dictionaries are unordered collections of key-value pairs.
- Each key-value pair in a dictionary is separated by a colon `:` and different pairs are separated by commas `,`.
- Example:
    ```python
    # Creating a dictionary
    student = {
        "name": "John",
        "age": 25,
        "gender": "Male"
    }

    # Accessing elements
    print(student["name"])   # Output: John

    # Modifying elements
    student["age"] = 26

    # Adding elements
    student["grade"] = "A"

    # Removing elements
    del student["gender"]
- **Sets:**
  - Sets are unordered collections of unique items. They are useful for performing mathematical set operations like union, intersection, and difference.
  - Example:
    ```python
    # Creating a set
    fruits = {"apple", "banana", "cherry"}

    # Adding elements
    fruits.add("orange")

    # Removing elements
    fruits.remove("banana")

    # Set operations
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    union = set1.union(set2)
    intersection = set1.intersection(set2)
    difference = set1.difference(set2)
    ```

**Functions:**

- **Defining Functions:**
  - Functions are blocks of code that perform a specific task and can be reused.
  - Example:
    ```python
    def greet(name):
        return f"Hello, {name}"

    # Calling the function
    print(greet("Alice"))   # Output: Hello, Alice
    ```

- **Arguments and Parameters:**
  - Functions can take arguments, which are values passed to the function when it is called.
  - Example:
    ```python
    def add(a, b):
        return a + b

    # Calling the function with arguments
    print(add(3, 4))   # Output: 7
    ```

- **Default Parameters:**
  - Functions can have default parameters, which are used if no argument is provided for that parameter.
  - Example:
    ```python
    def greet(name="Guest"):
        return f"Hello, {name}"

    # Calling the function without an argument
    print(greet())   # Output: Hello, Guest

    # Calling the function with an argument
    print(greet("Alice"))   # Output: Hello, Alice
    ```

- **Variable Scope:**
  - Variables defined inside a function are local to that function and cannot be accessed outside of it.
  - Example:
    ```python
    def my_function():
        x = 10   # Local variable
        print(x)

    my_function()   # Output: 10
    # print(x)   # This will raise an error because x is not defined outside the function
    ```

**Modules:**

- **Importing Modules:**
  - Modules are files containing Python code that can be imported and used in other Python files.
  - Example:
    ```python
    # Importing the math module
    import math

    # Using a function from the math module
    result = math.sqrt(16)
    print(result)   # Output: 4.0
    ```

- **Creating Modules:**
  - You can create your own modules by writing Python code in a file and saving it with a `.py` extension.
  - Example:
    ```python
    # Create a file named mymodule.py with the following code:
    def greet(name):
        return f"Hello, {name}"
    ```

    ```python
    # Importing and using the custom module
    import mymodule

    print(mymodule.greet("Alice"))   # Output: Hello, Alice
    ```

**File Handling:**

- **Reading Files:**
  - Python provides functions to read from files.
  - Example:
    ```python
    # Opening a file in read mode
    file = open("example.txt", "r")

    # Reading the content of the file
    content = file.read()
    print(content)

    # Closing the file
    file.close()
    ```

- **Writing Files:**
  - Python provides functions to write to files.
  - Example:
    ```python
    # Opening a file in write mode
    file = open("example.txt", "w")

    # Writing content to the file
    file.write("Hello, World!")

    # Closing the file
    file.close()
    ```

- **Appending to Files:**
  - You can also append content to an existing file.
  - Example:
    ```python
    # Opening a file in append mode
    file = open("example.txt", "a")

    # Appending content to the file
    file.write("\nAppend this text.")

    # Closing the file
    file.close()
    ```

**Exception Handling:**

- **Try, Except, Finally:**
  - Exception handling in Python is done using `try`, `except`, and `finally` blocks to catch and handle errors.
  - Example:
    ```python
    try:
        # Code that may raise an exception
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("This will always execute")
    ```

**Object-Oriented Programming (OOP):**

- **Classes and Objects:**
  - Classes are blueprints for creating objects. An object is an instance of a class.
  - Example:
    ```python
    # Defining a class
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            return f"Hello, my name is {self.name}"

    # Creating an object of the class
    person1 = Person("John", 25)

    # Accessing attributes and methods
    print(person1.name)   # Output: John
    print(person1.greet())   # Output: Hello, my name is John
    ```

- **Inheritance:**
  - Inheritance allows a class to inherit attributes and methods from another class.
  - Example:
    ```python
    # Defining a base class
    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            return "Some sound"

    # Defining a derived class
    class Dog(Animal):
        def speak(self):
            return "Bark"

    # Creating an object of the derived class
    dog = Dog("Buddy")

    # Accessing attributes and methods
    print(dog.name)   # Output: Buddy
    print(dog.speak())   # Output: Bark
    ```

**Conclusion:**

This tutorial covered the basics of Python, including its syntax, control flow, data structures, functions, modules, file handling, exception handling, and object-oriented programming. Python is a versatile language with a wide range of applications. Keep practicing and exploring more advanced topics to enhance your Python skills. Happy coding!
