# HTML Forms

HTML forms let us interact with the user.

1. Define a route that will display your form

    ```python
    @app.route('/my-first-form')
    def my_first_form():
        return render_template('my-first-form.html')
    ```

1. Create a form on an html page:

    A form consists of multiple form elements, one of the most common being an
    `input` element.

    ```html
    <!-- inside of my-first-form.html -->
    <h2>Please fill out this form:</h2>
    <form action="/make-greeting" method="POST">
        <label for="title">Preferred Title</label>
        <input id="title" type="text" name="title">
        <br />
        <label for="name">Your Name</label>
        <input id="name" type="text" name="name">
        <br />
        <input type="submit" />
    </form>
    ```

    The form's `action` attribute determines which url the form data will be
    submitted to.

1. Define a route that handles the form submission:

    ```python
    from flask import request

    @app.route('/make-greeting', methods=['POST'])
    def handle_form_submission():
        name = request.form['name']
        title = request.form['title']

        greeting = 'Hello, '

        if title != '':
            greeting += title + ' '

        greeting += name + '!'

        return render_template('greeting-result.html', greeting=greeting)
    ```

1. Create an html page named `greeting-result.html` to show the results

    ```html
    <!-- inside of greeting.html -->
    <h1>{{ greeting }}</h1>
    ```

## Exercises

1. Create the form outlined in the lesson above that greets a user when they
   type in their name.

1. Displaying Model Output

    Now we will build a web app that lets a user type a message into an input
    field and uses our model to look at the user's input and predict whether or
    not what they submitted is spam.

    1. Create a route within your application that shows an HTML form that
       contains an input field for a text message.
    1. Create an endpoint that handles the form submission. Inside of this
       function, your should use the `predict` function from your `model` module
       to make a prediction about the user's input.
    1. Display the user's input along with the model's prediction in another
       html page.
