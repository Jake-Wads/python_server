# Git Branching

Branching in git allows different people (or the same person) to work in
parallel in different directions from a common starting place, and combine the
changes together. To explain this in more detail, we'll use an example.

Imagine you are working on a website, building a login page. You first write the
HTML, then the CSS, and finally the JavaScript for the page. A diagram of your
work might look like this:

```txt
|
* <-- add 'login.js'
|
|
* <-- add 'login.css'
|
|
* <-- add 'login.html'
```

Now imagine you and a friend decide to build a website together. Again, imagine
you are working on the login page. You are already finished with the HTML, and
ask for your friend's help. You decide that you will write the javascript for
the login page, and your friend will write the HTML. You agree that you should
be working on separate things and neither on of you will modify the HTML. Once
you both finish your respective parts, you will combine them together for the
completed project. You both create a copy of the HTML file, and then begin
working on your separate parts. A diagram of both of yall's work might look like
this:

```txt
|
* <-- add 'login.js' to the main project
|\
*  \ <-- add 'login.css' to the main project
|\  |
| | |
| | * <-- add 'login.js'
| | |
| * | <-- add 'login.css'
| | |
| |/
|/
* <-- add 'login.html'
^ ^ ^
| | |
`-+-+--- starting point
  | |
  `-+--- your friend's work
    |
    `--- your work
```

What happened is yall both created a copy of the project, and in parallel,
worked on different aspects of the project, then merged your work together.
Before yall combined the work, at any given time, you had no idea about the css
file, and your friend had no idea about the js file.

It turns our this is a very common pattern, so much so that git gives us a way
to formalize this process, through *branching*. In general, all git projects
will have a branch named `master`, that represents the main project. Different
individuals will *branch* off of master and do their work separate (that is,
make commits) from everyone else, then *merge* their branches back into master.
Here is the same diagram from above, but with git terminology applied (For the
purposes of illustration, we'll assume your name is Jerry, and your partner's
name is Beth):

*Note that every `*` represents one commit*

```txt
|
* <-- Merge branch jerry into master
|\
*  \ <-- Merge branch beth into master
|\  |
| | |
| | * <-- add 'login.js'
| | |
| * | <-- add 'login.css'
| | |
| |/
|/
* <-- initial commit
^ ^ ^
| | |
`-+-+--- master branch
  | |
  `-+--- beth branch
    |
    `--- jerry branch
```

### Merge Conflicts

What happens if both you and your teamate make changes to the same file when you
try to merge your changes together? The answer depends on where the changes were
made. We will stick with our exapmle from above and assume that both you and
your teamate made changes to the `login.html` file, in addition to css and js
files.

If you add the html for a navbar, and your teamate adds the html for a footer,
there shouldn't be too much conflict, you will just keep both of your changes.

If you changed the main heading on the page to say "Please Login To Continue",
and your teamate changed the same heading to say "Login Page", you will not be
able to simply keep both sets of changes, you will have to decide which changes
you want to keep.

Git behaves in a very similiar manner. When branches are merged together, git
will do it's best to merge the changes, but if both branches made a change to
the same line in the same file, we will have a situation known as a *merge
conflict*. This is git telling us that it cannot automatically reconcile the
changes, and we will have to manually decide how to combine the changes
together.

```txt
|
* <-- Merge Conflict!
|\
*  \ <-- Merge branch beth into master
|\  |
| | |
| * | <-- changed the wording on the main heading on the login page
| | |
| | * <-- change heading on login page
| | |
| | * <-- add 'login.js'
| | |
| * | <-- add 'login.css'
| | |
| |/
|/
* <-- initial commit
^ ^ ^
| | |
`-+-+--- master branch
  | |
  `-+--- beth branch
    |
    `--- jerry branch
```

In general you should try to plan out ahead of time what work you plan to do
(that is what files you will be chaning) in your branch, so that you and your
team don't run into too many merge conflicts.

## Working with branches

Git gives us the ability not just to create different branches, but also to
switch between different branches. This can be very useful to check out the work
your teamates are doing, or even see what the state of your project was at a
different point in time. However, it is very important to keep in mind what
branch you are currently on when you are making changes to files, or commiting
changes made. While there are various ways to fix it, you don't want to make a
commit on the wrong branch!

### Commands

Generally speaking, make sure you have a clean working directory (i.e. you have
committed any changes) before doing any branch manipulation.

- Create a new branch based off of the branch we are currently on

    ```bash
    git branch <new-branch-name>
    ```

- Switch to a different branch

    ```bash
    git checkout <other-branch>
    ```

- Create a new branch based off of the branch we are currently on and switch to it

    ```bash
    git checkout -b <new-branch-name>
    ```

- Rename the current branch

    ```bash
    git branch -m <new-name>
    ```

- Merge another branch into the branch you are currently on

    ```
    git merge <other-branch>
    ```
