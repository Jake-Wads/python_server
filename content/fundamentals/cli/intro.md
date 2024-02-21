# Introduction to the CLI

We will explore the command-line interface (CLI), and the Z shell (Zsh). A command-line interface is a text-based interface. This means interaction with the interface is done by typing in commands and reading the text output. This is in contrast to a graphical user interface (GUI) which relies on users interacting with images, such as clicking on an icon.


## Interface

We will start by introducing some basic command-line concepts and get ourselves familiar with the interface. The command-line interface only interprets text commands. There are no buttons, icons, or any point-and-click interactions whatsoever. Because of this, understanding what commands are available to you and how to use them is very important.

- **terminal**: The graphical interface to the shell; the way you interact with the shell.
- **shell**: The program that reads your input and produces output. The program that controls your interaction with the operating system.

To access the command-line interface you will need a terminal application. Your Mac came with a terminal application preinstalled, called Terminal.app. It is installed in your Applications folder, inside of Utilities. Another option for a terminal is [iTerm2](http://iterm2.com), which is a slightly more featureful terminal. Either one will work fine for this course.

### The Prompt

When you open your terminal, you will see a prompt. A prompt is just that: it prompts you, the user, for input. The input you provide is a text-based command or series of commands to accomplish a desired goal. All of the commands you type into the command-line will be prefixed by this prompt automatically.

Your prompt should look something like:

```
User@Macbook ~ %
```

The first part of this prompt is the username, or the account through which you are using your laptop. In this example, the username is `User`. The username is followed by an `@` symbol and the name of the machine. In this case, the computer is named `Macbook`. The final piece of information is the current working directory. In this example, the current working directory is represented by the `~` symbol, which means we are in the home directory. The `%` symbol is explained below.

### Issuing Commands

Most text-based commands follow a set pattern. First, type out the command you would like to run. Next, type out any arguments the command needs. Separate the command and each of the arguments with spaces. Finally, we can issue that command to the computer by pressing the `Return` or `Enter` key.

Spaces are used as separators in the command-line inputs. For that reason most commands are single word and it is recommended to avoid using spaces in your file names.

### Z shell

The software which powers this prompt (aka, our shell) is called [Z shell][wiki-zsh]. Z shell is started for you automatically as soon as you open your terminal, and will continue running in the background until you close the window. You can think of it like the Finder and the Dock for the command line (or Windows Explorer and the Start menu).

Let's start our exploration of the command line by finding out what version of Z shell we are using. The command to do that is:

```
zsh --version
```

Go ahead and type that in at your prompt, it should look something like this:

```
User@Macbook ~ % zsh --version
```

Once that is done, hit enter. You should see output printed to the window:

```
zsh 5.8 (x86_64-apple-darwin21.0)
```

After the output you should see another prompt just like before. We provided the Z shell some input. It interpreted our command, and gave us back some output. Now it’s waiting for us to give it more input.

### The `%` Symbol

There was a last part of the prompt we didn't discuss: the `%` at the end. By convention this is there to let you know you are logged in as a regular user, as opposed to a superuser or "root". Remember though that the rest of the prompt will change depending on what your computer is named, what your username is, and the directory in which you're currently working. Since the `%` is relatively constant, it is typically used to indicate commands to be typed into a prompt. So in future examples, rather than seeing:

```
User@Macbook ~ % zsh --version
```

You will see:

```
% zsh --version
```

[wiki-zsh]: https://en.wikipedia.org/wiki/Z_shell


## Listing Files

The primary use for Z shell is to manage files. But how do we know what files are around for us to manage? The key to this is the command `ls`. `ls` is short for "list." It lists the contents of a directory. To see what files are in the directory we are currently in, simply use:

```
% ls
```

If your home directory looks something like this:

![Codeup home directory](/img/prework/home-folder.png)

The output we see in the terminal would be:

```
% ls
Desktop        Downloads    Movies      Pictures
Documents      Library      Music       Public
%
```

## Specifying a Directory

By default, `ls` lists the contents of the directory we are currently in. What if we wanted to see the contents of a different directory? We can tell `ls` to show the contents of a different place by adding that as an argument. For example, We can see the contents of the `Documents` folder using the following command:

```
% ls Documents
```

My Documents folder only has four files in it, so the output I see is:

```
% ls Documents
File 1  File 2  File A  File B
%
```

Yours will surely be different.

**Note: The Mac file system is *not* case sensitive. That means that it sees `Documents` and `documents` as the same folder. Most other systems do not behave this way and would treat those as two different folders. Be careful when writing out the names of files and folders. In general, programmers tend to avoid capital letters in filenames whenever possible.**

## Flags

Most CLI commands can take in what are called "flags". Flags are options that can change the way a command behaves. Typically a flag takes the format of a `-` followed by a single letter or number, or two `--` and a word. `ls` can take in several different flags that change its output, some common ones are:

```
-a : all files
-l : long format
```

If we wanted to see the contents of our current directory in "long" format, we would do the following:

```
% ls -l
```

That output would look something like:

```
% ls -l
total 0
drwx------+  4 user  staff   136 Jan  5 01:40 Desktop
drwx------+  7 user  staff   238 Jan  5 16:20 Documents
drwx------+  3 user  staff   102 Nov  5 01:12 Downloads
drwx------+ 42 user  staff  1428 Jan  5 01:37 Library
drwx------+  3 user  staff   102 Nov  5 01:03 Movies
drwx------+  3 user  staff   102 Nov  5 01:03 Music
drwx------+  3 user  staff   102 Nov  5 01:03 Pictures
drwxr-xr-x+  5 user  staff   170 Nov  5 01:03 Public
%
```

The long format outputs the directory listing in a series of columns resembling a table. Much of the information `ls` displays is beyond the scope of this lesson. However, the last three columns represent: the file size (in bytes), the last date the file was modified on, and the name of the file. For example, the first file listed is `136` bytes, was last modified on `Jan  5 01:40`, and its name is `Desktop`.

You can also use two or more flags together. For example, if you wanted to see *all* the files in a directory in long format, you could run:

```
% ls -l -a
```

However, short flags (flags represented by a single dash followed by a single letter) can be combined together. Rather than listing each flag individually you could simply type:

```
% ls -la
```

This syntax will produce exactly the same output as the previous example.

## Exercises


1. Check what version of zsh you have.
1. Try each of the flags for `ls` individually and then combine flags together. 
1. List the contents of some other directories. 
1. Can you combine both flags and a different directory?
1. What happens if you try to list the contents of two or more directories?
1. [Look over the reference manual for the `ls` command.](https://www.unix.com/man-page/FreeBSD/1/ls/)