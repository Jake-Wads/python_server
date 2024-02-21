# HTML

HTML, Hypertext Markup Language, provides the basic structure of web pages. In
this lesson we'll get a brief overview of HTML, and learn how to work with it in
flask.

## Basic HTML

At it's most basic, any plain text is valid HTML.

```html
Hello There!
```

But HTML can be much more than just plain text. HTML consists of **elements**,
which are defined by **tags** that contains **content**.

```html
<h1>Hello There!</h1>
```

This is an `h1` element, it indicates a first-level (`1`) heading (`h`)

!!!tip "Parts of an HTML Element"
    - Contents: everything inside the tags: `Hello There!`
    - Opening Tag: `<h1>`
    - Tag Name: `h1`
    - Closing Tag: `</h1>`

The content of an element can be another html element:

```html
<p>How are <strong>you</strong> today?</p>
```

Here a `strong` tag (indiciates it's contents should be bolded) is inside of a
`p` tag (indicating a paragraph).

## HTML Page Structure

A typical HTML document will look like this:

```html
<!doctype html5>
<html>
    <head>
        <title>My Page</title>
    </head>
    <body>
        <h1>A Heading</h1>
        <p>Some content</p>
    </body>
</html>
```

Notice several things:

- The entire document is enclosed in an `<html>` element
- the `<head>` element contains meta-information about the page
- the `<body>` element contains the actual content of the page

## Common HTML Elements

### Headings

There are 6 levels of heading. 1 is the most important, and 6 is the least.

```html
<h1>Hello</h1>
<h2>Hello</h2>
<h3>Hello</h3>
<h4>Hello</h4>
<h5>Hello</h5>
<h6>Hello</h6>
```

### Paragraphs `<p></p>`

```html
<p>Paragraphs indicate a paragraph of text.</p>

<p>Notice that the spacing in
the html code doesn't matter.</p>
<p>The browser will put a uniform amount of spacing for us.</p>
```

### Line Breaks `<br>`

```html
<p>These can be used<br> to break up<br> a paragraph.</p>
```

Notice there is not closing tag for this element. This is called a **void
element**. Void elements have no content.

### Lists

- `<li>`: a list item

Unordered Lists `<ul>`

```html
<p>At Codeup, we teach:</p>
<ul>
    <li>Data Science</li>
    <li>Web Development</li>
</ul>
```

Ordered Lists `<ol>`

```html
<ol>
    <li>Learn data science</li>
    <li>Find some data</li>
    <li>???</li>
    <li>Profit!</li>
</ol>
```

### Anchors `<a>`

- Hyperlinks
- Link to other web pages (internal or external)

```html
<p>Click <a href="https://google.com">here</a> to go to google.</p>
```

- The content of the `<a>` tag will be a clickable hyperlink
- The `href` **attribute** is part of the opening tag, and defines the target of
  the link

## Working with HTML Templates in Flask

To have your flask application show html pages:

1. Create a `templates` directory for your html templates to live in.

    `templates/index.html`

    ```html
    <!doctype html5>
    <html>
        <head>
            <title>My Flask Application</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is the index page!</p>
        </body>
    </html>
    ```

1. Reference the template from your server code:

    ```python
    from flask import render_template

    # ...

    @app.route('/')
    def index():
        return render_template('index.html')
    ```

In addition to showing plain HTML pages, flask lets us easily inject variable
values into our pages.

1. Pass additional keyword arguments to `render_template` to make those keyword
   arguments available as variables in the template.

    ```python
    def index():
        return render_template('index.html', name='Ada')
    ```

1. Reference the variables in the template

    Anything inside of double curly braces will be evaluated as a python
    expression, and the result will be printed out.

    ```python
    <h1>Hello, {{ name.upper() }}!</h1>
    ```

## Further Reading

- [HTML Tutorial](https://www.w3schools.com/html/default.asp)
- [Jinja2 Templating Engine](http://jinja.pocoo.org/)

## Exercise

1. Create an HTML page for your home page (i.e. the `/` route).
1. Create an HTML template for your `/roll-dice` url. It should show the dice
   roll inside of an HTML page, instead of as plain text.
