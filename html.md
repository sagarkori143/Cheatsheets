# Beginner Level HTML Tutorial

## Table of Contents
1. [Introduction to HTML](#introduction-to-html)
    - [What is HTML?](#what-is-html)
    - [Why HTML?](#why-html)
    - [Installing a Text Editor](#installing-a-text-editor)
2. [Basic Structure](#basic-structure)
    - [HTML Document Structure](#html-document-structure)
    - [Doctype Declaration](#doctype-declaration)
    - [HTML Elements](#html-elements)
    - [HTML Attributes](#html-attributes)
3. [Common HTML Elements](#common-html-elements)
    - [Headings](#headings)
    - [Paragraphs](#paragraphs)
    - [Links](#links)
    - [Images](#images)
    - [Lists](#lists)
        - [Ordered List](#ordered-list)
        - [Unordered List](#unordered-list)
        - [Definition List](#definition-list)
    - [Tables](#tables)
    - [Forms](#forms)
4. [Semantic HTML](#semantic-html)
    - [Semantic Elements](#semantic-elements)
5. [HTML5 Features](#html5-features)
    - [Audio and Video](#audio-and-video)
    - [Canvas](#canvas)
    - [Geolocation](#geolocation)
6. [HTML Best Practices](#html-best-practices)
    - [Use Semantic Elements](#use-semantic-elements)
    - [Keep Code Clean and Readable](#keep-code-clean-and-readable)
    - [Optimize Images](#optimize-images)
    - [Validate HTML](#validate-html)
7. [Conclusion](#conclusion)

## Introduction to HTML

### What is HTML?
- HTML (HyperText Markup Language) is the standard language for creating web pages and web applications.
- HTML describes the structure of a web page using markup.
- HTML elements are represented by tags.

### Why HTML?
- HTML is the foundation of web development, used to structure content on the web.
- It is easy to learn and widely supported across all web browsers.
- Knowledge of HTML is essential for creating and designing websites.

### Installing a Text Editor
- To write HTML, you need a text editor. Some popular options include:
  - Visual Studio Code (https://code.visualstudio.com/)
  - Sublime Text (https://www.sublimetext.com/)
  - Atom (https://atom.io/)
  - Notepad++ (https://notepad-plus-plus.org/)
- You can also use a simple text editor like Notepad (Windows) or TextEdit (Mac).

## Basic Structure

### HTML Document Structure
- An HTML document is made up of various elements that define its structure.
- Example:
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>My First HTML Page</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is my first HTML page.</p>
    </body>
    </html>
    ```

### Doctype Declaration
- The `<!DOCTYPE html>` declaration defines the document type and version of HTML.
- It should be the first line in an HTML document.

### HTML Elements
- HTML elements are defined by a start tag, some content, and an end tag.
- Example:
    ```html
    <p>This is a paragraph.</p>
    ```

### HTML Attributes
- HTML elements can have attributes that provide additional information about the element.
- Attributes are always included in the opening tag and usually come in name/value pairs like `name="value"`.
- Example:
    ```html
    <a href="https://www.example.com">This is a link</a>
    ```

## Common HTML Elements

### Headings
- Headings are used to define headings of different levels in an HTML document.
- There are six levels of headings, from `<h1>` to `<h6>`.
- Example:
    ```html
    <h1>This is a heading 1</h1>
    <h2>This is a heading 2</h2>
    ```

### Paragraphs
- The `<p>` element defines a paragraph.
- Example:
    ```html
    <p>This is a paragraph.</p>
    ```

### Links
- The `<a>` element (anchor) is used to create hyperlinks.
- Example:
    ```html
    <a href="https://www.example.com">Visit Example.com</a>
    ```

### Images
- The `<img>` element is used to embed images.
- The `src` attribute specifies the path to the image.
- Example:
    ```html
    <img src="image.jpg" alt="Description of image">
    ```

### Lists
- HTML supports ordered lists (`<ol>`), unordered lists (`<ul>`), and definition lists (`<dl>`).

#### Ordered List
- Example:
    ```html
    <ol>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ol>
    ```

#### Unordered List
- Example:
    ```html
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>
    ```

#### Definition List
- Example:
    ```html
    <dl>
        <dt>Term 1</dt>
        <dd>Definition of Term 1</dd>
        <dt>Term 2</dt>
        <dd>Definition of Term 2</dd>
    </dl>
    ```

### Tables
- The `<table>` element is used to create tables.
- Example:
    ```html
    <table>
        <tr>
            <th>Heading 1</th>
            <th>Heading 2</th>
        </tr>
        <tr>
            <td>Data 1</td>
            <td>Data 2</td>
        </tr>
    </table>
    ```

### Forms
- Forms are used to collect user input.
- Example:
    ```html
    <form action="/submit" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br>
        <input type="submit" value="Submit">
    </form>
    ```

## Semantic HTML

### Semantic Elements
- Semantic elements clearly describe their meaning in a human- and machine-readable way.
- Examples of semantic elements:
    ```html
    <header>Header content</header>
    <nav>Navigation links</nav>
    <section>Section content</section>
    <article>Article content</article>
    <footer>Footer content</footer>
    ```

## HTML5 Features

### Audio and Video
- HTML5 introduced `<audio>` and `<video>` elements for media playback.
- Audio example:
    ```html
    <audio controls>
        <source src="audio.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    ```

- Video example:
    ```html
    <video width="320" height="240" controls>
        <source src="movie.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    ```

### Canvas
- The `<canvas>` element is used to draw graphics via scripting (usually JavaScript).
- Example:
    ```html
    <canvas id="myCanvas" width="200" height="100" style="border:1px solid #000000;"></canvas>
    ```

### Geolocation
- The Geolocation API allows the user to provide their location to web applications.
- Example:
    ```html
    <button onclick="getLocation()">Try It</button>
    <p id="demo"></p>

    <script>
    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
        } else {
            document.getElementById("demo").innerHTML = "Geolocation is not supported by this browser.";
        }
    }

    function showPosition(position) {
        document.getElementById("demo").innerHTML = "Latitude: " + position.coords.latitude +
        "<br>Longitude: " + position.coords.longitude;
    }
    </script>
    ```

## HTML Best Practices

### Use Semantic Elements
- Use semantic HTML elements to enhance the readability and accessibility of your web pages.

### Keep Code Clean and Readable
- Write clean, readable code with proper indentation and comments.

### Optimize Images
- Optimize images for faster loading times. Use appropriate file formats and sizes.

### Validate HTML
- Use HTML validators (like the W3C Markup Validation Service) to check your HTML for errors and ensure it adheres to standards.

## Conclusion

This tutorial covered the basics of HTML, including document structure, common elements, forms, semantic HTML, and HTML5 features. HTML is a fundamental technology for web development, and understanding it is crucial for creating well-structured, accessible, and functional web pages. Keep practicing and exploring more advanced topics to enhance your HTML skills. Happy coding!
