# Other Command Line Topics and Commands

## Command History

You can press the up and down arrow keys to go backwards and forwards through your command history in the shell. This can be very useful if you previously typed a very long or complicated command that you need to modify or run again.

## Interrupting Programs

Pressing `ctrl-c` will "interrupt" most programs. This can usually be used to stop a long running or misbehaving process.

For example, an infinite loop created in Python can be interrupted using the `ctrl-c` command.

## Getting Help

### Built-in Help

Most commands have a built-in help message that can be displayed by passing one of the following arguments:

```
-h
--help
help
```

For example, try running:

```
% git --help
```

### Man Pages

Man (manual) pages are documentation that come with most unix distributions. They tend to be highly technical, and most serve as a reference for most commands (as opposed to a tutorial on how to use them).

```
% man COMMAND_NAME
```

- `d` to go down a half page
- `u` to go up a half page
- `q` to quit
- `/` to search for something

## Comments

The `#` character tells your shell to ignore anything past it.

```
% # pressing enter after this line does nothing 
```

Often times you will see this character to explain what a command is doing, either before, or inline with the command:

```
% # list all the files
% ls
```

```
% ls -lah # all files, long format, human-readable sizes
```

## Other Commands

- `code` is a command that will launch VS Code for you, either opening up a directory, or a specific file

    ```
    % code . # launch VS Code in the current directory
    % code somefile.txt # open somefile.txt in VS Code (creates it if it doesn't exists)
    ```

- `grep` can be used to search for text in a file

    ```
    % grep PATTERN myfile.txt
    ```

- `rm` is used to remove a file(s)

- `find` is used to search for files and can perform more advanced actions

- `cat` can be used to display the contents of a file(s) 

- `less` is the pager program that works just like in the man pages, and is another way to display file contents on the command line

- `open` is specific to MacOS and will try to guess which program to use to open a given file 

- `head` and `tail` can be used to view the first or last few lines of a file

- `pbpaste` and `pbcopy` (exclusive to MacOS) can be used to show and set the contents of your clipboard

## Keyboard Shortcuts

Not only will these keyboard shortcuts work in your terminal, they will work in most places in MacOS where you need to input text:

- `ctrl-a`: go to the beginning of the line
- `ctrl-e`: go to the end of the line
- `ctrl-k`: delete from the cursor to the end of the line
- `ctrl-l`: clear the screen
- `ctrl-w`: delete one word backwards


## Further Resources
- https://explainshell.com/
- [Full Text download of *The Linux Command Line*, By William Shotts](http://linuxcommand.org/tlcl.php) 
- [How to Use the Command Line in Linux, Windows, and Mac](https://www.youtube.com/watch?v=BFMyUgF6I8Y)