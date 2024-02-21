# Merge Conflicts

Merge conflicts can happen when you and your teammate have both made changes to
the same file. You will encounter the merge conflict when you pull from github.

**_Make sure you have added and comitted all your work before pulling._**

After pulling and creating a merge conflict...

0. Use `git status` to check and see which files git thinks are conflicted

1. Compare the different versions of the file:

    To use your version:

    ```
    git checkout --ours some_notebook.ipynb
    ```

    To use the version from github:

    ```
    git checkout --theirs some_notebook.ipynb
    ```

    You should open up the notebooks and compare the differences at this point.

1. `git add` the conflicted file, **after** you've figured out which version to
   use and run the appropriate `git checkout` command

1. `git commit` to complete the pull process

1. `git push` your work up to github
