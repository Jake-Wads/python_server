# Developing Data Products

- 9:00 [Virtual Environments](#virtual-environments)
- 9:15 [Building a model](#building-a-model)
- 10:15 [Flask Intro](#flask-intro)
- 11:30 [HTML Templates](#html-templates)
- 13:30 [HTML Forms](#html-forms)
- 15:00 [Styling](#styling)
- 16:00 [Next Steps](#next-steps)

## Virtual Environments

1. What are they
1. Demo creation, activation, import `np`, install `np`, `deactivate`

## Building a model

Copy the file from the curriculum and run it.

## Flask Intro

1. Create + run a `hello world` server
    1. Python Code
    1. `FLASK_APP`, `FLASK_ENV`, `flask run`
1. Hello `name` route `/hello/<name:str>`
1. Bonus Exercise `/<greeting>/<name>`
1. Exercise Review: emphasize request-response

## HTML Templates

1. create `templates/index.html` and wire it up -- about me / personal site page
1. Basic HTML, headings, paragraphs, links, lists
1. Passing data, single item plus a list
1. Bonus Exercise `/count/<to>`, `/count/from/<from>/to/<to>/by/<by>`
1. Bonus Exercise `/<greeting>/<name>/<times>`
1. Exercise Review: emphasize request-response

## HTML Forms

1. Forms HTML code -- counting form
1. Handling form submission on the backend
    1. seperate POST route
    1. `request.form['key']`
    1. Seperate HTML page to show results
1. Same path, diff request methods
1. Same names for form input, `request.form[..]`, template variable, etc
1. Exercise Review: emphasize request-response data flow

## Styling

1. Static content with flask
1. CSS basics
    1. Style Attribute, Tag, External Style Sheet; precedence
    1. syntax: selectors, properties, values
    1. Common properties: `background`, `color`, `font-family`, `font-size`,
       `border`, `text-align`
    1. Classes -- highlight even numbers
    1. divs: `.container` + `.column` + `display: flex`
    1. Bootstrap

## Next Steps

1. `return jsonify(data_structure)`
1. How to make this application live?
    1. Domain name + DNS; webserver setup
    1. [Cods Deployment Guide](https://github.com/zgulde/cods/blob/master/docs/python-deployment-guide.md)
