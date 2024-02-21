# Virtual Environments

Virtual environments let us isolate project dependencies, that is, the third
party libraries we use with each project. For example, if one project you are
working on depends on an older version of pandas, but you want to use the newest
version elsewhere, we could create seperate virtual environments for each
project.

## Creating a Virtual Environment

1. Create a virtual environment

    ```
    python -m venv env
    ```

    Where `env` is the name of the directory to create the virtual environment
    inside of. We'll assume you are also using `env` for the rest of the
    examples.

1. Add the `env` directory to your `.gitignore`.

## Activating and Deactivating

1. Activate the virtual environment

    ```
    source env/bin/activate
    ```

    From this point forward, your shell will exist inside the virtual
    environment.

1. Deactivating the virtual environment

    To leave the virtual environment:

    ```
    deactivate
    ```

## Installing Dependencies

!!!note "Virtual Environments"
    Each virtual environment is seperate from all the others, and also separate
    from your "global" python installation. Just because you've installed a
    library elsewhere, doesn't mean it will be available in a new virtual
    environment. Any libraries you plan on using must be explicitly installed.

0. Make sure the virtual environment is activated.

1. (If a `requirements.txt` file exists) Install any existing dependencies.

    ```
    python -m pip install -r requirements.txt
    ```

1. Add a new dependency.

    ```
    python -m pip install sklearn
    ```

1. Save all your installed dependencies to a text file.

    ```
    python -m pip freeze > requirements.txt
    ```

## Workflow

### Setting up a New Project

1. Create the virutal environment.
1. Install dependencies with pip.
1. Save the dependencies to `requirements.txt`.

### Starting Work on an Existing Project

1. Activate the virtual environment

1. Install the project dependencies from `requirements.txt`

    ```
    pip install -r requirements.txt
    ```

### Day-to-day project work

1. Activate the virtual environment.

1. Work on your project like you normally would.

1. Deactivate the virtual environment when you are done working on the project.

## Exercise

1. Create a directory named `flask_intro` within your `codeup-data-science`
   directory.
1. Within `flask_intro`, create a readme file that explains that this project is
   your repository to practice learning flask.
1. Initialize a git repository inside of `flask_intro`, then add and commit the
   readme file.
1. Create a new repository on github named `flask_intro`.
1. Link your local repository to the one you have created on github and push
   your work to github.

---

1. Create a new virtual environment. Be sure to add the virtual environment
   directory to your `.gitignore`.
1. Activate the virtual environment.
1. Start an interactive python session.
1. Import `numpy`. You should get an `ImportError` because we have not yet
   installed `numpy`. Exit the interactive session.
1. Install numpy, and then generate a `requirements.txt` file.
1. Add and commit the work that you've done.
