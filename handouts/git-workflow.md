# Git Workflow

## Getting Work on GitHub | First time repo setup

1. Create the repo

    ```
    git init
    ```

1. Add and commit your files for the first time

    ```
    git add .
    git commit -m 'Initial Commit'
    ```

1. Add a remote and push to GitHub

    ```
    git remote add ...
    git push origin master
    ```

## Day to day git workflow

1. Make changes to files...

1. Add and commit the changes you've made

    ```
    git add FILE1 FILE2
    git commit
    ```

1. Push the changes up to GitHub

    ```
    git push origin master
    ```

## Miscelanneous

- Moving all files with a certain extension to a directory

    ```
    mv *.ipynb codeup
    ```

- Creating the `atom` command

    ```
    ln -s /Applications/Atom.app/Contents/Resources/app/atom.sh /usr/local/bin/atom
    chmod +x /usr/local/bin/atom
    ```

- Changing the default git commit editor

    ```
    git config --global core.editor 'atom -n -w'
    ```

- [Codeup curriculum on the git cli](https://java.codeup.com/appendix/git/cli/)

