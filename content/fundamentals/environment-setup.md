# Environment Setup

In order to work effectively on the command line, and be ready for fundamentals, run through each setup step carefully. 

1. Open up a terminal to run the commands throughout this process.

    1. Open up Spotlight Search by pressing Command+Space 
    
    1. Type "terminal" to open the built-in terminal application

1. Install Xcode, a developer tool for MacOS.

    1. Run in the terminal:

        ```
        xcode-select --install
        ```

    1. Follow the prompts that come up after running this command.

1. Install [Homebrew](https://brew.sh/), a package manager for MacOS. This will be used to install the other pieces of software that we need.

    1. Run in the terminal:

        ```
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        ```

    1. When you are prompted for a password, enter the password for the current user account on your Mac.
        
        **The password does not show as you type** 

    1. Hit your ENTER key, even though it looks like nothing is there.
    
    1. Read the results messages. You may be prompted to run a couple of commands to correctly point your path. Copy and 
    paste necessary commands into the terminal. 


1. Install [VS Code](https://code.visualstudio.com/), a text editor.

    1. Run in the terminal:
    
        ```
        brew install visual-studio-code
        ```

    1. Run the command below to make VS Code your editor for git-related operations:

        ```
        git config --global core.editor 'code -w'
        ```

1. Install [MySQL Workbench](https://dev.mysql.com/downloads/workbench/), a SQL client.

    1. Download the application from the above link. 


1. Install the MySQL command line client.

    1. Run in the terminal: 

        ```
        brew install mysql-client
        brew link --force mysql-client
        ```

1. Authorize your laptop to push to your github account, by generating a public-private key pair.

    1. Run in the terminal:

        ```
        ssh-keygen -b 4096 -t rsa -f ~/.ssh/id_rsa
        ```

    1. **When prompted for a password, DO NOT ENTER A PASSWORD, just press the return/enter key.**
    

1. Add your public key to github.

    1. Run this in the terminal to copy your public key to your clipboard. 

        ```
        cat ~/.ssh/id_rsa.pub | pbcopy
        ```

    1. Then [go here to add the key to your github account](https://github.com/settings/keys)
    
    1. Click "Add SSH Key".

    1. The title for your key is specific to your computer. Name it something like "Laptop", "Macbook" or "Codeup".

    1. Paste from your clipboard into the large "Key" text box.
