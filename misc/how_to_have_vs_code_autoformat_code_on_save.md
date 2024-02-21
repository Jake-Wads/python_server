1. Figure out if you have `autopep8` installed

    You can copy and paste the command below into your terminal. It will output "Good to go!" if you have `autopep8` installed, otherwise it will say "autopep8 not found".

    ```
    if which autopep8 > /dev/null ; then echo 'Good to go!' ; else echo 'autopep8 not found!' ; fi
    ```
   
1. If you don't have it installed, install `autopep8`

    ```
    conda install autopep8
    ```

1. In VS Code, open your settings
    
    Command + Shift + P -> type "settings" -> choose "Preferences: Open Settings (JSON)"

1. After the last item in your setttings, add a comma

1. Add the code below to your settings:

    ```
    "editor.formatOnSave": true,
    "python.formatting.provider": "autopep8"
    ```

1. That's it! You should be good to go now