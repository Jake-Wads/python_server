# Data Science Environment Setup 

## Basics / Prerequisites

1. You need to have your Mac OS user account password handy and you will also need to have administration rights on your computer.

2. Open up a terminal to run the commands throughout this process. To find your terminal application, use the keyboard shortcut `command + spacebar` to launch Spotlight, then type in `Terminal` and launch the terminal application.

3. Install Xcode

    Xcode contains developer tools for MacOS. Execute the following command in your terminal. It may take a moment to download.

    ```
    xcode-select --install
    ```

4. Install Brew.

    [Homebrew](https://brew.sh/) is a package manager for MacOS. We'll use this to install the other pieces of software that we need.
    This installation process will prompt you to type in your password. **Notice** the command-line prompt to type in your password *does not* show asterisk signs `***` as you type. When prompted, confidently type your password in, then press enter. If there is a typo, type in your password and hit Enter again.

    ```
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```

## Tools

1. Install [VS Code](https://code.visualstudio.com/)
    - This is the text editor we will be using for the course. While Photoshop is built for editing photos and Word is built for writing letters, code editors like VS Code are optimized for authoring and editing code.

    ```
    brew cask install visual-studio-code
    ```

    - Once VS Code is installed, go to your Applications folder on your Mac, then right click on the VS Code icon. From the right click menu, select "Open". 
    - Run `git config --global core.editor 'code -w'` from your terminal to set VS Code as your default git editor.


1. Install [Sequel Pro](https://sequelpro.com/)

    This is the SQL client we will use for the course

    ```
    brew cask install sequel-pro
    ```

2. Install the MySQL command line client

    ```
    brew install mysql-client
    brew link --force mysql-client
    ```

## Python

1. Install Anaconda

    ```
    brew cask install anaconda
    ```

2. Add anaconda's bin directory to your path

    This will tell our system how to find all everything we just installed.

    Open up your `.bash_profile` file in VS Code by running this command

    ```
    code ~/.bash_profile
    ```

    Add the line below to this file:

    ```
    export PATH=/usr/local/anaconda3/bin:$PATH
    ```

    Save and close the file

3. Close any open terminals and open a new one.

4. Check your version of python

    Running the following command:

    ```
    python --version
    ```

    Should tell you that you are running python version 3.7.x if everything
    happened successfully.

## SSH Key Setup + Link to GitHub

1. Generate a public-private key pair.
    1. Copy the line below and replace `YOUR_NAME` with your first name.

    ```
    ssh-keygen -b 4096 -t rsa -f ~/.ssh/id_rsa -C 'YOUR_NAME@codeup'
    ```

    2. Recommend hitting `Enter` to skip the passphrase when prompted to "generate a passphrase" for your key pair.

2. Add your public SSH key to github

    This command will copy your public key to your clipboard.

    ```
    cat ~/.ssh/id_rsa.pub | pbcopy
    ```

    Then [go here to add your public SSH key to your github account](https://github.com/settings/ssh/new). 
        - Title your key after your laptop. A good title would be "Macbook Pro", "Codeup", or "Macbook Air", for example.
            - In the text area labeled **Key**, paste from your clipboard with `command + v`.

## Context

- What is anaconda?

    Anaconda is a distribution of python, that is, it provides an opinionated
    way to setup and install python. It also comes with many data science
    libraries for python pre-installed.

- Why are we modifying the `.bash_profile` file?

    This file describes how our shell is setup and in this file we are modifying
    the `PATH`. The `PATH` explains where to find commands that you can run in
    your terminal. In this case, we are basically telling our computer to use
    the python installation that we got from anaconda, instead of the
    (out-of-date) installation that comes with MacOS.

    After we modify this file, we'll need to close all existing terminals and
    open a new one so that the changes we made to our `PATH` are applied.