# Flask

Flask is a library for quickly building web servers.

After activating your virtual environment, run

```
python -m pip install flask
```

to install flask.

## Setup A Web Server Hello World

We have the following code inside of `server.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'
```

Let's break down the pieces:

```python
app = Flask(__name__)
```

Creates the **flask application**. We can then use the application to define
**routes**, or urls within our webserver.

```python
@app.route('/')
def index():
    return 'Hello, World!'
```

The `@` prefix defines a python **decorator** that will act on the function
definition that follows it.

What we are saying here is that when the `/` url is visited, run the `index`
function, and whatever the function returns will be what the web server returns
to the browser.

### Running Our Application

Make sure your virtual environment is activated, and you have installed flask,
then run the following from your terminal:

```
# assuming we've created and activated our virtual environment
export FLASK_APP=server.py
export FLASK_ENV=development
flask run
```

Now we can visit our website in the browser and interact with it.

## Exercise

1. Create a `server.py` file. Include a route for `/` that returns a "Hello,
   World" message.
1. Using the curriculum as a guide, run your application and read the messages
   that appear on application startup.
1. Visit your website in your browser and verify that you see your hello world
   message.
1. Write the code necessary so that when `/roll-dice` is visited, a random
   number between 1 and 6 is shown. **Bonus** show 3 random numbers.
