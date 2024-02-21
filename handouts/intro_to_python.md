# Intro to Python

## Why Python
- Fast
- Much higher level and closer to natural language than most other languages.
- Tremendous amount of Data Science and Machine Learning resources in Python.

## Perspective

- Programming languages are languages with syntax, grammer, vocaulary, idioms, un-written rules
- Python - all the syntax and idioms are in one place: <https://www.python.org/dev/peps/pep-0008/>
- There's a *lot* of learning going on and you're making tons of connections when learning to solve problems programmatically w/ a programming language
  1. You're learning the programming language itself
  2. You're learning how to think programmatically (think in terms of sequences of steps, automation)
  3. You're learning how to debug or create new functionality using the scientific method
     - Look
     - Guess
     - Test
     - Conclude
     - Repeat
  4. *Code does what you tell it to do, not what you intend, expect, or hope it will do.*
  5. Code is executable instructions

## Orientation

- The `.py` file extension means that a file should contain syntactically correct Python.
- A Python script runs from top to bottom stopping when running a syntax or type error.
- A `.ipynb` file extension is created for code run inside of a Jupyter Notebook.

## How to Write and Run Python Code
1. Write your Python code to `filename.py` file using `VS Code` or another editor. Run with `python filename.py`.
2. Use a `Jupyter Notebook` and write Python code into code cells in a `filename.ipynb` file. Run by typing `jupyter notebook` or `jupyter notebook filename.ipybn`
3. Use `ipython` to run an interactive Python shell (REPL). Use this for a scratch pad or sandbox.

## 5 Parts of Any Program (one or more of the following)
- Input (from sensors, people, other computers, other programs, text files, etc...)
- Mathematical or logical operations (*Sequence*)
- Conditional Execution (*Selection*)
- Repetition (*Iteration*)
- Output

## 3 Big Ideas Around Data Processing Programs
1. Sequence (flow-of-control, order of operations for math and logical operators)
   - Code from top to bottom unless told otherwise
   - Code follows PEMDAS mathematical order of operations
   - Code follows logical order of operations (usually solved with parentheses)
   - 1 + 1 => 2
2. Selection (boolean operators, conditionals)
3. Iteration (loops)

Every complex data manipulation and transformation comes back to a combination of these 3 simple 

## Recommended Practices

- Make a `.gitignore` file for every project! 
  - Add `.DS_Store` and `env.py` to it first.
  - Add `.ipynb_checkpoints` too
- (As always), `git add`, `git commit`, and `git push` your work every day.
- *Prefer to use `.py` files for group work, rather than Jupyter Notebooks.*
- Add `.ipynb_checkpoints/` and `__pycache__` to your `.gitignore` file.
- Prefer `ipython` to `python` for the REPL (read-evaluate-print-loop)

### Reference

- `code filename`, `code foldername`, or `code .` launch VS Code accordingly
- `conda list` to shows conda installed packages. `pip list` shows pip installs.
- `python --version` to check the python version
- `python` from the CLI to launch the python REPL
- `ipython` from CLI launches iPython
- `jupyter notebook` to launch the jupyter notebook server
- `jupyter notebook foldername` or `jupyter notebook filename` launches accordingly
- When using `ipython` or a Jupyter Notebook, type a function name followed by a question mark like `len?` to learn more about that function.