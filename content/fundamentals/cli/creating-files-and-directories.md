# Creating and Moving

There are a number of ways to create files and directories on the linux filesystem. We are going to show you some of the most common commands.

## touch

How do we create new files from the command line? Just like this:

```
% touch newfile.txt
```

The `touch` command allows us to create a new empty file of whatever name we specify. In this case, our file will show up like this:

```
% ls -l

-rw-r--r--   1 user  wheel         0 Nov 18 11:00 newfile.txt
```

You can even create multiple files at once, like this:

```
% touch one two three four five
```

## mkdir

What if we want to create a directory?  There is the `mkdir` command:

```
% mkdir secret_plans
```

What happens to your desktop if you `cd` to it, and make this directory?

Just like `touch`, you can create multiple directories inside your current one simultaneously:

```
% mkdir one two three four
```


## mv

Occasionally we want to move files from one location to another. We can use the following command, and our path, to accomplish this.

`mv` needs two pieces of information, or arguments, to work. The first is the original file you want to move, the second is the location where you want to move it.

```
% mv ~/newfile.txt ~/Desktop/newfile.txt
```

This command moves our `newfile.txt` from the home directory, and puts it on our Desktop. What if you only want to use relative paths?  Let's say you were already in your home directory:

```
% pwd
/Users/john
```

You run `ls` to see what files are in there:

```
% ls -a
.
..
newfile.txt
```

Now, we know where we are, and we know where we want to go, so let's specify our current file and the location to move it to using relative paths.

```
% mv newfile.txt ../newfile.txt
```

This would move the file up one directory from our current location.

`mv` can also rename files with a slight variation in our syntax:

```
% mv current_filename.txt new_filename.txt
```

This would not actually move our file from its current directory, but it would rename it inside of our current directory.



## Exercise

1. Create a new directory on your desktop called "test".
2. Create some new files in there, named "test1", "test2", and "test3".
3. Create another directory inside of test, called "secret_files".
4. Create some new files inside of that.
5. Navigate back to your desktop and run `ls -l test`.  What do you see?
6. Now try `ls -l test/secret_files`.  Do you see your secret files?
7. Try running `ls -R test`. What does the `-R` flag do?
8. Create a file inside of the `test` named `.hidden_file`. Does this file show up when you run `ls`? What could you do to make it show up?
9. You've seen that we can create hidden files by prepending the file name with a `.`. Does this also work for directories? Try to create a hidden directory and add files to it. Do all the files in a hidden directory need to be hidden files? 
1.  Create a new file on your desktop called "move_it.txt".
2.  Move this file into your home directory.
3.  Now move it into your documents folder, where it belongs.
4.  Change the name of the file, within your documents folder, to `important.txt`.

