# Page Styling

In this lesson, we'll discuss CSS, which stands for Cascading Style Sheets and
provides styling and layout for HTML pages.

## Attributes

**Attributes** provide meta-information about an element and are defined in the
opening tag for the element.

```html
<a href="https://codeup.com">Codeup</a>
```

In the example above, the anchor tag has an `href` attribute, and the value of
the `href` attribute is `https://codeup.com`.

We can use a `style` attribute to add CSS to our elements:

```html
<p style="color: red">We have style!</p>
```

## Ways To Include CSS

There are several ways we can apply CSS to the elements on our page:

- The `style` attribute

    ```html
    <p style="color: red">We have style!</p>
    ```

- A `<style>` element

    ```html
    <style>
      p {
          color: red;
      }
    </style>
    ```

- A `<link>` element pointing to an external stylesheet (css file)

    ```html
    <link rel="stylesheet" href="/style.css" />
    ```

    ```css
    p {
        color: red;
    }
    ```

    The `<link>` element should go in the `<head>` of the html document.

    ```html
    <html>
    <head>
        <title>Title of the webpage</title>
        <link rel="stylesheet" href="/style.css" />
    </head>
    <body>
        <p>We Have Style!</p>
    </body>
    </html>
    ```

In general, external stylesheets are preferred for several reasong:

- easier organization
- easy to change out
- some performance optimizations

### Style Precedence

1. Inline: `style="..."`
1. The `<style>` element
1. An external stylesheet

## CSS Syntax

A language's **syntax** is the rules that define the language, or how the parts
of the language are put together.

CSS syntax is made up of **selectors**, **properties**, and **values**.

In general, the syntax looks like this:

```css
selector {
    property: value;
}
```

```css
h1 {
    text-align: center;
    font-size: 24px;
}
p {
    color: red;
}
```

We'll use the code above to elaborate.

- **Selectors**: Define what element(s) the rules apply to
    - `h1`
    - `p`
- **Properties**: The name for one rule
    - `text-align`
    - `font-size`
    - `color`
- **Values**: The value for one property
    - `center`
    - `24px`
    - `red`

## Common CSS Properties

- `background`: background color
- `color`: font color
- `font-family` (google fonts)
- `font-size`
- `font-weight`: bold or regular
- `text-align`: `left`, `right`, or `center`
- `text-decoration`: underline, strikethrough

```css
h1 {
    background: peachpuff;
    color: firebrick;
    font-family: cursive;
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    text-decoration: underline;
}
```

## Classes

We can define **classes** that provide some common styling to html elements.

Classes in HTML:

- We these classes by adding them to the `class` attribute of an element
- Multiple classes are separated by spaces
- The same class can appear on many different elements

Classes in CSS

- are a valid css selector
- The class name is prefixed with a `.`

In the example below, we can use a class to apply some styling to a single
specific list item:

```html
<ul>
  <li>one</li>
  <li class="highlight">two</li>
  <li>three</li>
</ul>
```

```css
.highlight {
    color: red;
    background: yellow;
    font-weight: bold;
}
```

## Divisions `<div>`s

- Indicate a division of content
- Can be useful in combination with CSS
- Can be used apply styles to every element within them

```html
<div class="column">
    <h1>Welcome to Codeup!</h1>
    <p>
        Codeup is a career accelerator located in San Antonio, Texas. At Codeup,
        we focus on two things: you and your success. Find a job within six
        months of graduation, or get 100% of your tuition returned.
    </p>
</div>
<div class="column">
    <p>Our Courses:</p>
    <ul>
        <li>Data Science</li>
        <li>Web Development</li>
    </ul>
</div>
```

- we can create columns with divs
- `width`: specify the width of an element
- the parent element must have `display: flex`

```css
body {
    display: flex;
}

.column {
    width: 50%;
}
```

## Bootstrap

[Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/) is
a CSS library that provides pre-defined classes for styling. Bootstrap also has
great documentation and examples that can be tweaked to your needs.

Bootstrap provides many different styled page components, utility classes, and a
grid system for laying out web pages.

## Further Reading

- [CSS Tutorial](https://www.w3schools.com/css/default.asp)
- [All the valid CSS Colors](https://www.w3schools.com/cssref/css_colors.asp)
- [Bootstrap Components](https://getbootstrap.com/docs/4.3/components/alerts/)
- [Bootstrap Grid](https://getbootstrap.com/docs/4.3/layout/grid/)
- [Bootstrap Utilities](https://getbootstrap.com/docs/4.3/utilities/borders/)

## Exercise

1. Link an external stylesheet to your page.

    Create a directory named `static` in the root of your project. Inside of
    this directory, create a file named `style.css` to put your custom css code.

    You can reference this file in your template as `/static/style.css`.

1. Make your pages look a little better.

    - Add some padding to the page content
    - Change the default fonts to sans-serif
    - Experiment with different CSS selectors and properties

1. Add Bootstrap to your page

    1. Include a `<link>` to bootstrap's css in the `<head>` of your document.
    1. Add the `p-5` to the `<body>` for some overall padding
    1. Add `text-center` to the heading
    1. Add `pb-4` for some horizontal whitespace
    1. Surround individual `<label>` and `<input>`s in a `form-group`
    1. Add `form-control` to `<input>`s
    1. Browse the bootstrap docs for more examples to play with

