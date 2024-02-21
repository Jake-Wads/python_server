# PDB

Python Debugger

see also `pudb` and `pudb3` for a ncurses cool solution

## Control Flow

- `n`: go to the next line, "skip over" any function calls
- `s`: step; step into any new function calls
- `c`: continue until a breakpoint is found
- `r`: continue until the current function returns

## Inspecting State

- `p`: print the results of the expression that follows
- `pp`: pretty print the results of the expression that follows
- `l`: list the source code
- `ll`: long list the source code
- `a`: print the arguments to the current function call
- `w`: `where`; print a stack trace

## Breakpoints

- `b`: set a breakpoint, or list all the current breakpoints
- `cl`: clear, remove a breakpoint

- Set a breakpoint on line 11

    ```
    (Pdb) b 11
    ```

- Set a breakpoint on line 11 that will only trigger if `foo == 'bar'`

    ```
    (Pdb) b 11, foo == 'bar'
    ```

- Set a breakpoint for when the foo function from the bar module is hit

    ```
    (Pdb) b bar.foo
    ```
