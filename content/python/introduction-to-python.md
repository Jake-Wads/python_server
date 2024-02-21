# Introduction

Python is a high-level, dynamic, interpreted programming language that is widely used within the data science community. 

We will exclusively use Python 3 for this course. When you search the internet for Python-related questions, verify the version of Python and the date the information was posted.



### Setting Up a Python Environment

We will use [Anaconda](https://www.anaconda.com/) to install and manage our Python environment. Anaconda is a distribution of Python that includes many libraries commonly used for data science. This will reduce the time spent installing packages and libraries.


**Note:** The following commands *do not* need to be run within a specific working directory.



1\. Use Homebrew to install Anaconda.


```bash

brew install --cask anaconda
```


2\. Verify your device's processor by clicking the Apple icon in the upper left-hand corner of the desktop and selecting *About This Mac*. This will be either **M1** or **Intel**.



3\. Set the PATH variable to include the location of the Anaconda distribution. Use the appropriate command based on the processor type.  


#### Intel processors

```bash
echo 'export PATH=/usr/local/anaconda3/bin:$PATH' >> ~/.zshrc
```

#### M1 andn M2 processors

```bash
echo 'export PATH=/opt/homebrew/anaconda3/bin:$PATH' >> ~/.zshrc
```


4\. Reload the configuration file to allow the changes to take effect.

```bash
source ~/.zshrc
```


5\. Verify a successful installation of the Python distribution. 


```bash
python --version
```

Example output:

```bash
Python 3.9.13
```

If this command prints a version number less than 3, something went wrong during the installation process.


---
## Using Python

There are many methods of creating and executing Python code. Lines of code can be typed and executed within a terminal using the Python **REPL** (also known as an interactive session.)



**REPL** is a *read-eval-print-loop* which *reads* input, *evaluates* the code, *prints* the results, and *loops* back to receive more input. 


Starting A REPL


```bash
python
```

The REPL prompt

```python
 >>>
```

Type a line of code and press enter to execute. Multiple lines may be separated by a semicolon.



Exit the REPL 

```python
 >>>quit()
```

Or use CTRL+D


!!!note "iPython"
    iPython extends the features available in the Python REPL and is included in the Anaconda distribution. Type `ipython` to launch this enhanced REPL.


### Getting Help

You can access an interactive help page or receive information about Python functions. 


Access interactive help from the REPL 


```python
>>> help()
```


Access documentation for the function `print`

```python
>>> help(print)
```


### Python Scripts


A Python executable file (or script) has the file extension `.py` and may be run using the command line. 


#### Writing and executing a script


1\. Exit the REPL.

2\. Create a text file which will contain a simple Python script with Visual Studio Code (or another text editor). 

```bash
code helloworld.py
```

3\. Edit the file to contain the following Python code:

```python
print('Hello, World!')
```


4\. Save the file and run the following command. 

```bash
python helloworld.py
```



### REPL vs Python Scripts

Make note of key differences between executing Python code with a REPL or with a script. 


REPL

- Prints errors and warning messages
- Prints the result(s) of *every* expression  


Script

- Prints errors and warning messages
- Prints results *only* when `print` statements are used


### Interactive scripts


Interactive scripts are fully executed and then a REPL session is launched.


`python -i myscript.py`



### Jupyter Notebooks


Project Jupyter is an interactive computing platform with which users can create Jupyter Notebooks. These notebooks are made of cells which contain executable Python code. The content can also be formatted with Markdown and embedded media. 



#### Creating a notebook


1\. Create and/or navigate to the directory that will contain your notebook.



2\. Launch the web-browser interface for a Jupyter Notebook.

```bash
jupyter notebook
```

3. Select the **New** icon and the *Python 3* option.


---
## Installing Packages


Modules, packages, and directories expand the capabilities of Python and provide specialized tools for Python programmers.


Some important terms:


**Script**: A file with executable code


**Module**: A file that is imported and accessed by other scripts


**Package**: Multiple, related modules which are used to perform specific tasks 


**Library**: Bundled code sources which are distributed for use



Python developers can make their packages available through the [Python Package Index (PyPi).](https://pypi.org/) These packages can be installed, removed, and updated with with a tool named [pip.](https://pypi.org/project/pip/)



### Example Syntax 

The following are helpful commands when using `pip` to install and manage Python packages. 

Install a package

```bash
pip install <package-name>
```

List installed packages

```bash
pip list
```

Update a package

```bash
pip install --upgrade <package-name>
```



## More Resources


In case you already installed Anaconda or if you are using bash instead of zsh, [this resource](https://gist.github.com/ryanorsinger/7d89ad58901b5590ec3e1f23d7b9f887) will help.


---

## Exercises

1. Create a new github repository named `python-exercises` to hold exercises for the python module.

    1. Create a new remote repository on github.com
    
    1. Clone this repository to your local device in `~/codeup-data-science` directory

    1. Create a .gitignore
    
    1. Create a README.md file that outlines the contents and purpose of your repository

    1. Add, commit, and push these two files.


1. Set the working directory to `~/codeup-data-science/python-exercises` and run `git status`. Is this a regular directory or a git repository?

1. Follow the steps in the lesson above in "Setting Up a Python Environment". 

1. Open Visual Studio Code and [install the Python extension](https://code.visualstudio.com/docs/python/python-tutorial) for helpful editing features.

1. Create a script named `python_introduction_exercises.py` that prints "Hello, World!" to the console. 

1. Run this program from the command line.

1. Modify the program to contain a variable named `greeting` that holds the message that you will print to the console.

1. Run your script interactively.

    `python -i python_introduction_exercises.py`

1. View the contents of the `greeting` variable.

1. Create a Jupyter notebook named `my_first_notebook`.

1. Execute at least 3 Python cells and make some notes that describe 3 keyboard shortcuts for Jupyter notebooks.

1. Use pip to install the `pydataset` library which contains datasets we will use. 

1. Add, commit, and push your work so far.