# Navigating the Filesystem

Let's examine some concepts that we need to be aware of when navigating our computers via the command line.

## Paths and Directory Separators

A file path is a line of text that specifies a unique location in a file system. It points to that location by specifying the hierarchy of directories that lead up to that location. For example, `Documents/Secret_Diary/My_Crush.txt` indicates that the file `My_Crush.txt` is in the directory `Secret_Diary`, which in turn is in the folder `Documents`. We separate each directory (or "folder") with the `/` character. Those of you with a background in Windows may be more familiar with the `\` for this purpose, however that character has a different meaning in UNIX systems and most programming languages.

## The Root Directory

The `/` character separates one directory from another in a path, so `Parent_Directory/Child_Directory` represents one folder nested inside of another. But what about just the `/` on its own? When used by itself, the `/` represents what is called the "root" directory. Remember that directories form a hierarchy. If we were to think of that hierarchy as a tree that branches up and out into child directories (and grandchild, and great-grandchild, etc), the `/` would be the root of that tree. Thus, using just the `/` on its own will take you to the absolute base, or "root", of your filesystem.

## Absolute and Relative File Paths

There are two ways to represent any given location within our filesystem: the **absolute** path, and the **relative** path.

You can think of these in the following way. Let's say you had a house, and you wanted to give your friend directions to the guest bedroom. You could do that in the following way:

> Starting at the front door, go up the main stairs, down the hallway to your left, and enter the last room on the right. That is the guest bedroom.

What if instead you were trying to tell them how to find the guest bathroom? It is inside the guest bedroom. You could give them all the same directions over again:

> Starting at the front door, go up the main stairs, down the hallway to your left, enter the last room on the right, and go in the first door to the right. That is the guest bathroom.

These are both examples of "absolute" paths. You are giving your friend directions to a room from a fixed point of entry in your house (the front door). Thus, you are giving them *absolute* directions. But what if your friend is already in the guest bedroom? Giving an absolute path then would be rather excessive. In that case, you would probably say:

> Go in the first door to the right. That is the guest bathroom.

This is a "relative" path. You are giving your friend direction to a room *relative* to where they currently are.

Applying these concepts to the filesystem, let's say that we are currently in our home directory, whose path is:

```
/Users/john/
```

If we wanted to point to the `Documents` directory in there, we could give the **absolute** path to it:

```
/Users/john/Documents
```

Or we could use the **relative** path:

```
Documents
```

Because we are in `/Users/john`, both these paths point to the same `Documents` directory.

Remember that:

- The **absolute** path will tell you where you are according to the root of the filesystem. It will *not* change, because the root of the filesystem will always be in the same place.
- The **relative** path *will* change depending on your current location. It changes because your current location within the filesystem will change as you move around it.

## The Home Directory

In the previous example, we mentioned a "home" directory. Every user on a UNIX based computer has a home directory. This is a place where that user can store their personal files and settings. In Linux, users' home directories are typically stored inside of `/home`. The home directory for a user named `steve` would be:

```
/home/steve
```

Mac OS X does things a little bit differently. The home directory on your laptop is inside of `/Users`. If your username is `billy`, then your home directory would be:

```
/Users/billy
```

In either case though, you will use your home directory a lot. In fact, you refer to it so often, that people developed a shortcut for it: `~`. The `~` points to your home directory, on whatever system you are on, no matter what your username is. So, a path like the following:

```
~/Movies
```

refers to a directory called `Movies` inside of your home directory.


## Print Working Directory

We have a command which can tell us where we are in our current filesystem, similar to the *"You Are Here"* marker on a map. We can see where we are in our current filesystem with `pwd`, the "print working directory" command.

```
% pwd
/Users/username
```

Know that `pwd` will always give us an **absolute** path on our filesystem, never a relative one.

## Change Directory

We can move around our filesystem with the `cd`, or "change directory" command.

```
% cd
```

When we use `cd` we have to specify where we want to go. We can do this by using either the absolute or relative path to that directory.

This would take you to your home directory using an absolute path:

```
% cd /Users/john
```

This would take you to your home directory using the shorthand `~`:

```
% cd ~/
```

So, how does our previous command `ls` factor into this scenario?  Let's find out.

Go to your home directory, and type in:

```
% ls
```

You're going to see something like this:

```
% ls
Applications    Documents    Library    Music       Public
Desktop         Downloads    Movies     Pictures
```

This shows us the directories listed under our current one.  Now we can choose to `cd`, or jump into one of those directories.  Let's go into our Desktop and list the files there.

```
% cd Desktop/
% ls
```

What do you see?  Do you see files and folder names listed here that correspond with what's actually on your desktop?  What happens when you create a new folder on the desktop, and then run `ls` again? Can you see that the new folder you created shows up in your command line as well?

There is one more thing we'd like to show you.  Type `ls -lah` and take a look at what is listed.  It should look something like this:

```
% ls -lah
total 17032
drwx------+  36 user  staff   1.2K Jan 23 10:01 .
drwxr-xr-x+  51 user  staff   1.7K Jan 21 17:32 ..
-rw-r--r--@   1 user  staff    21K Jan 23 10:01 .DS_Store
-rw-r--r--    1 user  staff     0B May  6  2014 .localized
-rw-r--r--@   1 user  staff   136K Jan 11 09:14 random_file.txt
-rw-r--r--@   1 user  staff    16K Jan 15 14:12
```

Do you see the following characters listed above your files/folders?

```
.
..
```

These are two additional ways of representing directories with shorthand characters, similar to how our home directory can be accessed anywhere with `~`.  These characters are important when we are attempting to navigate using relative paths.

- The `.` single dot, represents our current directory.
- The `..` double dot, represents the parent directory, or the directory immediately above our current directory.

You can use commands like these the traverse upwards:

```
# Go up one directory
% cd ../

# Go up two directories
% cd ../../

# Go up three directories
% cd ../../../
```

You can traverse downwards by naming the directory you want to move into that is contained in the dictionary to the left of it:

```
% cd ./Desktop/some_directory/another_directory/
```

You can even chain the double dot with other directories to go up one or more levels and then back down some other part of the directory tree:

```
# Go up one directory, and then down another directory
% cd ../another_directory/
```

It’s important to note the leading `./` and trailing slash are not always necessary. The following commands both have the same result, when issued from the home directory:

```
% cd ./Desktop/some_directory/another_directory/
% cd Desktop/some_directory/another_directory
```

The prompt is smart enough to know what you are trying to do in both instances. Did you notice that both of those are relative paths? As you use these commands more, you will get more comfortable with the syntax. It will become second nature to you!

## Exercise

1.  Start at your home directory.  Change directory into your Desktop.
2.  Find another folder to `cd` into, and keep going until you have run out of directories to traverse downwards.
3.  Start moving your way back up with `cd ../`.  What happens when you try to `cd ../../`?
4.  Start over again at your home directory, and pick a place on your filesystem to jump to using the absolute path.
5.  Pick another one, far away from that place, and jump to it using `cd`.
6.  Make sure to use `pwd` to check your current location if you get lost.